#Here we calculate the area of a rectangle given length and width.
def main():
    length = 10
    width = 5
    print(f"The area of the rectangle is: {rectArea(length,width)}")

def rectArea(length: float,width: float)-> float:
    """Calculates the area of a rectangle given length and width. 
    Assumes the user will always select positive values for length and width."""
    area = length * width
    return area

main()