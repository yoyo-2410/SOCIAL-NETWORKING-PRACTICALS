# pip install google-api-python-client

import json, random, string
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def get_name():
    return random.choice(["File", "Doc", "Report", "Data"]) + " " + str(random.randint(1, 100))

def get_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=20))

def fake_files(n=10):
    return [{"name": get_name(), "id": get_id()} for _ in range(n)]

def get_drive_files():
    try:
        token = """PASTE_YOUR_JSON_HERE"""
        creds = Credentials.from_authorized_user_info(json.loads(token))

        service = build('drive', 'v3', credentials=creds)
        items = service.files().list(pageSize=10).execute().get('files', [])

        if items:
            print("Google Drive Files:\n")
            return items
    except:
        print("API Failed → Using sample data\n")

    return fake_files()

files = get_drive_files()

for i, f in enumerate(files, 1):
    print(f"{i}. {f['name']} ({f['id']})")
