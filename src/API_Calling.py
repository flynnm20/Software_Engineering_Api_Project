import time
from github import Github
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objects as go
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

# Class for orginizations and is used to store data regarding the orginiations.
class Org:
    def __init__(self, name):
        self.name = name
        self.langData = {} # dic for the languages and the sum of the stars used.
        self.members = []
        self.fig = None
        self.mostUsedLang = None
        self.mostUsedLangStar = 0 # calculated at the end
        self.AvgSList = [] # x axis of the scatter plot
        self.LnKnList = [] # y axis of the scatter plot
        self.org = g.get_organization(self.name)
        self.membersList = self.org.get_members()
        self.num = 0
        self.labels = []
        self.values = []
        # get avg stars and lang used for each member of an organization up to a set limit
        df = pd.DataFrame
        for m in self.membersList: # get teach dot for the values
            repos = m.get_repos()
            tmpLangData = getRepoLanguagesCount(repos)
            self.langData = appToData(tmpLangData, self.langData)
            self.langKnown = len(tmpLangData)
            self.AvgSList.append(get_avg_of_repo(repos)) # append new x value
            self.LnKnList.append(self.langKnown) # append new y value
            self.num = self.num + 1
            if self.num >= 20:
                break
        self.mostUsedLang = max(self.langData, key=self.langData.get) # assign most used language

# Get the unique instances of languages for all the repos.
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
g = Github("ACCESS TOOKEN")
listOfOrgs = ["Facebook", "amzn", "Apple", "Google", "IBM"]
most_used_lang = []
most_used_lang_vals = []
n = 0
aS= []
lK = []
index = []
for i in listOfOrgs: # cycle through each specified 
    tmpOrg = Org(i)
    print(i)
    strings = [tmpOrg.mostUsedLang,'/',tmpOrg.name] # used as label for the barchart
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
#Data has been gathered and now needs to be ploted
scatData = pd.DataFrame({"Org":index, "Average Stars": aS, "Languages Known":lK}) # create a pd dataframe for use in ploting
barData = pd.DataFrame({"Org":listOfOrgs,"UsedLang":most_used_lang, "Vals":most_used_lang_vals})
fig = px.scatter(scatData,x="Average Stars",y = "Languages Known", color="Org") # calculate the dots and set the colours based on organizations
plot(fig) # plot the scatter plot
time.sleep(30) # this is to allow users time to allow the program to run if needed.
figBar = px.bar(barData, x = "UsedLang", y = "Vals", color="Org")
plot(figBar) # plot the bar chart
