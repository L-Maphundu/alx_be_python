#This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division).
#The script will then perform the selected operation using a Match Case statement and display the result.

def main():
    nmbr1 = float(input("Enter the first number: "))
    nmbr2 = float(input("Enter the second number: "))
    oprtr = input("Choose the operation (+, -, *, /): ")
    arithmetic(nmbr1, nmbr2, oprtr)

def arithmetic(num1: float, num2: float, operation: str) -> float:
    """Returns an answer based on a chosen operation (+, -, *, /)
    between two numbers"""

    match operation:
        case '+': print(f"The result is {num1 + num2}.")
        case '-': print(f"The result is {num1 - num2}.")
        case '*': print(f"The result is {num1 * num2}.")
        case '/': 
            if num2 == 0: print("Cannot divide by zero.")
            else: print(f"The result is {num1 / num2}.")

main()