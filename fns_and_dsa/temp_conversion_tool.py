#This is a simpl temperature converter.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return FAHRENHEIT_TO_CELSIUS_FACTOR*(fahrenheit - 32)
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (CELSIUS_TO_FAHRENHEIT_FACTOR*celsius) + 32

def main():
    temp_str = input("Enter the temperature to convert: ").strip()
    if temp_str.isnumeric:
        temp = int(temp_str)
    else:
        print("Invalid temperature. Please enter a numeric value."
              )
    current_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

    if current_unit == 'f':
        result = f"{temp}°F is {convert_to_celsius(temp)}°C"
    elif current_unit == 'c':
        result = f"{temp}°C is {convert_to_fahrenheit(temp)}°F"
    else:
        result = "Please make sure the temperature units are in celsius (C) or fahrenheit (F)"
    print(result)
    
main()