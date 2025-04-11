def main():
    """
    Converts a temperature from Fahrenheit to Celsius and prints the result.
    Prompts the user to enter a temperature in Fahrenheit, converts it to Celsius,
    and prints the temperature in both Fahrenheit and Celsius.
    """

    print("Simple program to convert Fahrenheit to Celsius")
    degrees_fahrenheit: float = float(input("Enter temperature in Fahrenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}°C")


if __name__ == '__main__':
    main()