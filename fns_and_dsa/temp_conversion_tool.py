FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))  # Get temperature input from the user
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()  # Get unit input from the user

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)  # Call function to convert to Fahrenheit
            print(f"{temp}°C is {converted_temp}°F")  # Output the result
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)  # Call function to convert to Celsius
            print(f"{temp}°F is {converted_temp}°C")  # Output the result
        else:
            print("Error: Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")  # Handle invalid unit input
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")  # Handle non-numeric input

if __name__ == "__main__":
    main()  # Run the main function

