# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority level."

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it at your convenience."

# Print the customized reminder
print(f"Reminder: {reminder}")

