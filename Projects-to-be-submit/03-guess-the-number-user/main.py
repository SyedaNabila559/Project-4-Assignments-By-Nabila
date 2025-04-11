import random
from colorama import Fore, Back, Style
import time


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


def print_rules():
    """
    Prints the rules of the game.
    """

    print(Fore.YELLOW)
    delay_print(f"Think of a number between 1 and {MAX_VALUE}, and I'll try to guess it!")
    time.sleep(0.5)
    delay_print(f"Press Enter to continue", end='')
    input('')
    print(f"{Fore.WHITE + Style.BRIGHT} {'#'*31} {Style.RESET_ALL}")


def end_game(num: int | None = None, attempts: int = 1, error: bool = False):
    """
    Ends the game by displaying the final number and a series of thank you messages.
    Args:
        num (int): The number that was to be guessed in the game.
        attempts (int): The number of attempts it took to guess the number.
    """
    
    if not error:
        delay_print(f"{Fore.GREEN + Style.BRIGHT}Yay! I guess the number {num} in only {attempts} attempts.")
        time.sleep(0.5)
    
    print(f"\n{Back.MAGENTA} {'#'*31} ")
    time.sleep(0.5)
    print("       Thanks for playing!       ")
    time.sleep(0.5)
    print("          See you soon!          ")
    time.sleep(0.5)
    print(f" {'#'*31}  {Style.RESET_ALL}")






def main():

    low = 1
    high = MAX_VALUE
    feedback = ''
    attempts = 0

    welcome()
    print_rules()

    while True:

        computer_guess = random.randint(low, high)
        attempts += 1
        
        delay_print(f"{Style.RESET_ALL}Hmmmm! I guess number {computer_guess}")
        feedback = input(f"{Fore.CYAN}Is it (H)igh, (L)ow, or (C)orrect? {Style.RESET_ALL}").lower()

        
        while feedback not in ['c', 'l', 'h']:
            delay_print(f"{Fore.RED} Please enter {Style.BRIGHT}H, L, or C{Style.NORMAL} only! ", end='')
            feedback = input('').lower()

        
        if feedback == "c":
            end_game(computer_guess, attempts)
            break

        elif feedback == 'l':
            low = computer_guess + 1

        elif feedback == 'h':
            high = computer_guess - 1
        



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        end_game(error=True)