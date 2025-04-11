def main():
    """
    Prompts the user to enter a number and repeatedly doubles the value until it exceeds 100,
    printing each intermediate value.
    """
    curr_value: int = int(input("Enter a number: "))

    while curr_value <= 100:
        curr_value *= 2
        print(curr_value)


if __name__ == '__main__':
    main()