import random
import sys
from colorama import Fore, Back, Style
import time

MIN_VALUE = 1
MAX_VALUE = 50

def delay_print(value: str, delay: float = 0.05, end: str = "\n"):
    """
    Prints the given string value character by character with a specified delay between each character.
    Args:
        value (str): The string to be printed.
        delay (float, optional): The delay in seconds between each character. Default is 0.1 seconds.
        end (str, optional): The string appended after the last value. Default is a newline character.
    """

    for char in value:
        print(char, end='')
        time.sleep(delay)
    print(end=end)


def welcome():
    """
    Prints a welcome message for the number guessing game with styled text and delays.
    """

    print(f"{Back.MAGENTA + Style.BRIGHT} {'#'*31} ")
    time.sleep(0.5)
    print(" Welcome to number guessing game ")
    time.sleep(0.5)
    print(f" {'#'*31} {Style.RESET_ALL}")


def print_rules(lives: int):
    """
    Prints the rules of the game.

    Args:
        lives (int): The total number of lives the player has.

    """
    print(Fore.YELLOW)
    delay_print(f"You have to guess a number between {MIN_VALUE} and {MAX_VALUE}.")
    time.sleep(0.5)
    delay_print(f"You have total {lives} lives.")
    time.sleep(0.5)
    delay_print("Let's start the game!")
    time.sleep(0.5)
    print(f"{Fore.WHITE + Style.BRIGHT} {'#'*31} {Style.RESET_ALL}")


def end_game(num: int | None = None):
    """
    Ends the game by displaying the final number and a series of thank you messages.
    Args:
        num (int): The number that was to be guessed in the game.
    """
    
    delay_print(f"{Fore.CYAN + Style.BRIGHT}The number was {num}.")
    time.sleep(0.5)
    print(f"\n{Back.MAGENTA} {'#'*31} ")
    time.sleep(0.5)
    print("       Thanks for playing!       ")
    time.sleep(0.5)
    print("          See you soon!          ")
    time.sleep(0.5)
    print(f" {'#'*31}  {Style.RESET_ALL}")






def main():

    lives = 5
    user_guess = 0
    # random_number = 8
    random_number = random.randint(MIN_VALUE, MAX_VALUE)

    welcome()
    print_rules(lives)

    while True:

        if lives <= 0:
            end_game(random_number)
            sys.exit(0)

        user_guess = int(input(f"\n{Fore.CYAN}Enter a number: {Style.RESET_ALL}"))

        if user_guess == random_number:
            break

        if user_guess < random_number:
            delay_print(f"{Fore.RED}Too Low! Try again.")

        if user_guess > random_number:
            delay_print(f"{Fore.RED}Too high! Try again.")
        
        lives -=1
        delay_print(f"{Style.RESET_ALL}You have {lives} live(s) left.")

    delay_print(f"\n{Style.BRIGHT + Fore.GREEN}Congratulations! You won")
    end_game(random_number)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        end_game()