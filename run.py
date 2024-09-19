# Import gspread and credentials 
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

def get_week_number():
    """
    Prompt the user to input the week number.
    """
    while True:
        try:

            week_number = int(input("Please enter the week number (1-52): "))
            
            if 1 <= week_number <= 52:
                return week_number
            else:
                print("Invalid input. Please enter a number between 1 and 52.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

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

def extract_staff_schedule(Schedule):
    """
    Extract staff availability from the specified tab in Google Sheets.
    Each day will have a list of available staff members.
    """
    try:
        # Open the tab where the staff schedule is stored
        schedule_sheet = SHEET.worksheet(Schedule)
        
        # Get all the data from the sheet
        schedule_data = schedule_sheet.get_all_values()
        
        # Extract the staff schedule based on the headers (first row)
        days = schedule_data[0]
        staff_schedule = {day: [] for day in days}
        
        # Fill in the staff availability for each day
        for row in schedule_data[1:]:
            for idx, staff in enumerate(row):
                if staff != 'off':  # Skip staff that are marked as 'off'
                    staff_schedule[days[idx]].append(staff)
        
        return staff_schedule
    
    except Exception as e:
        print(f"Error extracting staff schedule: {e}")
        return {}

def calculate_needed_staff(workload, staff_schedule):
    """
    Calculates the needed staff for each day in the week, based on the workload.
    One person can cover only 5 tasks/orders per day.
    """
    needed_staff = {}
    for day, items in workload.items():
        staff_required = items // 5
        if items % 5 != 0:
            staff_required += 1
        
        available_staff = len(staff_schedule.get(day, []))  # Use .get() to avoid KeyError (added due to an error)
        needed_staff[day] = min(staff_required, available_staff)
    
    return needed_staff


def update_week_days_sheet(WeekDays, week_number, data):
    """
    Update WeekDays work sheet with the required staff needed for each day of the week.
    Save the data without deleting the previous data.
    """
    worksheet = SHEET.worksheet(WeekDays)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    row = [data[day] for day in days] + [f"Week {week_number}"]
    
    worksheet.append_row(row)
    

def update_google_sheet(workload_data, week_number):
    """
    Update the 'workload' sheet in Google Sheets by appending the new workload data for the specified week.
    """
    try:
        # Open the 'Workload' sheet
        workload_sheet = SHEET.worksheet("Workload")
        
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        row =  [workload_data[day] for day in days] + [f"Week {week_number}"]
    
        workload_sheet.append_row(row)
        
        print(f"Workload for week {week_number} updated successfully in Google Sheets.\n")
    
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function - run all program functions.
    """
    week_number = get_week_number()
    
    staff_schedule = extract_staff_schedule("Schedule")

    if not staff_schedule:
        print("Error: Unable to extract staff schedule. Please check the spreadsheet.")
        return
    
    data = get_schedule_data()
    update_google_sheet(data, week_number)
    needed_staff = calculate_needed_staff(data, staff_schedule)
    print(f"Staff required per day for week {week_number}:", needed_staff)
    update_week_days_sheet("WeekDays", week_number, needed_staff)

main()
