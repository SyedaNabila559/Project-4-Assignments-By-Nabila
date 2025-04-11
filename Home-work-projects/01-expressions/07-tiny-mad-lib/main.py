def main():
    """Generates a fun and interactive Python programmer-themed Madlib story.  
    Prompts the user to input various words and phrases, which are then used to 
    fill in the blanks of a pre-defined story template. The completed story is 
    printed out for the user to enjoy.
    """

    print("🐍 Python Programmer Madlib 💻")
    
    name = input("Enter your name: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    funny_phrase = input("Enter a funny phrase: ")
    random_object = input("Enter a random object: ")
    random_action = input("Enter a random action: ")
    silly_method = input("Enter a silly method to fix bugs: ")
    random_word = input("Enter a random word: ")

    madlib = f"""
    One day, a {adjective} Python programmer named {name} was working on a {noun}.
    Suddenly, their code started {verb_ing}! 😱
    They quickly checked Stack Overflow, but the answer was just "{funny_phrase}". 🤦‍♂️
    
    Desperate, they tried debugging with {random_object}, but instead, their computer started {random_action}. 💥
    In the end, they fixed the bug by {silly_method}, and their program finally printed:
    
    "Hello, {random_word}!" 🎉
    """

    print(madlib)

if __name__ == "__main__":
    main()