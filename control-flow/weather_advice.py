#This script is for recommendation for what to wear based on what the user is.

def main():
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
    print(what_to_wear(weather))

def what_to_wear(wthr: str) -> str:
    """Returns a recommendation for what to wear based on whether the weather (wthr)
    is sunny, rainy or cold."""
    
    if wthr == 'sunny': return "Wear a t-shirt and sunglasses."
    elif wthr == 'rainy': return "Don't forget your umbrella and a raincoat." 
    elif wthr == 'cold': return "Make sure to wear a warm coat and a scarf."
    else: return "Sorry, I don't have recommendations for this weather."
    
main()