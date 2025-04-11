def main():
    """
    This function calculates the perimeter of a triangle based on user input.  
    It prompts the user to input the lengths of the three sides of the triangle,
    calculates the perimeter by summing these lengths, and then prints the result.
    """
    
    print("Welcome to the Triangle Perimeter Calculator!")

    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    perimeter = side1 + side2 + side3
    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == '__main__':
    main()