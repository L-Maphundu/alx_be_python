#In this script We will Converts given hours into seconds.

def main():
    hours = 2
    print(f"{hours} hour(s) is {timeInSec(hours)} seconds.")

def timeInSec(hours: float):
    """Converts given hours (h) into seconds"""
    seconds = hours * 3600
    return seconds

main()

