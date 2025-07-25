#contains a function that can perform all four basic arithmetic operations.

def perform_operations(num1: float, num2: float, operation: str):
    if operation == "add":
        return (num1 + num2)
    elif operation == "subtract":
        return (num1 - num2)
    elif operation == "multiply":
        return (num1*num2)
    else:
        if num2 != 0:
            return (num1/num2)
        else:
            return "The second number (denominator) cannot be 0!"               
    