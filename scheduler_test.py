import datetime
import time
from plyer import notification

# Function to check and notify about upcoming tasks
def check_upcoming_tasks(task_scheduler):
    current_time = datetime.datetime.now()
    notification_time = current_time + datetime.timedelta(minutes=10)  # Notify tasks due in 10 minutes

    upcoming_tasks = [task for task, due_date in task_scheduler.items() if current_time <= due_date <= notification_time]

    for task in upcoming_tasks:
        notification_title = "Upcoming Task Reminder"
        notification_message = f"Task: {task}\nDue at {task_scheduler[task].strftime('%Y-%m-%d %H:%M')}"
        notification.notify(
            title=notification_title,
            message=notification_message,
            timeout=10
        )

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
    task_scheduler = load_tasks_from_file(task_file)
    check_upcoming_tasks(task_scheduler)
    time.sleep(60)  # Check every minute
