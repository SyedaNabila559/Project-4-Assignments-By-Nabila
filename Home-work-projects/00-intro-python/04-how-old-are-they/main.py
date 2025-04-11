def main():
    """
    This program calculates and prints the ages of five friends: Anton, Beth, Chen, Drew, and Ethan.

    Anton is 21 years old.  
    Beth is 6 years older than Anton.  
    Chen is 20 years older than Beth.  
    Drew is as old as Chen's age plus Anton's age.  
    Ethan is the same age as Chen.
    
    The program stores each person's age in a variable and prints their names and ages.
    """

    anton_age: int = 21
    beth_age: int = anton_age + 6
    chen_age: int = beth_age + 20
    drew_age: int = chen_age + anton_age
    ethan_age: int = chen_age

    print(f"Anton is {anton_age}")
    print(f"Beth is {beth_age}")
    print(f"Chen is {chen_age}")
    print(f"Drew is {drew_age}")
    print(f"Ethan is {ethan_age}")

if __name__ == '__main__':
    main()