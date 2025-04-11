import random

def main():
    """A simple numberr guessing game"""
    
    secret_number = random.randint(1, 99)
    print(f"\n{'-'*11} Number Guessing Game {'-'*11}")
    print("I am thinking of a number between 1 and 99...")
    
    guess = int(input("Enter a guess: "))
    
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        guess = int(input("\nEnter a new guess: ")) 
        
    print(f"Congrats! The number was: {secret_number}")
    
if __name__ == '__main__':
    main()