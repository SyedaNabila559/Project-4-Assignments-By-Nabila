def main():
    """
    Prompts the user to input a number, calculates its square, and prints the result.  
    The function reads a floating-point number from the user, computes its square,
    and displays the squared value in a formatted string.
    """

    num: float = float(input("Type a number to see its square: "))
    print(f"{num} squared is {num ** 2}") 


if __name__ == '__main__':
    main()