import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mail
from prompter import yesno
import time
import numpy as np


def getdata(sheet, data):
    last_row = sheet.row_count - 1

    data_rough = sheet.range(3, 1, last_row, 9)
    for cell in data_rough:
        data = np.append(data, cell.value)
    return data


def fillempty(row):
    for i in range(3, 8):
        if row[i] == "":
            row[i] = "-"
    return row

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
url = "https://docs.google.com/spreadsheets/d/1j8LReHcC1wH9oi7KrfvPQmfok31h7aNo8d6glpDI9oM/edit#gid=0"
data = np.empty((0))

# Find a workbook by name and open the right sheet
spreadsheet = client.open_by_url(url)
repeat = True
while repeat:
    result = input("Kies groep (1 = pivos 2 = leiding 3 = explorers 4 = alles)")
    if result == "1" or result == "4":
        sheet = spreadsheet.get_worksheet(0)
        data = getdata(sheet, data)
        repeat = False
    if result == "2" or result == "4":
        sheet = spreadsheet.get_worksheet(1)
        data = getdata(sheet, data)
        repeat = False
    if result == "3" or result == "4":
        sheet = spreadsheet.get_worksheet(2)
        data = getdata(sheet, data)
        repeat = False

data = np.reshape(data, (-1, 9))
# Send e-mails after conformation form the user
print(data)


if yesno("Send e-mails? Make sure printed data above is correct! "):
    service = mail.init()

    for i in range(0, len(data)):
        print(data[i][0])
        if data[i][8] != "€ 0.00":
            print("lets mail")
            mail.main(service, fillempty(data[i]))  # Function that handles mailing
        else:
            print("Didn't send email to user since balance is 0")
        time.sleep(2)
