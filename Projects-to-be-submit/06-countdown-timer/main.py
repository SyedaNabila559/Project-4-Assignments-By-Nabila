import time
from colorama import Fore, Style


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


def countdown(seconds: int):
    """
    Countdown timer that prints the remaining time in MM:SS format.

    Args:
        seconds (int): The number of seconds to count down from.
    """

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1


def main():

    delay_print(f"{Fore.MAGENTA + Style.BRIGHT} Welcome to countdown timer\n")
    time.sleep(0.5)
    delay_print(f"{Fore.CYAN}Enter time in seconds: {Style.RESET_ALL}", 0.01, end='')

    user_input = input('')

    while not user_input.isdigit():
        delay_print(f"{Fore.CYAN}Enter time in seconds: {Style.RESET_ALL}", 0.01, end='')
        user_input = input('')

    countdown(int(user_input))

    delay_print(f"\n{Fore.MAGENTA + Style.BRIGHT} Times up! {Style.RESET_ALL}")



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        delay_print(f"\n{Fore.MAGENTA + Style.BRIGHT} Times up! {Style.RESET_ALL}")