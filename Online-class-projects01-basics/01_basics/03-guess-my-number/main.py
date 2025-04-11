from colorama import Fore, Style, Back
import random

WELCOME = f"{Back.MAGENTA + Fore.WHITE + Style.BRIGHT} {' '*12}Guess My Number{' '*12}"
INTRO = f"{Style.RESET_ALL + Fore.MAGENTA}I am thinking of a number between 0 and 99..."
FIRST_QUESTION = f"\n{Fore.CYAN + Style.BRIGHT}Enter a guess: {Style.RESET_ALL}"
QUESTION = f"\n{Fore.CYAN + Style.BRIGHT}Enter a new number: {Style.RESET_ALL}"

def main():
    """
    Main function to run the "Guess My Number" game.  
    The game generates a random number between 0 and 99, and the user has to guess the number.  
    The function provides feedback if the guess is too high or too low until the user guesses correctly.  
    When the correct number is guessed, a congratulatory message is displayed.
    """

    print(WELCOME)
    print(INTRO)
    
    number: int = random.randint(0, 99)
    user_guess = int(input(FIRST_QUESTION))

    while user_guess != number:
        if user_guess > number:
            print(Fore.YELLOW + "Your guess is too high")
        else:
            print(Fore.RED + "Your guess is too low")
        user_guess = int(input(QUESTION))

    print(f"{Fore.GREEN} Congrats! The number was: {user_guess} {Style.RESET_ALL}")


if __name__ == '__main__':
    main()