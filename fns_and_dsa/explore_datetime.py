#This is just an exploration of the datetime module.

import datetime

def display_current_datetime():
    current_date = (datetime.datetime.today()).replace(microsecond=0)
    return current_date
def calculate_future_date(no_of_days):
    future_date = datetime.date.today() + datetime.timedelta(days=no_of_days)
    return future_date

def main():
    print(f"Current date and time: {display_current_datetime()}")
    days = int(input("Enter the number of days to add to the current date: "))
    fdate = calculate_future_date(days)
    print(f"Future date: {fdate}")
        
main()