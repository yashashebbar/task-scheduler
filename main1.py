import datetime

# Function to add a task to the scheduler
def add_task(task, due_date, task_scheduler):
    task_scheduler[task] = due_date
    print(f"Task '{task}' added to the scheduler.")

# Function to mark a task as completed
def mark_task_completed(task, task_scheduler):
    if task in task_scheduler:
        del task_scheduler[task]
        print(f"Task '{task}' marked as completed.")
    else:
        print(f"Task '{task}' not found in the scheduler.")

# Function to display the current tasks
def display_tasks(task_scheduler):
    if task_scheduler:
        print("Current tasks:")
        for task, due_date in task_scheduler.items():
            print(f"Task: {task}, Due at: {due_date.strftime('%Y-%m-%d %H:%M')}")
    else:
        print("No tasks in the scheduler.")

# Function to save tasks to a file
def save_tasks_to_file(file_name, task_scheduler):
    with open(file_name, "w") as file:
        for task, due_date in task_scheduler.items():
            file.write(f"{task},{due_date.strftime('%Y-%m-%d %H:%M')}\n")

# Function to load tasks from a file
def load_tasks_from_file(file_name):
    task_scheduler = {}
    try:
        with open(file_name, "r") as file:
            for line in file:
                task, due_date_str = line.strip().split(",")
                due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
                task_scheduler[task] = due_date
    except FileNotFoundError:
        pass
    return task_scheduler

# Main program
task_file = "tasks.txt"
task_scheduler = load_tasks_from_file(task_file)

while True:
    print("\nTask Scheduler with Reminders")
    print("1. Add a new task")
    print("2. Mark a task as completed")
    print("3. Display current tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task description: ")
        due_date_str = input("Enter the due date and time (YYYY-MM-DD HH:MM): ")
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
        
        add_task(task, due_date, task_scheduler)
        save_tasks_to_file(task_file, task_scheduler)
    elif choice == "2":
        task = input("Enter the task to mark as completed: ")
        mark_task_completed(task, task_scheduler)
        save_tasks_to_file(task_file, task_scheduler)
    elif choice == "3":
        display_tasks(task_scheduler)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
