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
    Get the week number from the user.
    """
    while True:
        try:
            week = int(input("Enter the week number: "))
            return f"Week {week}"  # Return formatted week number
        except ValueError:
            print("Please enter a valid week number.")

def get_schedule_data():
    """
    Get the workload input from the user for each day of the week.
    """
    print("Please enter the tasks/orders that need to be fulfilled for the week.\n")
    print("Add the workload for each day of the week using numbers only (between 0 and 80).")

    workload = {}
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    for day in days:
        while True:
            try:
                items = int(input(f"Enter the workload for {day}: "))
                if 0 <= items <= 80:
                    workload[day] = items
                    break
                else:
                    print("Please enter a number between 0 and 80.")
            except ValueError:
                print("Please enter a valid number.")
    
    return workload

def extract_staff_schedule():
    """
    Extract staff availability from the 'Schedule' tab in Google Sheets.
    Each day will have a list of available staff members.
    """
    try:
        # Open the tab where the staff schedule is stored
        schedule_sheet = SHEET.worksheet("Schedule")
        
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
    needed_staff_schedule = {}
    
    for day, items in workload.items():
        staff_required = items // 5
        if items % 5 != 0:
            staff_required += 1
        
        available_staff = staff_schedule.get(day, [])
        assigned_staff = available_staff[:staff_required]  # Assign only the required number of staff
        needed_staff_schedule[day] = assigned_staff
    
    return needed_staff_schedule

def update_week_schedule(week_number, needed_staff_schedule):
    """
    Update the Week Schedule sheet in Google Sheets with the required staff per day.
    """
    try:
        # Create or open a new worksheet for the week schedule
        sheet_name = f"{week_number} Schedule"
        try:
            worksheet = SHEET.worksheet(sheet_name)
            worksheet.clear()
        except gspread.exceptions.WorksheetNotFound:
            worksheet = SHEET.add_worksheet(title=sheet_name, rows="100", cols="20")
        
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        rows = [days]  # Start with the header row (days of the week)
        
        # Find the maximum number of staff needed for any day to format the rows properly
        max_staff_needed = max(len(staff) for staff in needed_staff_schedule.values())
        
        # Add the staff members for each day into the respective row
        for i in range(max_staff_needed):
            row = []
            for day in days:
                if i < len(needed_staff_schedule[day]):
                    row.append(needed_staff_schedule[day][i])
                else:
                    row.append("off")  # If no more staff are needed, mark "off"
            rows.append(row)
        
        # Append the data to the worksheet
        worksheet.append_rows(rows)
        print(f"Staff schedule for {week_number} has been updated in the Google Sheet.\n")
    
    except Exception as e:
        print(f"An error occurred while updating the sheet: {e}")

def update_google_sheet(workload_data, week_number):
    """
    Update the 'Workload' sheet in Google Sheets with the provided workload data.
    The data is added as rows with each day as a column heading and week number appended.
    """
    try:
        workload_sheet = SHEET.worksheet("Workload")
       
        headers = list(workload_data.keys())
        
        workload_values = list(workload_data.values()) + [week_number]  # Add the week number at the end
        
        if workload_sheet.row_count == 0:
            workload_sheet.append_row(headers + ["Week Number"])
        
        workload_sheet.append_row(workload_values)
        
        print("Workload updated successfully in Google Sheets.\n")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def update_week_days_sheet(needed_staff_schedule, week_number):
    """
    Update WeekDays worksheet with the required staff needed for each day of the week.
    """
    try:
        worksheet = SHEET.worksheet("WeekDays")
        
     
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        rows = [days] 
        staff_count = [len(needed_staff_schedule[day]) for day in days]  # Count of needed staff per day
        
        if worksheet.row_count == 0:
            worksheet.append_row(days + ["Week Number"])
        
        worksheet.append_row(staff_count + [week_number])
        
        print("WeekDays sheet updated successfully in Google Sheets.\n")
    
    except Exception as e:
        print(f"An error occurred while updating the WeekDays sheet: {e}")

def main():
    """
    Main function - run all program functions.
    """
    week_number = get_week_number()
    staff_schedule = extract_staff_schedule()

    if not staff_schedule:
        print("Error: Unable to extract staff schedule. Please check the spreadsheet.")
        return
    
    workload = get_schedule_data()
    update_google_sheet(workload, week_number)
    needed_staff_schedule = calculate_needed_staff(workload, staff_schedule)
    print("Staff required per day:", needed_staff_schedule)
    update_week_days_sheet(needed_staff_schedule, week_number)
    update_week_schedule(week_number, needed_staff_schedule)

main()
