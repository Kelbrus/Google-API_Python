from pprint import pprint

from googleapiclient import discovery
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'google-sheets/creds.json'
spreadsheet_id = '1CGeheshhAEouueVmedKlTsUcvq0Nkgy6nUfC5T_I0sk'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive']
)
httpAuth = credentials.authorize(httplib2.Http())
service = discovery.build('sheets', 'v4', credentials=credentials)

""" 
#Просмотр значений в заданном диапазоне:
values = service.spreadsheets().values().get(
    spreadsheetId = spreadsheet_id,
    range = 'A1:F20', 
    majorDimension = 'ROWS'
).execute()
pprint(values)
exit()
"""


#Вставка/изменение данных
values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "A5:F5",
             "majorDimension": "COLUMNS",
             "values": [["4"], ["Федоров"], ["Федор"], ["Федорович"], ["21.12.1974"], ["Технолог"]]}]}
).execute()


"""
#Удаление данных
values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "A4:F4",
             "majorDimension": "COLUMNS",
             "values": [[""], [""], [""], [""], [""], [""]]}]}
).execute()
"""