# Python Terminal Task Manager

## About the Project
In this Python programming task, I was asked to develop a fully functional Task Manager that works in the terminal. Apart from developing the application, the aim was to apply various Python programming concepts.
Some of the requirements involved adding, viewing, editing, deleting and searching tasks, where each task would have its ID, name, status, and deadline. In addition to this, file handling, use of JSON, input validation and error handling were necessary.
As I worked on the project, I was keen on understanding how various Python programming concepts interact in the development of an application. I also included task deadline reminders and task statistics as extra features.

## Features
- **Add Tasks:** Adds tasks by specifying the name and deadline of a particular task.
- **View Tasks:** Lists all saved tasks with their deadlines and statuses.
- **Edit Tasks:** To change name, deadline or status of a task.
- **Delete Tasks:** To delete tasks using unique IDs.
- **Search Tasks**: To search for tasks using keywords from the name of tasks.
- **Reminder for Deadline**: Look for incomplete tasks that have deadlines tomorrow or today.
- **Task Statistics**: To get information about the total number of tasks, completed tasks, incomplete tasks, overdue tasks and upcoming tasks.
- **Status of Tasks**: Determine whether tasks are completed, overdue, upcoming and pending according to their status and deadline.
- **Save Data as JSON File**: Save data into a JSON file and retrieve it back when the program runs.
- **Exception Handling and Input Validation**: Handle errors for incorrect inputs, deadlines, missing tasks and reading data from the saved files.

## Python Concepts Used
While completing this task, I used the following concepts in Python:
- Variables, inputs, and outputs
- Conditions and loops
- Lists, tuples, dictionaries, and sets
- String manipulations
- Functions, arguments, and returns
- Searching and filtering
- Files and JSON
- Exception handling with `try` and `except` constructs
- Working with date and time using `datetime` library
- Working with files and folders using `os`
- Counting tasks using `collections.Counter`
It allowed me to work with the above technologies altogether within one application and not just in separate exercises.

## Technologies Used
- Python 3
- JSON format to store the data of the tasks
- Python standard libraries: `json`(to store tasks even when the device is shut down), `os`(to access files), `datetime`(for deadlines) and `collections`(for counting)

## Project Structure
- `task_manager.py` - contains the program code and all functions needed to manage tasks
- `tasks.json` - contains the information about the tasks so that the information will be accessible between multiple launches of the program
- `README.md` - provides information on how to run the program and what it does

## How to run
1. Have Python 3 installed
2. Open a terminal in the folder where the project is located
3. Run the following command:
   ```bash
   python3 task_manager.py
   ```
4. Choose an option and follow instructions.
The `tasks.json` file should be located in the same folder as the program. In case the file is not found, the program will start without any previous tasks.

## Task Status Calculation Rules
Based on the completion of the task and its deadline I determined the status of the task:
- **Completed:** The task is marked as completed.
- **Overdue:** The deadline is over and the task remains incomplete.
- **Upcoming:** The task remains incomplete but its deadline lies within the coming seven days.
- **Pending:** The task is incomplete and its deadline lies more than seven days ahead.

## Additional Features
Apart from the needed task management operations, there are two extra features that have been developed:
1. **Reminders for Deadlines:** Shows all incomplete tasks with the deadline of today or tomorrow.
2. **Statistics on Tasks:** Presents statistics on tasks and their deadline types using the Python `Counter` library and date functions.

## Challenges Faced

### 'No tasks available' Problem
One issue I faced while testing the project was that the program displayed "No tasks available" even though `tasks.json` already contained saved tasks. Initially, I thought there was a problem with the JSON data, but I later realised that the program was looking for the file in the current working directory instead of the folder containing my Python script.
I fixed this by using `os.path.abspath(__file__)` and `os.path.dirname()` to get the directory of `task_manager.py`, and `os.path.join()` to build the correct path to `tasks.json`. This allowed the program to locate the data file correctly, even when I ran it from a different directory.
This helped me understand the difference between a script's location and the current working directory, and why handling file paths correctly is important when working with file storage.

### Handling Invalid and Corrupted Data
Another challenge was making sure the program handled invalid inputs and unexpected data properly. For example, users could enter an invalid deadline, a non-numeric Task ID or try to update a task that did not exist. I added input validation and exception handling to display appropriate error messages instead of allowing these inputs to crash the program. I also added checks when loading the JSON file to detect corrupted or incorrectly structured task data.

### Calculating Task Status and Statistics
I also had to make sure tasks were classified correctly based on their deadlines. A task with a past deadline should be marked as overdue only if it has not been completed, while tasks due within the next seven days should be considered upcoming. I used Python's `datetime` module to compare dates and implemented separate logic for calculating task statistics. Testing these cases helped me understand how to handle date comparisons and avoid counting a task in the wrong category.

## What I Learned
From this particular task, I have gained experience in structuring a Python program using functions, JSON files, validating user input, exception handling and using dates in order to monitor deadlines. Besides, I have learned to take into account various possibilities regarding user input and files rather than concentrating only on the program’s standard execution.
Further improvements can be made in terms of adding such features as priorities of tasks, sorting by deadlines and other. All in all, this project became another opportunity to apply Python skills acquired in this task.



