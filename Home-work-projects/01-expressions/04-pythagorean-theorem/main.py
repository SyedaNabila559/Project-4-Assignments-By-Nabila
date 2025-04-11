import math 

def main():
    """
    Prompts the user to enter the lengths of the two legs of a right triangle (AB and AC),
    calculates the length of the hypotenuse (BC) using the Pythagorean theorem, 
    and prints the result.  
    """

    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    bc: float = math.sqrt(ab**2 + ac**2)
    print(f"The length of BC (the hypotenuse) is: {bc}")


if __name__ == '__main__':
    main()