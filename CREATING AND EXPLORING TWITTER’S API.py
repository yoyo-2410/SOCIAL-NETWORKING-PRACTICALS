# pip install requests requests-oauthlib

import requests
from requests_oauthlib import OAuth1

def get_user(k, ks, t, ts):
    r = requests.get(
        "https://api.twitter.com/2/users/me",
        auth=OAuth1(k, ks, t, ts)
    )
    if r.status_code == 200:
        d = r.json()["data"]
        print("User ID:", d["id"])
        print("Username:", d["username"])
    else:
        print("Error:", r.status_code, r.text)

api_key = "YOUR_API_KEY"
api_secret_key = "YOUR_API_SECRET_KEY"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

get_user(api_key, api_secret_key, access_token, access_token_secret)
