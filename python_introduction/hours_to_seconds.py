#In this script We will Converts given hours into seconds.

def main():
    hours = 2
    seconds = timeInSec(hours)
    print(f"{hours} hour(s) is {seconds} seconds.")

def timeInSec(h: float):
    """Converts given hours (h) into seconds"""
    return h*3600

main()

