#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
word_length = len(chosen_word)
for letter in chosen_word :
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

# Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# HARDEST PART!!! Best to use range function to get location of individual letters. - CM

for location in range(word_length):
    letter = chosen_word[location]
    if letter == guess:
        display[location] = letter

# Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".

print(display)