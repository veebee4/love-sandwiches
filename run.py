# imports whole of gspread library
import gspread
# imports Credentials class
from google.oauth2.service_account import Credentials

# below is a constant
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# another constant variable
CREDS = Credentials.from_service_account_file('creds.json')
# new constant variables for scope and gspread
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# below variable to access our love_sandwiches spreadsheet / sheet variable defined
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# access data in sales tab of love_sandwiches spreadsheet
sales = SHEET.worksheet('sales')

# variable using gspread method to pull all the values from the sales sheet
data = sales.get_all_values()

print(data)