#Import gspread and credentials 
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

def calculate_needed_staff(workload):
    """
    Calculates the needed staff for each day in the week, based on the workload.
    One person can cover only 5 tasks/orders per day.
    """
    needed_staff = {}
    for day,  items in workload.items():
        staff = items // 5
        if items % 5 != 0:
            staff += 1
            needed_staff[day] = staff

    return needed_staff
    


def update_google_sheet(workload_data):
    """
    Update the 'workload' sheet in Google Sheets with the provided workload data.
    The data is added as rows with each day as a column heading.
    """
    try:
        # Open the 'workload' sheet
        workload_sheet = SHEET.worksheet("Workload")
        
        # Create the row with headers
        headers = list(workload_data.keys())
        
        # Create the row with the corresponding workload numbers
        workload_values = list(workload_data.values())
        
        # Clear the sheet before updating
        workload_sheet.clear()
        
        # Append headers and workload values as rows
        workload_sheet.append_row(headers)         
        workload_sheet.append_row(workload_values) 
        
        print("Workload updated successfully in Google Sheets.\n")
    
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function - run all program functions.
    """
    data = get_schedule_data()
    update_google_sheet(data)
    needed_staff = calculate_needed_staff(data)
    print("Staff required per day:", needed_staff)

main()