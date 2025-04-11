AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    """
    A program which prompts the user to type an affirmation of your choice until they type it correctly.
    """
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()
    while user_feedback != AFFIRMATION: 
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")


if __name__ == '__main__':
    main()