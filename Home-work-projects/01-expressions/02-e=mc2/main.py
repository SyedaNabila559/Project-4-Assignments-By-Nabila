SPEED_OF_LIGHT = 299792458

def main():
    """
    Calculates the energy equivalent of a given mass using the formula E=mc^2.  
    Prompts the user to input a mass in kilograms, then calculates the energy
    using the speed of light constant and prints the result.
    """
    
    mass: float = float(input("Enter kilos of mass: "))
    energy: float = mass * (SPEED_OF_LIGHT**2)

    print("e = m * C^2... ")
    print(f"m = {mass} kg")
    print(f"C = {SPEED_OF_LIGHT} m/s")
    print(f"{energy} joules of energy!")


if __name__ == '__main__':
    main()