import os

from github import Github
from dotenv import load_dotenv

load_dotenv()

# First create a Github instance:

# using an access token
g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))

# Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print(repo.name)

def get_users(num_users=50):
  idx, users = 0, []

  for user in g.search_users("location:Texas language:javascript followers:20..500"):
    users.append((user.name, user.email, user.followers, user.blog, user.hireable))
    idx += 1

    if idx == num_users:
      break
  
  return users
