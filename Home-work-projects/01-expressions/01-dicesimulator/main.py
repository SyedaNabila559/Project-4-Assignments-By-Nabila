import random

NUM_SIDES = 6

def roll_dice():
    """Simulates rolling two dice and prints their total"""

    dice1: int = random.randint(1, NUM_SIDES)
    dice2: int = random.randint(1, NUM_SIDES)
    total: int = dice1 + dice2
    print(f"Total of two dice: {total}")


def main():
    dice1: int = 10
    print(f"dice1 in main() starts as: {dice1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"dice1 in main() is: {dice1}")


if __name__ == '__main__':
    main()