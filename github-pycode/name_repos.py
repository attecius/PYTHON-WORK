#code to get to know the repositries
from github import Github
g = Github("attecius","nanaksingh@98")


for repo in g.get_user().get_repos():
    print(repo.name)

