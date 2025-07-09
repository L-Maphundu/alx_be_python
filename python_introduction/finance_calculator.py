#In this script we will be calculating monthly savings and annual savings with interest.

def main():
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))
    monthly_savings = monthly_income - monthly_expenses
    print(f"Your monthly savings are ${monthly_savings}.")
    print(f"Projected savings after one year, with interest, is: ${savings(monthly_savings)}.")

def savings(monthly: float):
    """Calculates annual savings given monthly savings
    and an interest rate of 5%"""

    return (monthly * 12 + (monthly*12*0.05))
main()