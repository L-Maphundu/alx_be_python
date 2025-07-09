#This script is for calculating simple interest given principal (p) amount, interest rate (r) and time (t).

def main():
    principal = 1000
    rate = 0.05
    time = 3
    print(f"The simple interest is: {interest(principal, rate,time)}")

def interest(principal: float,rate: float,time: float) -> float:
    """Calculates interest amount given: principal amount(p),interest rate (r) and time (t)"""
    interest = principal * rate * time
    return interest
main()