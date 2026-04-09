# pip install google-api-python-client

import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def main():
    try:

        token_json_str = """
        {
          "token": "ya29.a0Aa7MYip5M_H9bQwToIztnrPTMklctL5FvLYQz8FO_p_EjLCoMzAbgXd7EYVICAs9_Ho9-2-c6yO4ZZovK9GBIIefEFG2xHhsQij_LDuRkvHs7sxrfIuMbSdazJnZvbmPsp-5_pFXn4An9wE286OilaWLmOtVNI1iWjTI46OiH9wzKYUBkLYv1eNlChW5rh89aTpYkXsaCgYKAV4SARUSFQHGX2MieVByLjyBRU5rGqausjHeOw0206",
          "refresh_token": "1//0grm9qRjwr5NOCgYIARAAGBASNwF-L9IrPa5I6RYi8RezzOqQSV9OHmsabgZQKSa_CHZJflhPyiTpkzFrt9Q_CzcExm_z71ev97A",
          "token_uri": "https://oauth2.googleapis.com/token",
          "client_id": "523101566913-tq6bjh1m0ovdrdujn729ooegnaq43mkk.apps.googleusercontent.com",
          "client_secret": "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",
          "scopes": ["https://www.googleapis.com/auth/drive.metadata.readonly"],
          "universe_domain": "googleapis.com",
          "account": "",
          "expiry": "2026-04-02T14:35:40Z"
        }
        """

        creds = Credentials.from_authorized_user_info(json.loads(token_json_str))

        service = build('drive', 'v3', credentials=creds)

        items = service.files().list(pageSize=10).execute().get('files', [])

        print("Files in your Google Drive:\n" if items else "No files found.")
        for i, f in enumerate(items, 1):
            print(f"{i}. {f['name']} (ID: {f['id']})")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
