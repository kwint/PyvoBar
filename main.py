import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mail
from prompter import yesno
import time


def getdata(sheet, data):
    # Finds the last row with data
    list_of_names = sheet.col_values(1)
    list_of_emails = sheet.col_values(2)
    for i in range(2, len(list_of_names)):
        if list_of_names[i] == "":
            last_row = i  # Google drive starts counting with 1...
            break

    # Print al the names found in sheet
    print("Found data for:\n", list_of_names[2:last_row])
    print("Processing data, this could take some time")

    # Getting balance and mailadresses from sheet, put them in array with name found earlier
    for current_row in range(3, last_row + 1):
        # print("currentrow", current_row)
        balance_new = sheet.cell(current_row, 10).value
        data.append([list_of_names[current_row - 1], list_of_emails[current_row - 1], balance_new])
    return data

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
filename = "Barlijst"
data = []  # this array gets filled with mail data

# Find a workbook by name and open the right sheet
spreadsheet = client.open(filename)
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


# Send e-mails after conformation form the user
print(data)
# print(type(data), data[len(data)-1], data[22])
# print(len(data))
# print(max)
if yesno("Send e-mails? Make sure printed data above is correct!"):
    for i in range(0, len(data)):
        print("naam:", data[i][0])
        print("data i 2:", data[i][2])
        if data[i][2] != "€ 0.00":
            print("lets mail")
            mail.main(data[i][0], data[i][1], data[i][2])  # Function that handles mailing
        else:
            print("Didn't send email to user since balance is 0")
        time.sleep(2)
