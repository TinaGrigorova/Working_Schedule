import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
RANGE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(RANGE_CREDS)
SHEET = GSPREAD_CLIENT.open("working_schedule")


def get_schedule_data():
    """
    Get schedule data input from the entered data by the user in SHEET
    """
    print("Please enter the tasks/orders that need to be fulfilled in the following week.\n")
    print("NB! Data should be seven numbers, separated by commas.\n")
    print("Example : 10,13,23,13,22,11,9\n")
    
    numbers_str = input("Enter tasks/orders here: ")
    print(f'The tasks/orders provided are: {numbers_str}')


get_schedule_data()
