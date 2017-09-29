import gspread
from oauth2client.service_account import ServiceAccountCredentials

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mail
from prompter import yesno
import time


def newtoold(sheet):
    list_of_names = sheet.col_values(1)
    newSaldo = sheet.range("J3:J" + str(len(list_of_names)))
    oldSaldo = sheet.range("C3:C" + str(len(list_of_names)))

    row = 0
    for cell in oldSaldo:
        cell.value = newSaldo[row].value
        row += 1

    sheet.update_cells(oldSaldo)

    cell_list = sheet.range('D3:G' + str(len(list_of_names)))
    for cell in cell_list:
        cell.value = ''

    sheet.update_cells(cell_list)

    cell_list = sheet.range('I3:I' + str(len(list_of_names)))
    for cell in cell_list:
        cell.value = ''

    sheet.update_cells(cell_list)


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
filename = "Barlijst"

spreadsheet = client.open(filename)

repeat = True
while repeat:
    result = input("Kies groep (1 = pivos 2 = leiding 3 = explorers 4 = alles)")
    if result == "1" or result == "4":
        sheet = spreadsheet.get_worksheet(0)
        newtoold(sheet)
        repeat = False
    if result == "2" or result == "4":
        sheet = spreadsheet.get_worksheet(1)
        newtoold(sheet)
        repeat = False
    if result == "3" or result == "4":
        sheet = spreadsheet.get_worksheet(2)
        newtoold(sheet)
        repeat = False


# clear sheet

