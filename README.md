# Working Schedule

Working Schedule is a simple and efficient way to manage weekly staff schedules based on workload and availability. The program collects workload data from users, calculates the necessary staff needed for each day, and updates multiple Google Sheets to reflect this information.

It handles inputs for each day of the week, checks staff availability, and provides a clear output of the required staffing. Additionally, it organizes data in an easily referenceable format, automating the generation of weekly working schedules based on team capacity and workload distribution.

Integrating with Google Sheets allows for real-time updates, ensuring the schedule reflects the latest staff availability and task requirements. Each team member can manage 5 tasks per day, enabling the system to calculate and assign the appropriate number of staff per day. It also generates a random schedule based on the provided information.

|  [Link to Working Schedule](https://working-schedule-31944893274f.herokuapp.com/)  ||  [Link to Google Spreadsheet](https://docs.google.com/spreadsheets/d/1RRbKmPenlRBxszcVJnW8DRHCUvOWhqTXxy8NBV6grUc/edit?gid=1975512601#gid=1975512601)  |

---
## Logic flowchart

![Flowchart](assets/images/logic_flowchart.png)

* The flowchart demonstrates the flow of data and decision-making in the program. It starts with the input of daily workloads and ends with the generated schedule being updated in Google Sheets.
---

## User Experience (UX)

The Working Schedule system is designed to provide a seamless, efficient experience for users responsible for managing staffing schedules. The interface allows users to input workload data, see the required staff members for the week, and ensure that the schedule is balanced based on staff availability. The output is automatically updated into Google Sheets, making it easy to review and adjust staffing plans on the fly.

### Key aspects of the user experience:

* Simplicity
  * The system minimizes manual effort by calculating the necessary staff based on workload inputs and predefined rules, such as staff availability.
* Automation
  * Users benefit from automated Google Sheets integration, which ensures that schedules are saved, accessible, and shareable across the organization.
* Error Handling
  * If the workload exceeds the available staff, the program provides feedback, prompting the user to make necessary adjustments.
* Efficiency
  * By using this system, users can focus more on operational management rather than manual schedule creation.

### User Stories

* First-time User Goals
  * Understand how the system works: The user should quickly understand how to input the workload data, and how the staff scheduling is calculated and updated into the Google Sheet.
  * Create their first schedule: Once the user understands the process, they should be able to input the weekly workload and generate a staff schedule without confusion.
  * Experience seamless integration: The first-time user should see how easy it is to update the schedule and view it in Google Sheets, helping them manage staff schedules efficiently.
* Returning User Goals
  * Continue scheduling efficiently: The returning user will likely want to input new workload data for future weeks and generate updated schedules without needing further guidance.
  * Adjust workload based on feedback: Returning users may refine their workload input based on previous feedback from the system, like insufficient staff, ensuring smoother operations.
  * Explore new features: Users might want to explore additional features such as saving historical data or generating reports for staff allocation over a month.
* Frequent User Goals
  * Optimize staff allocation: Frequent users may focus on optimizing staff usage, reducing over-scheduling, or ensuring that no team members are overworked.
  * Share the schedule with colleagues: Users who handle scheduling regularly will likely share the schedules with team members and supervisors, ensuring that everyone is aligned with the workload.
  * Save and analyze data: Frequent users may want to save weekly data to analyze trends, staff utilization rates, and workload distribution across multiple weeks to improve long-term planning.

## Features

* Automated Weekly Schedule Generation: Automatically calculates the number of staff required per day based on workload and assigns staff to tasks.
* Google Sheets Integration: The schedule is updated in a Google Sheet for easy access and real-time collaboration.
* Customizable Workload Inputs: Easily input workload data, and the system will adjust the staffing requirements accordingly.
* Dynamic Updates: The schedule adjusts automatically if there are changes in workload or staff availability.
* Week Number Tracker: Automatically appends the week number to each data row for better tracking.

### Existing Features

* Intro screen:

The app automates staff scheduling based on input workload and staff availability, storing the data in Google Sheets. It calculates the necessary number of staff for each day and updates the schedule, optimizing team management and reducing manual scheduling.

 <img src="assets/images/intro.png" alt="intro" width="500"/>

 
 
* Adding week number:

The user is prompted to input the week number (between 1 and 52) to generate the schedule for that specific week. This ensures that the schedule and workload data are tracked and stored for the correct time period.


 <img src="assets/images/correct_week_nr.png" alt="add_week_nr" width="500"/>

* Adding incorrect week number or not a number at all:

If the user enters invalid input (such as a week number outside the range of 1-52 or non-numeric values), the app will display an error message and prompt the user to enter the correct data again.

 <img src="assets/images/wrong_week_nr.png" alt="incorrect_week_nr" width="500"/>

* Reuesting data for each day of the week:

The app asks the user to input the workload for each day of the week (Monday to Sunday). The user is expected to provide the number of tasks that need to be completed each day.

 <img src="assets/images/weekdays_input_app.png" alt="weekdays_input" width="500"/>

 * Incorrect workload input:

If the user enters a workload value outside the acceptable range (0-80) or provides invalid input, an error message is displayed, and the user is asked to input the correct workload again.

 <img src="assets/images/wrong_workload_input.png" alt="wrong_workload_input" width="500"/>

* Correct workload input:

When the user inputs valid workload data (a number between 0 and 80 for each day), the app accepts the input and proceeds to calculate the required staff based on the given workload.

 <img src="assets/images/correct_input_calculation.png" alt="correct_input" width="500"/>

* If there are not enough people for the day/days:

If the app detects that there aren't enough staff members available to meet the required workload for a particular day, it displays an error message indicating the shortage of staff. The user is then prompted to adjust the workload accordingly.

 <img src="assets/images/not_enough_staff.png" alt="not_enough_staff" width="500"/>

* Updates Google Sheets with the input for workload:

 <img src="assets/images/workload_input_spreadsheet.png" alt="workload_update" width="500"/>

* Updates Google Sheets with the calculated staff needed for the week:

 <img src="assets/images/weekdays_input_spreadsheet.png" alt="weekdays_update" width="500"/>

* Generates working schedule based on availability and calculated data:

 <img src="assets/images/printed_schedule.png" alt="schedule" width="500"/>

### Features Left to Implement 

* Data to be deleted with request by the user in the app instead of manually by the user
* More staff to be added so more worlkoad can be done 
* Option to choose the amount of tasks that can be done by one individule. 

### Database

The data is stored in Google Sheets and the app accessit through Google Dribe and Google Sheets API.
The spreadsheet can be viewed [here](https://docs.google.com/spreadsheets/d/1RRbKmPenlRBxszcVJnW8DRHCUvOWhqTXxy8NBV6grUc/edit?gid=1975512601#gid=1975512601).

---
# Technologies Used

* Python: The primary programming language used for logic and automation.
* Google Sheets API: For seamless integration and updating of the schedule in Google Sheets.
* gspread: Python library used to interact with Google Sheets.
* OAuth2: Used for authentication with Google Sheets.

---
## Frameworks, Libraries & Programs Used

* [GitHub](https://github.com/)
    * To write the code.
* [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [LucidApp](https://lucid.app/)
    * To create a logic flowchart of the hangman game.
* [Heroku](https://www.heroku.com/)
    * To deploy the project.
* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * Check code for any issues.

---
## Testing

### Testing with CI Python Linter:

<img src="assets/images/testing_ci_liner.png" alt="testing_ci_liner" width="500"/>


### Manual Testing 


| Feature | Expected Result | Steps Taken | Actual Result | Screenshot |
| ------- | -------------- | ----------- | ------------- | ---------- |
| Intro Screen   | Displays the beginnig of the app | None | As Expected | <img src="assets/images/intro.png" alt="intro" width="300"/> |
| Request input for Week Number | Week Number to be entered correctly | Enter Week number (between 1 and 52) | As Expected | <img src="assets/images/correct_week_nr.png" alt="add_week_nr" width="300"/> |
| If incorrect Week Number has been entered | Request data again when wrong data is entered | Input wrong data | As Expected | <img src="assets/images/wrong_week_nr.png" alt="incorrect_week_nr" width="300"/> |
| Request input for Workload | Enter workload for each day of the week | Enter Workload for weach day of the week | As Expected | <img src="assets/images/weekdays_input_app.png" alt="weekdays_input" width="300"/> |
| If incorrect Workload has been entered | Request data again when wrong data is entered | Input wrong data | As Expected | <img src="assets/images/wrong_workload_input.png" alt="wrong_workload_input" width="300"/> |
| Entered data is correct | Display the entered data, calculate needed staff based on the workload input | Enter Data | As Expected | <img src="assets/images/correct_input_calculation.png" alt="correct_input" width="300"/> |
| If staff is not enough  | Print which days are with shortage of staff and request the worlkoad to be entered evenly in the choosen week | Enter more workload than what can be handled | As Expected | <img src="assets/images/not_enough_staff.png" alt="not_enough_staff" width="300"/> |
| Update Spreadsheet with input data | Update Google spreadsheet - "Workload" with entered data by the user | None | As Expected | <img src="assets/images/workload_input_spreadsheet.png" alt="workload_update" width="300"/> |
| Update Spreadsheet with calculated data by the input | Update Google spreadsheet - "WorkDays" based on calculated data | None | As Expected | <img src="assets/images/weekdays_input_spreadsheet.png" alt="weekdays_input" width="300"/> |
| Create Schedule for the choosen week | Create schedule for the choosen week, using the requred staff for each day , and printing in new tab random schedule based on given staff availability  | None | As Expected | <img src="assets/images/printed_schedule.png" alt="schedule" width="500"/> |

## Input validation testing

* Required week number 
    * Cannot continue with empty input
    * Week number must be entered

<img src="assets/images/week_validation.png" alt="week_validation" width="500"/> 

* Enter required workload
    * Cannot enter more than 80 and less then 0 workload 
    * Cannot continue with empty input

<img src="assets/images/workload_validation.png" alt="workload_validation" width="500"/> 

* Request data more evenly 
    * Cannot continue if there is not enough staff to cover the workload
  
<img src="assets/images/data_request_validation.png" alt="data_request_validation" width="500"/> 

---
## Fixed Bugs
* The program run twice as one func has been called twice , once in main and once at the end of the program, which was fixed by removing the get_schedule_data() func called after main()
* KeyErorr was present due to incorrect header spelling in spreadsheet and the data could not be extracte. Fixed by correcting the misspelled data. 
* Was not updating spreadsheet with the required information, fixed by placing needed_staff[day] = staff outside the "if" block to ensure calculated staff count is correctly assigned to the needed_staff dictionary for all cases.

---
## Deployment

### Deploying to Heroku

To deploy with Heroku, Code Institute Python Essentials Template was used so the python code can be viewed in a terminal in a browser
1. Log in to Heroku or create a new account
2. On the main page click "New" and select "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. On the next page find "settings" and locate "Config Vars"
6. Click "Reveal Config Vars" and add "PORT" key and value "8000", click "Add"
7. Scroll down, locate "Buildpack" and click "Add", select "Python"
8. Repeat step 7. only this time add "Node.js", make sure "Python" is first
9. Scroll to the top and select "Deploy" tab
10. Select GitHub as deployment method and search for your repository and link them together
11. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
12. [Deployed site](https://working-schedule-31944893274f.herokuapp.com/)

### Forking the GitHub Repository

By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate [GitHub Repository Working Schedule](https://github.com/TinaGrigorova)
2. At the top of the Repository(under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.

### Local Clone

1. Log in to GitHub and locate [GitHub Repository Working Schedule](https://github.com/TinaGrigorova)
2. Under the repository name click "Clone or download"
3. Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste The URL copied in the step 3.
7. Press Enter and your local clone will be created.

## Credits


### Code

- **Python Understanding**: through code institute lessons.
- **Google Sheets API Documentation**: I referred to the official documentation for interacting with Google Sheets and understanding the gspread library. Check it out [here](https://developers.google.com/sheets/api).
- **gspread and gspread-formatting Documentation**: Used for handling spreadsheet operations and formatting in Google Sheets. See the documentation [here](https://gspread.readthedocs.io/).
- **Stack Overflow**: Various discussions and solutions provided invaluable insights into error handling and code optimization. [Stack Overflow](https://stackoverflow.com/).
- **MDN Web Docs**: Referred to for understanding web technologies like OAuth and request handling. Check it out [here](https://developer.mozilla.org/en-US/).


### Content

* All content was written by the developer.

## Acknowledgements

 * My mentor Mitko Bachvarov provided helpful feedback.
 * Slack community for encouragement.