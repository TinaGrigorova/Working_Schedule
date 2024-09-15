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
    Get the workload input from the user for each day of the week.
    Get schedule data input from the entered data by the user in SHEET
    """
    print("Please enter the tasks/orders that need to be fulfilled in the following week.\n")
    print("Add the workload for each day of the week using numbers only.")

    workload = {}
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    for day in days:
        while True:
            try:
                items = int(input(f"Enter the workload for {day}: "))
                workload[day] = items
                break
            except ValueError:
                print("Please enter a valid number.")
    
    return workload

get_schedule_data()
