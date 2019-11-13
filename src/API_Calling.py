import math
from github import Github

def get_avg_of_repo(repositories):
 num = 0
 avg = 0
 for repo in repositories:
  if num >= 1000:
   break
  avg = avg + repo.stargazers_count
  num = num + 1
  print(num, " = ", repo.stargazers_count)
 return avg

def calLanguageStars()


g = Github("Github Access token") # access token for github
avgPy,avgJS,avgJ = 0 #var for the average star of python contributures
repositoriesPython = g.search_repositories(query='language:python') #get the repositories that use python
repositoriesJavaScript = g.search_repositories(query='language:javascript') #get the repositories that use python
repositoriesJAVA = g.search_repositories(query='language:python') #get the repositories that use python
avgPy = get_avg_of_repo(repositoriesPython)/1000
print(math.ceil(avgPy))