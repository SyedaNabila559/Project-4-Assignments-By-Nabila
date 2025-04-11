def main():
    """
    Asks the user for their favorite animal and prints a message agreeing with their choice.
    """

    print("Welcome to the Agreement Bot!")
    fav_animal = input("What's your favorite animal? ")
    print(f"My favorite animal is also {fav_animal.lower()}!")


if __name__ == '__main__':
    main()