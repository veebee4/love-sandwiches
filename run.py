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

# commented out below as this was just to check that the API was working
# access data in sales tab of love_sandwiches spreadsheet
# sales = SHEET.worksheet('sales')
# variable using gspread method to pull all the values from the sales sheet
# data = sales.get_all_values()
# print(data)

def get_sales_data():
    """
    Get sales figures input from the user
    """
    #while loop that asks user for data 
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")  # asks for data input from user here

        sales_data = data_str.split(",") #converts data from user into a list of values

        if validate_data(sales_data):
            print("Data is valid!")
            break
    return sales_data


def validate_data(values): #function that checks for errors in inputted values, if none, it returns true and returns string inside above if statement
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    print(values)
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
                )
    except ValueError as e: #if validate_data function encounters an error, the below code is run, returns false and the while loop will run again 
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

data = get_sales_data()

