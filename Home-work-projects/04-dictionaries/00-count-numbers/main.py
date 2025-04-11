def get_user_numbers() -> list[int]:
    """
    Create an empty list.
    Ask the user to input numbers and store them in a list. 
    Once they enter a blank line, break out of the loop and return the list.
    """

    user_numbers: list[int] = []
    user_input: str = input("Enter a number: ")
    
    while user_input != "":
        user_numbers.append(int(user_input))  
        user_input: str = input("Enter a number: ")
    
    return user_numbers


def count_nums(num_lst: list[int]) -> dict[int, int]:
    """
    Create an empty dictionary.
    Loop over the list of numbers. 
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in the dictionary, increment its value by 1.
    """
    num_dict: dict[int, int] = {}

    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
            
        else:
            num_dict[num] += 1

    return num_dict


def print_counts(num_dict: dict[int, int]) -> None:
    """
    Loop over the dictionary and print out each key and its value.
    """
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")


def main():
    """
    Ask the user to input numbers and store them in a list. Once they enter a blank line,
    print out the number of times each number appeared in the list.
    """
    
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print('='*50)
    print_counts(num_dict)


if __name__ == '__main__':
    main()