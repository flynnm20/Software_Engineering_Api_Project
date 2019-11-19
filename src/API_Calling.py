import peewee
from github import Github
import plotly.express as px
import math
import json
import matplotlib.pyplot as plt
import numpy as np
from enum import unique
import pandas

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


def get_avg_of_repo(repositories):
    num = 0
    avg = 0
    for repo in repositories:
        if num == 800:
            break
        avg = avg + repo.stargazers_count
        num = num + 1
    return avg


# access token for github
g = Github("GITHUB_ACCESS_TOKEN")

google = g.get_organization("Facebook")
members = google.get_members()
num = 0
avg_Str = []
nm_Lng = []
for mem in members:
    repos = mem.get_repos()
    avgStars = get_avg_of_repo(repos)
    langKnown = getRepoLanguagesCount(repos)
    avg_Str.append(avgStars)
    nm_Lng.append(langKnown)
    print("Gotone")
    num = num+1
    if num >= 10:
        break

print("Out of loop")

N = 50
x=avg_Str
y=nm_Lng
colors = 100
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
print("Dataset generated")

plt.scatter(x,y)
plt.show()
