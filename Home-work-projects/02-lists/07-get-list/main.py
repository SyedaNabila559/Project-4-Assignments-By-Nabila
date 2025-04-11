def main():
    """
    Prompts the user to enter values and appends them to a list until an empty input is received.  
    Finally, prints the list of entered values.
    """

    lst: list[str] = []  

    value: str = input("Enter a value: ") 
    while value:
        lst.append(value)
        value = input("Enter a value: ")  

    print("Here's the list:", lst)


if __name__ == '__main__':
    main()