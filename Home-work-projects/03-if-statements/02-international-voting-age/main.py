PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    """
    Main function to determine if the user can vote in different countries based on their age.
    Prompts the user to input their age and checks if they meet the voting age requirements for the following countries:
    - Peturksbouipo
    - Stanlau
    - Mayengua
    Depending on the user's age, the function prints whether the user can or cannot vote in each country.
    """

    user_age: int = int(input("How old are you? "))

    # Check if the user can vote in Peturksbouipo
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    

    # Check if the user can vote in Stanlau
    if user_age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")
    

    # Check if user can vote in Mayengua
    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")


if __name__ == '__main__':
    main()