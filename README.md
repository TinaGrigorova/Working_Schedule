# Working Schedule

Working Schedule is a simple and efficient way to manage weekly staff schedules based on workload and availability. The program collects workload data from users, calculates the necessary staff needed for each day, and updates multiple Google Sheets to reflect this information.

It handles inputs for each day of the week, checks staff availability, and provides a clear output of the required staffing. Additionally, it organizes data in an easily referenceable format, automating the generation of weekly working schedules based on team capacity and workload distribution.

Integrating with Google Sheets allows for real-time updates, ensuring the schedule reflects the latest staff availability and task requirements. Each team member can manage 5 tasks per day, enabling the system to calculate and assign the appropriate number of staff per day. It also generates a random schedule based on the provided information.


---- ! LINK TO LIVE PROJECT ! ----
---
## Logic flowchart

![Flowchart](assets/images/logic-flowchart.png)

The flowchart demonstrates the flow of data and decision-making in the program. It starts with the input of daily workloads and ends with the generated schedule being updated in Google Sheets.
---
## Features

* Automated Weekly Schedule Generation: Automatically calculates the number of staff required per day based on workload and assigns staff to tasks.
* Google Sheets Integration: The schedule is updated in a Google Sheet for easy access and real-time collaboration.
* Customizable Workload Inputs: Easily input workload data, and the system will adjust the staffing requirements accordingly.
* Dynamic Updates: The schedule adjusts automatically if there are changes in workload or staff availability.
* Week Number Tracker: Automatically appends the week number to each data row for better tracking.
---
# Technologies Used

* Python: The primary programming language used for logic and automation.
* Google Sheets API: For seamless integration and updating of the schedule in Google Sheets.
* gspread: Python library used to interact with Google Sheets.
* OAuth2: Used for authentication with Google Sheets.