# pip install requests

import requests

r = requests.get(
    "https://api.linkedin.com/v2/me",
    headers={"Authorization": "Bearer ACCESS_TOKEN"})

print("User Profile Data:" if r.status_code == 200 else "Error:", 
      r.json() if r.status_code == 200 else r.text)
