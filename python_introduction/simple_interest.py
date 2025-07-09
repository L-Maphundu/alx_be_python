#This script is for calculating simple interest given principal (p) amount, interest rate (r) and time (t).

def main():
    p = 1000
    r = 0.05
    t = 3
    print(f"The simple interest is: {interest(p, r,t)}")

def interest(principal: float,rate: float,time: float) -> float:
    """Calculates interest amount given: principal amount(p),interest rate (r) and time (t)"""
    interest = principal * rate * time
    return interest
main()