from datetime import datetime, timedelta, date
#This is just an exploration of the datetime module.

def display_current_datetime():
    current_date = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    return current_date
def calculate_future_date(no_of_days):
    future_date = date.today() + timedelta(days=no_of_days)
    return future_date

def main():
    print(f"Current date and time: {display_current_datetime()}")
    days = int(input("Enter the number of days to add to the current date: "))
    fdate = calculate_future_date(days)
    print(f"Future date: {fdate}")

main()