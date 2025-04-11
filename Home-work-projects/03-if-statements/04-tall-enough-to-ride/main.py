MINIMUM_HEIGHT : int = 50 

def main():
    """
    A program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.
    """
    
    height: float = float(input("How tall are you? "))

    while height < MINIMUM_HEIGHT:
        print("You're not tall enough to ride, but maybe next year!")
        height = float(input("How tall are you? "))

    print("You're tall enough to ride!")


if __name__ == '__main__':
    main()