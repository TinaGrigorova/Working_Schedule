# Working Schedule

Working Schedule is a simple and efficient way to manage weekly staff schedules based on workload and availability. The program collects workload data from users, calculates the necessary staff needed for each day, and updates multiple Google Sheets to reflect this information.

It handles inputs for each day of the week, checks staff availability, and provides a clear output of the required staffing. Additionally, it organizes data in an easily referenceable format, automating the generation of weekly working schedules based on team capacity and workload distribution.

Integrating with Google Sheets allows for real-time updates, ensuring the schedule reflects the latest staff availability and task requirements. Each team member can manage 5 tasks per day, enabling the system to calculate and assign the appropriate number of staff per day. It also generates a random schedule based on the provided information.


---- ! LINK TO LIVE PROJECT ! ----
---
## Logic flowchart

![Flowchart](assets/images/logic-flowchart.png)

* The flowchart demonstrates the flow of data and decision-making in the program. It starts with the input of daily workloads and ends with the generated schedule being updated in Google Sheets.
---
## Features

* Automated Weekly Schedule Generation: Automatically calculates the number of staff required per day based on workload and assigns staff to tasks.
* Google Sheets Integration: The schedule is updated in a Google Sheet for easy access and real-time collaboration.
* Customizable Workload Inputs: Easily input workload data, and the system will adjust the staffing requirements accordingly.
* Dynamic Updates: The schedule adjusts automatically if there are changes in workload or staff availability.
* Week Number Tracker: Automatically appends the week number to each data row for better tracking.

### Existing Features

* Intro screen
 ** (Img main screen)
* Adding week number
 ** (img adding wk nr)
* Reuesting data for each day if the week 
 ** (img when data is requested)
* Correct input
 ** (img when input is correct)
* Incorrect input 
 ** (img when input is incorrcet)
* Print the calculated data
 ** (img of data printed in app)
* Updates Google Sheets wirth correct data 
 ** (img of google sheet after update)
* Generates working schedule based on availability and calculated data 
 ** (img of examp schedule)

### Features Left to Implement 

* Data to be deleted with request by the user in the app instead of manually by the user
* More staff to be added so more worlkoad can be done 
* Option to choose the amount of tasks that can be done by one individule. 

---
# Technologies Used

* Python: The primary programming language used for logic and automation.
* Google Sheets API: For seamless integration and updating of the schedule in Google Sheets.
* gspread: Python library used to interact with Google Sheets.
* OAuth2: Used for authentication with Google Sheets.
---
## Fixed Bugs
* The program run twice as one func has been called twice , once in main and once at the end of the program, which was fixed by removing the get_schedule_data() func called after main()
* KeyErorr was present due to incorrect header spelling in spreadsheet and the data could not be extracte. Fixed by correcting the misspelled data. 
* Was not updating spreadsheet with the required information, fixed by placing needed_staff[day] = staff outside the "if" block to ensure calculated staff count is correctly assigned to the needed_staff dictionary for all cases.
 
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