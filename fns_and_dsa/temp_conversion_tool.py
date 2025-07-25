#This is a simpl temperature converter.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def main():
    temp = float(input("Enter the temperature to convert: "))
    current_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

    if current_unit == 'f':
        result = f"{temp}°F is {convert_to_celsius(temp)}°C"
    elif current_unit == 'c':
        result = f"{temp}°C is {convert_to_fahrenheit(temp)}°F"
    else:
        result = "Unrecognised temperature units"
    print(result)




def convert_to_celsius(fahrenheit):
    return (FAHRENHEIT_TO_CELSIUS_FACTOR*(fahrenheit - 32))
def convert_to_fahrenheit(celsius):
    return (CELSIUS_TO_FAHRENHEIT_FACTOR*celsius + 32)
main()