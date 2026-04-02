# pip install requests

import requests

# Paste your access token here
access_token = "Facebook_Access_Token"

# Get basic profile data
url = "https://graph.facebook.com/me?access_token=" + access_token

response = requests.get(url)
data = response.json()

# Print output
print("Name:", data["name"])
print("ID:", data["id"])
