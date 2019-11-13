import math
from github import Github

g = Github("4e5ff86857cf7f1cda72cf7fab4fe988115df46b")
avgPy = 0
num = 0
isDone = 0
repositories = g.search_repositories(query='language:python')
for repo in repositories:
 avgPy = avgPy + repo.stargazers_count
 num = num+1
 print(num, " = ", repo.stargazers_count)
 if num > 100 :
  break

avgPy = avgPy/num
print(math.ceil(avgPy))
