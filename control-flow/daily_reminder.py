#Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

message1 = f"Reminder: 'Finish project report' is a {priority} priority task that requires immediate attention today!"
message2 = f"Note: 'Read a book' is a {priority} priority task. Consider completing it when you have free time."
reminder = ""

if time_bound == 'yes': reminder = message1
else: reminder = message2

match priority:
    case 'low': print(reminder)
    case 'medium': print(reminder)
    case 'high': print(reminder)
