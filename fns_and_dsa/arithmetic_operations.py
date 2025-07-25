#contains a function that can perform all four basic arithmetic operations.

def perform_operation(num1, num2, operation):
    if operation == "add":
        return (num1 + num2)
    elif operation == "subtract":
        return (num1 - num2)
    elif operation == "multiply":
        return (num1*num2)
    else:
        if num2 == 0:
            return "The second number (denominator) cannot be 0!"        
        else:
            return (num1/num2)             
    