# Create Logo.
from art import logo

# Have CPU think of a number 1-100.
from random import randint

# Set turns.
easy_turns = 10
hard_turns = 5
turns = 0

# Choose difficulty.
def difficulty()    :
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy"  :
        return easy_turns
    else    :
        return hard_turns

# Check the guess.
def check_guess(player_number, cpu_number, turns)  :
    """Checks player_number against cpu_number. Returns number of turns remaining."""
    if player_number > cpu_number :
        print("Too high. Guess again.")
        return turns - 1
    elif player_number < cpu_number   :
        print("Too low. Guess again.")
        return turns - 1
    else  :
        print(f"You got it! The number was {cpu_number}.")

def play_game() :
# Choosing between 1 and 100
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    cpu_number = randint(1, 100)
    print(f"Psst! The answer is {cpu_number}.")

    turns = difficulty()

    # Repeat guess function if user gets it wrong.
    player_number = 0
    while player_number != cpu_number:
        print(f"You have {turns} chances left.")
        # User guesses a number
        player_number = int(input("Make a guess: "))
        turns = check_guess(player_number, cpu_number, turns)
        if turns == 0   :
            print("You've run out of guesses. You lose.")
            return
play_game()