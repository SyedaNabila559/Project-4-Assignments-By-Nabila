def read_phone_numbers() -> dict[str, str]:
    """
    Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook: dict[str, str] = {}

    while True:
        name = input("Name: ").lower()
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook: dict[str, str]) -> None:
    """
    Prints out all the names/numbers in the phonebook.
    """
    print(f"{'='*10} Phone Book {'='*10}")

    for name in phonebook:
        print(f"{name.capitalize()} --> {phonebook[name]}")
    print('='*32)


def lookup_numbers(phonebook: dict[str, str]):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    
    while True:
        name = input("Enter name to lookup: ").lower()
        if name == "":
            break
        if name not in phonebook:
            print(f"{name.capitalize()} is not in the phonebook")
        else:
            print(f"{name.capitalize()} --> {phonebook[name]}")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


# Python boilerplate.
if __name__ == '__main__':
    main()