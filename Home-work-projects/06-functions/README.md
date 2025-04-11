# 🚀 Functions in Python
# 00_averages - 📊 Calculating the Average
This program calculates the average of a set of numbers. It likely takes a list of values, sums them up, and divides by the count to return the average. Useful for computing statistics!

# Example:

numbers = [10, 20, 30, 40]
average = sum(numbers) / len(numbers)
print(f"The average is {average}")

# 01_chaotic_counting - 🔢 Randomized Counting
A function that counts numbers in a chaotic or random manner. Instead of a normal sequence (1, 2, 3...), it might skip numbers, introduce delays, or shuffle the order.

# Example:

import random
def chaotic_counting():
    for i in range(10):
        if random.random() < 0.3:
            continue  # Skip numbers randomly
        print(i)

# 02_count_even - ⚖️ Counting Even Numbers
This function counts how many even numbers exist in a given list or range. It checks each number using num % 2 == 0 and keeps track of the total count.

# Example:

numbers = [1, 2, 3, 4, 5, 6]
even_count = sum(1 for num in numbers if num % 2 == 0)
print(f"There are {even_count} even numbers.")

# 04_double - ✖️ Doubling a Number Until a Limit
Takes a starting number and keeps doubling it until it reaches a set limit (like 100). A great example of exponential growth in action!

# Example:

num = 1
while num <= 100:
    print(num)
    num *= 2  # Double the number each time

# 05_get_name - ✍️ User Input for Name
A simple function that asks the user for their name. It may also check for proper capitalization or prevent empty input before returning a valid name.

# Example:

name = input("What is your name? ")
if name.strip() == "":
    print("Name cannot be empty!")
else:
    print(f"Hello, {name}!")

# 06_is_odd - 🔄 Checking for Odd Numbers
This function determines if a number is odd. It returns True if num % 2 != 0 and False otherwise. Handy for filtering odd numbers in a dataset!

# Example:

def is_odd(num):
    return num % 2 != 0

print(is_odd(5))  # True
print(is_odd(4))  # False

# 07_print_divisor - ➗ Finding Divisors of a Number
Given an input number, this function prints all its divisors by checking which values evenly divide the number (num % i == 0).

# Example:

num = 12
for i in range(1, num+1):
    if num % i == 0:
        print(f"{i} is a divisor of {num}")

# 08_print_multiple - 🔢 Printing Multiples of a Number
Takes a base number and prints its multiples up to a certain limit. Useful for multiplication tables or finding common multiples!

# Example:

def print_multiples(num, limit):
    for i in range(1, limit+1):
        print(f"{num} x {i} = {num * i}")

print_multiples(5, 10)

# 09_sentence_generator - 📝 Generating Random Sentences
This function constructs random or structured sentences. It may use predefined lists (nouns, verbs, adjectives) to generate meaningful or funny phrases.

# Example:

import random

def sentence_generator():
    nouns = ["dog", "cat", "fish"]
    verbs = ["runs", "jumps", "swims"]
    adjectives = ["quick", "lazy", "cute"]
    
    sentence = f"The {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)}."
    print(sentence)

sentence_generator()

# 10_print_ones_digit - 🔟 Extracting the Last Digit
A function that prints the last digit (ones place) of a given number. It achieves this using num % 10, isolating the final digit.

# Example:

def print_ones_digit(num):
    print("The ones digit is", abs(num) % 10)

print_ones_digit(12345)  # Output: 5
print_ones_digit(-6789)  # Output: 9

# Usage 🎯
To run any of these functions, simply execute the respective code in your Python environment. Feel free to modify or extend the functionality based on your needs! ✨

