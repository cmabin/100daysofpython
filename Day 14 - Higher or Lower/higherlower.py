# Import art, game_data, random module
import os
from art import logo, vs
from game_data import data
import random
clear = lambda: os.system('cls')


"""Make the data into a printable format with the name, description, and country"""
def format_data(compare)    :
    compare_name = compare["name"]
    compare_desc = compare["description"]
    compare_country = compare["country"]
    return(f"{compare_name}, a {compare_desc} from {compare_country}.")

"""Using an if statement to check if the user is correct"""
def check_guess(player_guess, first_follower, second_follower)  :
    if first_follower > second_follower : 
        return player_guess == "a"
    else    :
        return player_guess == "b"
    

# Show "Higher Lower" art, set the score to zero, add a condition to continue the game
print(logo)
player_score = 0
continue_game = True
# Create a random account from game_data
second_compare = random.choice(data)

# Make repeatable
while continue_game :

    # Move correct answer to B from A
    first_compare = second_compare
    second_compare = random.choice(data)

    if first_compare == second_compare  :
        second_compare = random.choice(data)

    # Show first_compare, vs. art, and second_compare
    print(f"Compare A: {format_data(first_compare)}")
    print(vs)
    print(f"With B: {format_data(second_compare)}")

    # Have user guess which has more followers
    player_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Compare the players answer
    ## Get the follower count of each comparison
    first_follower = first_compare["follower_count"]
    second_follower = second_compare["follower_count"]
    correct_guess = check_guess(player_guess, first_follower, second_follower)

    # Clear the screen in between guesses
    clear()
    print(logo)

    # Give the user feedback
    if correct_guess    :
        player_score += 1
        print(f"Correct! Your current score is {player_score}.")
    else    :
        continue_game = False
        print(f"Sorry, that's incorrect. Your final score is {player_score}.")