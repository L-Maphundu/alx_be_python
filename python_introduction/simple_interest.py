#This script is for calculating simple interest given principal amount, interest rate and time.

def main():
    principal = 1000
    rate = 0.05
    time = 3
    interest = interestAmount(principal,rate,time)
    print(f"The simple interest is: {interest}")

def interestAmount(p: float,r: float,t: float) -> float:
    """Calculates interest amount given: principal amount(p),interest rate (r) and time (t)"""
    return p*r*t
main()