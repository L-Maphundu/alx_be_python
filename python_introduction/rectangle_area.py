#Here we calculate the area of a rectangle given length and width.
def main():
    length = 10
    width = 5
    area = rectArea(length,width)
    print(f"The area of the rectangle is: {area}")

def rectArea(l: float,w: float)-> float:
    """Calculates the area of a rectangle given length and width. Assumes the user will always select positive values for length and width."""
    return l*w

main()