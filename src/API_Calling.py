import peewee
from github import Github
import plotly.express as px
import math
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from enum import unique
from io import StringIO
from flask import Response
import pandas as pd

#get the amount of languages from the repos
def getRepoLanguagesCount(repos):
    retLang = []
    num = 0
    for r in repos:
        lang = r.get_languages()
        for l in lang:
            if l not in retLang:
                retLang.append(l)
    for n in retLang:
        num = num + 1
    return num


# get the avg star of a users repos
def get_avg_of_repo(repositories):
    num = 0
    avg = 0
    for repo in repositories:
        if num == 800:
            break
        avg = avg + repo.stargazers_count
        num = num + 1
    return (avg/num)


#
def getimage(orgStr):
 area = (30 * np.random.rand(50)) ** 2  # 0 to 15 point radii
 print("Dataset generated")
 fig = plt.figure()
 plt.scatter(avg_Str,nm_Lng, figure = fig)
 return fig


def createPandasTable():
 listOfOrgs = ["Apple","Google","Facebook","amzn",]
 avg_Str = []
 nm_Lng = []
 orgForRef = []
 for orgStr in listOfOrgs:
     org = g.get_organization(orgStr)
     members = org.get_members()
     num = 0
     # get avg stars and lang used for each member of an organization up to a set limit
     for mem in members:
         repos = mem.get_repos()
         avgStars = get_avg_of_repo(repos)
         langKnown = getRepoLanguagesCount(repos)
         avg_Str.append(avgStars)
         nm_Lng.append(langKnown)
         orgForRef.append(orgStr)
         num = num + 1
         if num >= 30:
             break
     print(orgStr)
 df1 = pd.DataFrame({'org': orgForRef, 'avg_Star': avg_Str, 'num_Lang': nm_Lng})
 return df1

#Main
# access token for github
g = Github("edb0efbc1665d703212a3ee8e95ecf7cc5e05a07")
DataTable = createPandasTable()
print(DataTable)
data = DataTable.to_json(orient='columns')
print(data)
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
#GoogImage = getimage("Google")
#FBImage = getimage("Facebook")
#plt.show()
