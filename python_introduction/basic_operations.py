#This script performs basic arithmetic operations on any 2 selected numbers. Our example numbers will be 10 and 5.

number1 = 10
number2 = 5

def arithmetic(num1: float, num2: float):
    """Given any 2 numbers the function performs basic arithmetic operations on the numbers and prints out an answer for each operation"""
    print(f"Addition of {num1} and {num2} is {num1+num2}")
    print(f"Subtraction of {num1} and {num2} is {num1-num2}")
    print(f"Multiplication of {num1} and {num2} is {num1*num2}")

arithmetic(number1,number2)




