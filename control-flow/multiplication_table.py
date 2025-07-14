#This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.

def main():
    number = int(input("Enter a number to see its multiplication table: "))
    times_table(number)

def times_table(number):
    """Returns a multiplicaiton table for any given positive integer."""
    for i in range(1, 11):
        print(f"{number * i} = {number*i}")

main()