from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

def traer_datos():
    SCOPES = ['a']
    KEY = 'a'

    SPREADSHEET_ID = 'a'

    creds = None
    creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId = SPREADSHEET_ID, range = 'Hoja 1!A1:G').execute()
    values = result.get('values', [])

    for row in values:
        print(row)


