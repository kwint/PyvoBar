import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Barlijst").sheet1

print(sheet.row_count)
# Extract and print all of the values
list_of_names = sheet.col_values(1)
list_of_emails = sheet.col_values(2)
for i in range(2, len(list_of_names)):
    if list_of_names[i] == "":
        last_row = i
        max_names = i-2
        break

data = []
print(list_of_names[2:last_row])
print(max_names, last_row)
cell_list = sheet.range('D3:H' + str(last_row))
print(cell_list)

for cell in cell_list:
    cell.value = ''

sheet.update_cells(cell_list)
