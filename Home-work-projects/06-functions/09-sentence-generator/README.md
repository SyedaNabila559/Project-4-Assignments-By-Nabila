# 9.📝 Sentence Maker Program
# Description 📜
This Python program generates sentences based on a word and its part of speech (noun, verb, or adjective). The user will input a word and specify whether it's a noun, verb, or adjective, and the program will create a sentence using that word.

# Features 🎯
Word Input: The program prompts the user to input a word.

Part of Speech Selection: The user specifies whether the word is a noun, verb, or adjective.

Sentence Creation: Based on the part of speech, the program generates a sentence using the word provided.

Validation: The program checks if the part of speech is valid (0 for noun, 1 for verb, 2 for adjective).

# How It Works 🔄
Word Input: The user is asked to input a word they want to use in a sentence.

Part of Speech Selection: The user specifies if the word is a noun, verb, or adjective.

Output: The program prints a sentence using the word based on its part of speech.

# Example Output:

Please type a noun, verb, or adjective: happiness
Is this a noun, verb, or adjective?
Type 0 for noun, 1 for verb, 2 for adjective: 0
I am excited to add this happiness to my vast collection of them!
# Example Runs:
When entering a noun:


Please type a noun, verb, or adjective: apple
Is this a noun, verb, or adjective?
Type 0 for noun, 1 for verb, 2 for adjective: 0
I am excited to add this apple to my vast collection of them!
When entering a verb:


Please type a noun, verb, or adjective: run
Is this a noun, verb, or adjective?
Type 0 for noun, 1 for verb, 2 for adjective: 1
It's so nice outside today it makes me want to run!
When entering an adjective:


Please type a noun, verb, or adjective: beautiful
Is this a noun, verb, or adjective?
Type 0 for noun, 1 for verb, 2 for adjective: 2
Looking out my window, the sky is big and beautiful!
When entering an invalid part of speech:


Please type a noun, verb, or adjective: fun
Is this a noun, verb, or adjective?
Type 0 for noun, 1 for verb, 2 for adjective: 3
Part of speech must be 0, 1, or 2! Can't make a sentence.

# Code Explanation 🧑‍💻
make_sentence(word, part_of_speech)
This function takes two parameters:

word (the word to be used in the sentence)

part_of_speech (the category of the word: 0 for noun, 1 for verb, 2 for adjective)

It checks the part_of_speech and generates a sentence accordingly.

If the part of speech is invalid (not 0, 1, or 2), it returns an error message.

main()
The main function prompts the user to input a word and select its part of speech.

It then calls the make_sentence() function to generate and print a sentence based on the word.