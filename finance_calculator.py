#In this script we will be calculating monthly savings and annual savings with interest.

def main():
    income = float(input("Enter your monthly income: "))
    expenses = float(input("Enter your total monthly expenses: "))
    monthlySavings = income - expenses
    print(f"Your monthly savings are ${monthlySavings}.")
    print(f"Projected savings after one year, with interest, is: ${savings(monthlySavings)}.")

def savings(monthly: float):
    """Calculates annual savings given monthly savings
    and an interest rate of 5%"""

    return (monthly * 12 + (monthly*12*0.05))
main()