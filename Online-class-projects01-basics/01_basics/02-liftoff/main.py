from colorama import Fore, Style
from time import sleep

def main():
    """
    Executes a countdown from 10 to 1 with a half-second interval between each number,
    and prints "Liftoff!" at the end.  
    The countdown numbers are displayed in bright cyan,
    and the "Liftoff!" message is displayed in green.
    """

    for i in range(10, 0, -1):
        print(Fore.CYAN + Style.BRIGHT + str(i))
        sleep(0.5)
    
    print(Fore.GREEN + "Liftoff!" + Style.RESET_ALL)

if __name__ == '__main__':
    main()