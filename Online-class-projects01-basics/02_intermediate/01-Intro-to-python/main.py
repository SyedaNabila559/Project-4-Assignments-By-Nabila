"""
Prompts the user for a temperature on Earth
and a planet (in separate inputs). Then 
prints the equivalent temperature on that planet.
"""

# Dictionary storing temperature multipliers for each planet
TEMPERATURE_FACTORS = {
    "Mercury": 1.5,
    "Venus": 0.92,
    "Mars": 1.03,
    "Jupiter": 1.6,
    "Saturn": 1.3,
    "Uranus": 0.7,
    "Neptune": 0.9
}

def venus_temperature():
    """Prompts user for Earth temperature and calculates temperature on Venus."""
    earth_temp = float(input("Enter a temperature on Earth (in Celsius): "))
    venus_temp = round(earth_temp * TEMPERATURE_FACTORS["Venus"], 2)
    print(f"The equivalent temperature on Venus: {venus_temp}°C")

def planetary_temperature():
    """Prompts user for Earth temperature and calculates temperature on any planet."""
    earth_temp = float(input("Enter a temperature on Earth (in Celsius): "))
    planet = input("Enter a planet: ")

    if planet in TEMPERATURE_FACTORS:
        temp_on_planet = round(earth_temp * TEMPERATURE_FACTORS[planet], 2)
        print(f"The equivalent temperature on {planet}: {temp_on_planet}°C")
    else:
        print("Invalid planet name. Please enter a valid planet.")

def main():
    """Main function to allow user to choose between Venus or any planet."""
    print("Choose an option:")
    print("1. Calculate temperature on Venus")
    print("2. Calculate temperature on any planet")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        venus_temperature()
    elif choice == "2":
        planetary_temperature()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
