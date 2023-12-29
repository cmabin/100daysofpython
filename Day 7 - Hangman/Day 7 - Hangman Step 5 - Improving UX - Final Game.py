# Step 5
import os 
clear = lambda: os.system('cls')
import random

import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art
print(hangman_art.logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    # If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in display:
        print(f"You've alredy guessed {guess}.")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            print(f"Correct!")
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"Sorry, but {guess} isn't in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"That's it, game over. The word was {chosen_word}.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win! That was the word!")

    # Import the stages from hangman_art.py and make this error go away.
    import hangman_art
    print(hangman_art.stages[lives])