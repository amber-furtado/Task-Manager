import json
import os
from datetime import datetime, date, timedelta
from collections import Counter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "tasks.json")

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)

        if not isinstance(tasks, list):
            raise ValueError("Task data must be a list.")

        task_ids = set()

        for task in tasks:
            if not isinstance(task, dict):
                raise ValueError("Invalid task entry.")

            if not all(key in task for key in ("id", "name", "status", "deadline")):
                raise ValueError("A task is missing required fields.")

            if type(task["id"]) != int or task["id"] < 1:
                raise ValueError("Invalid task ID.")

            if task["id"] in task_ids:
                raise ValueError("Duplicate task ID.")

            task_ids.add(task["id"])

            if not isinstance(task["name"], str) or not task["name"].strip():
                raise ValueError("Invalid task name.")

            if task["status"] not in ("Pending", "Completed"):
                raise ValueError("Invalid task status.")

            datetime.strptime(task["deadline"], "%Y-%m-%d")

        return tasks

    except (json.JSONDecodeError, ValueError, TypeError,
            KeyError, OSError) as error:
        print("Error loading tasks:", error)
        print("Please check tasks.json before continuing.")
        return None


def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)

    except OSError:
        print("Error: Could not save tasks to file.")
    


def add_task(tasks):
    # Get the task name
    name = input("Enter task name: ").strip()

    if name == "":
        print("Error: Task name cannot be empty.")
        return

    # Get and validate the deadline
    deadline = input("Enter deadline (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(deadline, "%Y-%m-%d")

    except ValueError:
        print("Error: Invalid deadline. Use YYYY-MM-DD.")
        return

    # Generate a unique task ID
    if len(tasks) == 0:
        task_id = 1
    else:
        task_id = max(task["id"] for task in tasks) + 1

    # Create the task dictionary
    task = {
        "id": task_id,
        "name": name,
        "status": "Pending",
        "deadline": deadline
    }

    # Add the task to the list
    tasks.append(task)

    # Save the updated list
    save_tasks(tasks)

    print("Task added successfully!")
    print("Task ID:", task_id)


def get_task_status(task):
    if task["status"] == "Completed":
        return "COMPLETED"

    deadline = datetime.strptime(
        task["deadline"], "%Y-%m-%d"
    ).date()

    today = date.today()

    if deadline < today:
        return "OVERDUE"

    elif deadline <= today + timedelta(days=7):
        return "UPCOMING"

    else:
        return "PENDING"


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\n========== YOUR TASKS ==========")

    for task in tasks:
        status = get_task_status(task)

        print("\nTask ID:", task["id"])
        print("Task Name:", task["name"])
        print("Deadline:", task["deadline"])
        print("Status:", status)

    print("\n================================")


def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def update_task(tasks):
    try:
        task_id = int(input("Enter Task ID to update: "))
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    task = find_task(tasks, task_id)

    if task is None:
        print("Error: Task not found.")
        return

    # Work on a copy until all inputs are validated
    updated_task = task.copy()

    print("Leave a field blank to keep its current value.")

    name = input(
        "New name [" + task["name"] + "]: "
    ).strip()

    if name != "":
        updated_task["name"] = name

    deadline = input(
        "New deadline [" + task["deadline"] + "]: "
    ).strip()

    if deadline != "":
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid deadline. No changes made.")
            return

        updated_task["deadline"] = deadline

    status = input(
        "Status (Pending/Completed) ["
        + task["status"] + "]: "
    ).strip().lower()

    if status != "":
        if status == "pending":
            updated_task["status"] = "Pending"
        elif status == "completed":
            updated_task["status"] = "Completed"
        else:
            print("Error: Invalid status. No changes made.")
            return

    # Apply changes only after all inputs are valid
    task.update(updated_task)
    save_tasks(tasks)

    print("Task updated successfully!")


def delete_task(tasks):
    try:
        task_id = int(input("Enter Task ID to delete: "))
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    task = find_task(tasks, task_id)

    if task is None:
        print("Error: Task not found.")
        return

    tasks.remove(task)

    save_tasks(tasks)

    print("Task deleted successfully!")


def search_task(tasks):
    keyword = input("Enter task name to search: ").strip().lower()

    if keyword == "":
        print("Search cannot be empty.")
        return

    found = False

    for task in tasks:
        if keyword in task["name"].lower():
            print("\nTask ID:", task["id"])
            print("Task Name:", task["name"])
            print("Deadline:", task["deadline"])
            print("Status:", get_task_status(task))
            found = True

    if not found:
        print("No matching tasks found.")


def deadline_reminders(tasks):
    today = date.today()
    tomorrow = today + timedelta(days=1)
    found = False

    print("\n====== DEADLINE REMINDERS ======")

    for task in tasks:
        if task["status"] == "Completed":
            continue

        deadline = datetime.strptime(
            task["deadline"], "%Y-%m-%d"
        ).date()

        if today <= deadline <= tomorrow:
            print(task["name"], "-", task["deadline"])
            found = True

    if not found:
        print("No tasks due today or tomorrow.")



def task_statistics(tasks):
    counts = Counter(task["status"] for task in tasks)

    completed = counts["Completed"]
    pending = len(tasks) - completed

    overdue = 0
    upcoming = 0

    for task in tasks:
        status = get_task_status(task)

        if status == "OVERDUE":
            overdue += 1
        elif status == "UPCOMING":
            upcoming += 1

    print("\n====== TASK STATISTICS ======")
    print("Total tasks:", len(tasks))
    print("Completed:", completed)
    print("Not completed:", pending)
    print("Overdue:", overdue)
    print("Upcoming:", upcoming)


def main():
    tasks = load_tasks()

    if tasks is None:
        print("Task Manager cannot start until the file is fixed.")
        return

    while True:
        print("\n====== TASK MANAGER ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Deadline reminders")
        print("7. Task Statistics")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            update_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            search_task(tasks)

        elif choice == "6":
            deadline_reminders(tasks)
        
        elif choice == "7":
            task_statistics(tasks)

        elif choice == "8":
            print("Exiting Task Manager!")
            break

        else:
            print("Invalid choice. Please enter 1 to 8.")


if __name__ == "__main__":
    main()
