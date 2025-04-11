def main():
    """
    Doubles each element in a list of integers and prints the updated list.  
    The function initializes a list of integers, iterates through each element,
    doubles its value, updates the list with the new values, and prints the updated list.
    """

    numbers: list[int] = [1, 2, 3, 4]
    
    for i, num in enumerate(numbers):
        numbers[i] = num * 2

    print(numbers) 


if __name__ == '__main__':
    main()