import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mail
from prompter import yesno
import time
import numpy as np
import argparse


def getdata(sheet, data):
    last_row = sheet.row_count - 1

    data_rough = sheet.range(3, 1, last_row, last_column + 1) # +1 because G start counting at 1
    for cell in data_rough:
        data = np.append(data, cell.value)
    return data


def fillempty(row):
    for i in range(3, last_column):
        if row[i] == "":
            row[i] = "-"
    return row

# Input argmument parser
parser = argparse.ArgumentParser(description='Send barupdates')
# parser.add_argument('--dev', action='store_true')
# parser.add_argument('--prod', action='store_true')
parser.add_argument('version', choices=['dev', 'prod'], help='dev for testing, prod for the real thing')
args = parser.parse_args()

# Set Dev or Prod sheet
if args.version == 'dev':
    url = "https://docs.google.com/spreadsheets/d/12wdambiIM6ES9CMLf7pA_TdKFpMJYlzZGuD7sTpEZ9s/edit#gid=1865050320"  # dev
elif args.version == 'prod':
    url = "https://docs.google.com/spreadsheets/d/1bGjdq8_Qgxud0KFb-3lAM1_VwCivCXj5vhM8XeWuWyY/edit#gid=0"  # production
else:
    exit(1337)

# Set some const values
new_balance_column = 9
last_column = new_balance_column
# Set some not const variables
data = np.empty((0))

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the right sheet
spreadsheet = client.open_by_url(url)
repeat = True
while repeat:
    result = input("Kies groep (1 = pivos 2 = leiding 3 = explorers 4 = alles): ")
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

    if repeat == True:
        print("Vul een getal tussen de 1 en de 4 in. Heb je misschien een spatie toegevoegd?")

# reshape data array so it workable and readable, then print it so user can check some values
data = np.reshape(data, (-1, 10))
print(data)

# Send e-mails after conformation form the user
if yesno("Send e-mails? Make sure printed data above is correct! "):
    service = mail.init() # email init, login etc

    for i in range(0, len(data)):
        print(data[i][0])
        if data[i][new_balance_column] != "€ 0.00": # send e-mail if balance is not equal to 0
            print("lets mail")
            mail.main(service, fillempty(data[i]))  # Function that handles mailing
            time.sleep(2) # otherwise gmail thinks Im spamming and won't send emails
        else:
            print("Didn't send email to user since balance is 0")

