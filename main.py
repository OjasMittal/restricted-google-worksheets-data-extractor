import gspread

gc = gspread.service_account('key.json')

spreadsheet = gc.open('python google spreadsheets')

# Get a worksheet by index
# worksheet1 = spreadsheet.get_worksheet(0)

# Get a worksheet by name 
worksheet1 = spreadsheet.worksheet('2013')

data = worksheet1.get_all_records()
print(data)