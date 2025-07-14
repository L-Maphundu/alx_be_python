#This script is for recommendation for what to wear based on what the user is.

def main():
    wthr = input("What's the weather like today? (sunny/rainy/cold): ").lower()
    what_to_wear(wthr)

def what_to_wear(weather: str) -> str:
    """Returns a recommendation for what to wear based on whether the weather (wthr)
    is sunny, rainy or cold."""

    if weather == 'sunny': print("Wear a t-shirt and sunglasses.")
    elif weather == 'rainy': print("Don't forget your umbrella and a raincoat.")
    elif weather == 'cold': print("Make sure to wear a warm coat and a scarf.")
    else: print("Sorry, I don't have recommendations for this weather.")
    
main()