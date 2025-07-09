#Here we will calculate the future age of an individual.

def main():
    currentAge = int(input('How old are you? '))
    print(f"In 2050, you will be {futureAge(currentAge)} years old.")

def futureAge(age: int) -> int:
    """Given that the current year is 2023, calculates the future age
    of an individual in 2050"""
    return (27 + age)

main()