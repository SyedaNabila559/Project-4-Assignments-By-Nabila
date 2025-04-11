# 1.🔢 Chaotic Counting Game 🎲
# Description 📜
This Python program counts from 1 to 10, but with a twist! The function may stop at any time, randomly, before reaching 10. The stopping condition is based on a random chance, meaning it could stop at any moment during the count, or it might count all the way to 10. The chance of stopping is defined by the probability constant DONE_LIKELIHOOD.

# Features 🎯
Starts counting from 1 to 10.

Has a chance to stop randomly based on a probability.

Prints numbers until it either reaches 10 or decides to stop early.

A fun, unpredictable count!

# How It Works 🔄
The program starts counting from 1.

With each number, there is a 20% chance (controlled by DONE_LIKELIHOOD) that the program will decide to stop counting.

If the program reaches 10 without stopping, it finishes normally.

If the program stops early, the count halts before reaching 10.

# Example Output 🖥️

I'm going to count until 10 or until I feel like stopping, whichever comes first.
1
2
3
I'm done
In this case, the program stopped at 3 due to the random chance.