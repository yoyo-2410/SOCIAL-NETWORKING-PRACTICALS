import requests
from requests_oauthlib import OAuth1

def get_authenticated_user(api_key, api_secret_key, access_token, access_token_secret):
    url = "https://api.twitter.com/2/users/me"

    auth = OAuth1(
        api_key,
        client_secret=api_secret_key,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret
    )

    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        user_data = response.json()
        print("User ID:", user_data["data"]["id"])
        print("Username:", user_data["data"]["username"])
    else:
        print("Error:", response.status_code)
        print(response.text)


# ===== Replace with your actual credentials =====
api_key = "YOUR_API_KEY"
api_secret_key = "YOUR_API_SECRET_KEY"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

get_authenticated_user(
    api_key,
    api_secret_key,
    access_token,
    access_token_secret
)
