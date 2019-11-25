import time
import peewee
from github import Github
import math
import json
import matplotlib.pyplot as plt
from plotly.offline import plot
import plotly.express as px
from plotly.subplots import make_subplots
import operator
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from enum import unique
from io import StringIO
from flask import Response
import pandas as pd

#create a strongest language view where we get the most popular language and compare the repos that their in.
# create a bar chart with ORG/Language at the base and hight being the avg repos

def appToData(tmpLangData, langData):
    for l in tmpLangData:
        if l not in langData:  # if doesn't exist then add key and val.
            langData[l] = tmpLangData[l]
        else:  # else add the new val to old val
            langData[l] = langData[l] + tmpLangData[l]
    return langData

class Org:
    def __init__(self, name):
        self.name = name
        self.langData = {}
        self.members = []
        self.fig = None
        self.mostUsedLang = None
        self.mostUsedLangStar = 0
        self.AvgSList = []
        self.LnKnList = []
        self.org = g.get_organization(self.name)
        self.membersList = self.org.get_members()
        self.num = 0
        # get avg stars and lang used for each member of an organization up to a set limit
        df = pd.DataFrame
        for m in self.membersList:
            repos = m.get_repos()
            tmpLangData = getRepoLanguagesCount(repos)
            self.langData = appToData(tmpLangData, self.langData)
            self.langKnown = len(tmpLangData)
            self.AvgSList.append(get_avg_of_repo(repos))
            self.LnKnList.append(self.langKnown)
            self.num = self.num + 1
            if self.num >= 1:
                break
        self.mostUsedLang = max(self.langData, key=self.langData.get)

def getRepoLanguagesCount(repos):
    retLang = {} # dict of all lang listed and the stars associated with that language
    num = 0
    for r in repos:
        lang = r.get_languages()
        for l in lang:
            if l not in retLang: # if doesn't exist then add key and val.
                retLang[l] = r.stargazers_count
            else: # else add the new val to old val
                retLang[l] = retLang[l] + r.stargazers_count
    return retLang


# get the avg star of a users repos
def get_avg_of_repo(repositories):
    num = 0
    avg = 0
    for repo in repositories:
        if num == 800:
            break
        avg = avg + repo.stargazers_count
        num = num + 1
    if num == 0:
        num = 1
    return (avg/num)





#Main
# access token for github
g = Github("edb0efbc1665d703212a3ee8e95ecf7cc5e05a07")
listOfOrgs = ["Facebook", "amzn", "Apple", "Google", "IBM"]
most_used_lang = []
most_used_lang_vals = []
fig = plt.figure()
n = 0
colours = ["b", "g", "r", "c", "y"]
plt.figure(1)
aS= []
lK = []
index = []
for i in listOfOrgs:
    tmpOrg = Org(i)
    strings = [tmpOrg.mostUsedLang,'/',tmpOrg.name]
    barLabel = ''.join(strings)
    most_used_lang.append(barLabel)
    most_used_lang_vals.append(tmpOrg.langData[tmpOrg.mostUsedLang])
    for h in  tmpOrg.AvgSList:
        index.append(i)
    for a in tmpOrg.AvgSList:
        aS.append(a)
    for b in tmpOrg.LnKnList:
        lK.append(b)
    n = n+1

scatData = pd.DataFrame({"Org":index, "Average Stars": aS, "Languages Known":lK})
barData = pd.DataFrame({"Org":listOfOrgs,"UsedLang":most_used_lang, "Vals":most_used_lang_vals})


fig = px.scatter(scatData,x="Average Stars",y = "Languages Known", color="Org")
plot(fig)
time.sleep(30)
figBar = px.bar(barData, x = "UsedLang", y = "Vals", color="Org")
plot(figBar)
