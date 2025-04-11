import random
import time
from colorama import Fore, Style
import inquirer


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


def choice_input(message: str, choices: list[str], name = 'key') -> str:
    """
    Prompts the user to select an option from a list of choices.
    Args:
        message (str): The message to display to the user.
        choices (list[str]): A list of choices for the user to select from.
        name (str, optional): The key name for the answer dictionary. Defaults to 'key'.
    Returns:
        str: The selected choice from the list.
    """
    
    question = inquirer.List(name, message=message, choices=choices, carousel=True)
    answer = inquirer.prompt([question])

    while not answer:
        answer = inquirer.prompt([question])
    
    return answer[name]



def is_win(player1: str, player2: str):
    """
    Determine if player1 wins against player2 in a game of rock-paper-scissors.
    Args:
        player1 (str): The choice of player1, which can be "rock", "paper", or "scissors".
        player2 (str): The choice of player2, which can be "rock", "paper", or "scissors".
    Returns:
        bool: True if player1 wins against player2, False otherwise.
    """

    con1 = player1 == "rock" and player2 == "scissors"
    con2 = player1 == "paper" and player2 == "rock"
    con3 = player1 == "scissors" and player2 == "paper"
    
    return con1 or con2 or con3
    

def main():

    delay_print(f"{Fore.MAGENTA + Style.BRIGHT} Hey! Wanna play rock, paper, scissors! ")
    time.sleep(0.5)

    choices = ["Rock", "Paper", "Scissors"]
    user_choice = choice_input("Choose one of them", choices)
    computer_choice = random.choice(choices)


    delay_print(f"You choose: {user_choice}")
    delay_print(f"I choose: {computer_choice}")

    print(Fore.CYAN + Style.BRIGHT)

    if user_choice == computer_choice:
        delay_print("It's a tie!")
    
    elif is_win(user_choice.lower(), computer_choice.lower()):
        delay_print("Yay! You win!")

    else:
        delay_print("Opps! You lose! Better luck next time.")
    
    print(Style.RESET_ALL)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        delay_print(f"{Fore.MAGENTA + Style.BRIGHT} See you next time! {Style.RESET_ALL}")