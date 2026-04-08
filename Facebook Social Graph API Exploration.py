# pip install requests

import requests

access_token = "Facebook_Access_Token"

url = "https://graph.facebook.com/me?access_token=" + access_token

response = requests.get(url)
data = response.json()

print("Name:", data["name"])
print("ID:", data["id"])
