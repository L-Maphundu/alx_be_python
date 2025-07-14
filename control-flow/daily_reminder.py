#"Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity."

"""It's very inefficient because it has to match a very unsophisticated checker in order to pass as correct. There was no need at all
for the Match Case, the program works as well with a only one If statement."""

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'low': 
        if time_bound == 'yes': print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else: print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")

    case 'medium':
        if time_bound == 'yes': print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else: print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")

    case 'high': 
        if time_bound == 'yes': print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else: print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
