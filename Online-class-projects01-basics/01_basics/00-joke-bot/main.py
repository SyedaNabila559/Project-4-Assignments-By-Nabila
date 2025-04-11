from colorama import Fore, Style

PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you!\n Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY: str = "Sorry I only tell jokes."

def main():
    """
    Main function to interact with the user and respond with a joke or an apology.
    Prompts the user for input and checks if the input contains the word "joke".
    If it does, it prints a joke in magenta color.
    Otherwise, it prints an apology in red color.
    The function uses color formatting from the `colorama` library.
    """

    user_input:str = input(Fore.CYAN + Style.BRIGHT + PROMPT + Style.RESET_ALL).strip().lower()
    
    if "joke" in user_input:
        print(Fore.MAGENTA + JOKE)
    else:
        print(Fore.RED + SORRY)
    print(Style.RESET_ALL)


if __name__ == '__main__':
    main()