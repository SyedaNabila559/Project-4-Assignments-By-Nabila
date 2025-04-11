import random
import string
import sys
import time
from typing import Iterable
from colorama import Fore, Style
import requests

LIVES = 6

APPRECIATION_WORDS = [
    "Great job!",
    "Well done!",
    "Nice work!",
    "Keep it up!",
    "You're doing great!",
    "Fantastic!",
    "Excellent!",
    "Superb!",
    "Impressive!",
    "You're on fire!"
]


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



def get_words() -> list[str]:
    """
    Fetches a list of words from an online source and return it.  
    If the request fails, returns a default list of words.
    """
    
    default_words = ["absent", "little", "rotten", "doctor", "unknown"]

    try:
        response = requests.get("https://www.randomlists.com/data/words.json")

        if response.status_code == 200:
            data = response.json()
            return data["data"]

        return default_words

    except Exception:
        return default_words



def display_initial_message(word: str):
    """
    Displays the initial message to the player, including the length of the word and the number of lives.
    
    Args:
        word (str): The word to be guessed.
    """
    delay_print(f"\n{Fore.YELLOW}I think of a word, it has {Style.BRIGHT}{len(word)}{Style.NORMAL} letters.")
    delay_print(f"{Style.NORMAL}You have {Style.BRIGHT}{LIVES}{Style.NORMAL} lives to guess it.")
    delay_print(f"Let's see if you win or...")

    delay_print(f"\n{Fore.CYAN + Style.BRIGHT}Press enter to start: ", end='')
    input()


def display_game_status(word: str, used_letters: Iterable[str], lives: int):
    """
    Displays the current status of the game, including the current word with guessed letters, used letters, and remaining lives.
    
    Args:
        word (str): The word to be guessed.
        used_letters (Iterable[str]): The letters that have been guessed so far.
        lives (int): The number of lives remaining.
    """
    word_list = [letter if letter in used_letters else '__' for letter in word]
    delay_print(f"{Fore.YELLOW}You have {Style.BRIGHT}{lives}{Style.NORMAL} lives left.")
    delay_print(f"\n{Style.RESET_ALL}Current word: {Style.BRIGHT}{' '.join(word_list)}")
    delay_print(f"{Style.NORMAL}You have used these letters: {Style.BRIGHT}{' '.join(used_letters)}")


def end_game():
    """
    Ends the game by printing a farewell message and exiting the program.
    This function uses `delay_print` to display a thank you message to the player
    and then terminates the program using `sys.exit(0)`.
    """

    delay_print(f"\n{Fore.MAGENTA + Style.BRIGHT} Thanks for playing! ")
    delay_print(f" See you next time! {Style.RESET_ALL}")
    sys.exit(0)


def main():

    delay_print(f"{Fore.MAGENTA + Style.BRIGHT} Hey! Let's play hangman! {Style.RESET_ALL}")
    time.sleep(0.5)

    words = get_words()
    word = random.choice(words).upper()
    word_letters = set(word)
    alphabats = set(string.ascii_uppercase)
    used_letters: set[str] = set()
    
    lives = 6

    display_initial_message(word)

    while len(word_letters):

        if lives <= 0:
            delay_print(f"{Fore.RED}Opps! You died!")
            delay_print(f"{Fore.YELLOW}The word was {Style.BRIGHT}{word}.")
            end_game()
       

        delay_print(f"\n{Fore.CYAN + Style.BRIGHT}Guess a letter: {Style.RESET_ALL}", end='')
        user_letter = input().upper()


        if user_letter in (alphabats - used_letters):
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                delay_print(Fore.GREEN + random.choice(APPRECIATION_WORDS))

            else: 
                lives -= 1
                delay_print(f"{Fore.RED}Letter not in word!")


        elif user_letter in used_letters:
            delay_print(f"{Fore.RED}You have alread used that letter!")

        else:
            delay_print(f"{Fore.RED}Invalid character!")
            continue


        display_game_status(word, used_letters, lives)


    delay_print(f"{Fore.GREEN}Yay! You guessed the word!")
    end_game()
            


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        end_game()