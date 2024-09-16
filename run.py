import gspread
from google.oauth2.service_account import Credentials

# Google API Scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Authenticate and Connect to Google Sheets
CREDS = Credentials.from_service_account_file('creds.json')
RANGE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(RANGE_CREDS)
SHEET = GSPREAD_CLIENT.open("working_schedule")

def get_schedule_data():
    """
    Get the workload input from the user for each day of the week.
    """
    print("Please enter the tasks/orders that need to be fulfilled for the week.\n")
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

def update_google_sheet(workload_data):
    """
    Update the 'workload' sheet in Google Sheets with the provided workload data.
    """
    try:
        # Open the 'workload' sheet
        workload_sheet = SHEET.worksheet("Workload")
        
        # Convert the dictionary to a list of lists for insertion into the sheet
        row = [["Day", "Workload"]]  # Add headers
        for day, items in workload_data.items():
            row.append([day, items])
    
        
        # Update the sheet with new data
        workload_sheet.append_rows(row)
        print("Workload updated successfully in Google Sheets.")
    
    except Exception as e:
        print(f"An error occurred: {e}")




