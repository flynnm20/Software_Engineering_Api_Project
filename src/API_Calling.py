import math
import json
from enum import unique
from github import Github
import peewee


def getRepoLanguagesCount(repos):
 retLang = []
 num = 0
 for r in repos:
  lang = r.get_languages()
  for l in lang:
   if l not in retLang:
    retLang.append(l)
 for n in retLang:
  num = num +1
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



g = Github("20907a9e9a82869e2095f2186f2438de081dbb02") # access token for github

google = g.get_organization("Google")
members = google.get_members()
num = 0
data = {}
data["points"] = []
for mem in members:
 repos = mem.get_repos()
 avgStars = get_avg_of_repo(repos)
 langKnown = getRepoLanguagesCount(repos)
 data['points'].append({'avgStr' : avgStars, 'lngKnwn':langKnown})
 print("Users avg star rating is =",avgStars, "Users number of languages known is ",langKnown)
 if num > 10:
  break
 print(mem)
 num=num+1
with open['points.txt','w+'] as outfile:
 json.dump(data, outfile)


'''
avgPy = 0
avgJS =0
avgJ = 0 #var for the average star of python contributures
repositoriesPython = g.search_repositories(query='language:python') #get the repositories that use python
repositoriesJavaScript = g.search_repositories(query='language:javascript') #get the repositories that use python
repositoriesJAVA = g.search_repositories(query='language:java') #get the repositories that use python

avgPy = get_avg_of_repo(repositoriesPython)/800
avgJ = get_avg_of_repo(repositoriesJAVA)/800
print(math.ceil(avgPy))
'''

