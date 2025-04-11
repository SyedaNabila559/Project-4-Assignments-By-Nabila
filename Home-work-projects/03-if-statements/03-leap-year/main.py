def main():
    """ 
    A program that reads a year from the user and tells whether a given year is a leap year or not.
    """
    year = int(input('Please input a year: '))

    if year % 4 != 0:
        print("That's not a leap year.")
    
    elif year % 100 == 0 and year % 400 == 0:
        print("That's a leap year!")

    else:
        print("That's not a leap year!")


if __name__ == '__main__':
    main()