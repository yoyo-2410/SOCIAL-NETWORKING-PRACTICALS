# pip install requests

import requests

def get_user(u):
    r = requests.get(f"https://api.github.com/users/{u}")
    if r.status_code == 200:
        d = r.json()
        print("\nUSER DETAILS")
        print("Name:", d.get("name"))
        print("Username:", d.get("login"))
        print("Followers:", d.get("followers"))
        print("Following:", d.get("following"))
        print("Public Repos:", d.get("public_repos"))
    elif r.status_code == 404:
        print("User not found.")
    else:
        print("Error:", r.status_code)

def get_repos(u):
    r = requests.get(f"https://api.github.com/users/{u}/repos")
    if r.status_code == 200:
        print("\nREPOSITORIES:")
        for repo in r.json()[:5]:
            print(f"- {repo['name']}  {repo['stargazers_count']}")
    else:
        print("Error fetching repos:", r.status_code)

u = input("Enter GitHub username: ")
get_user(u)
get_repos(u)
