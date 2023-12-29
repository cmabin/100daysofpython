import random
from cities import cities

import os 
clear = lambda: os.system('cls')


print("Welcome to Dad's Travel Advisory Co.! Let's take a trip.")




# Select three cities at random from the list.
first_list = random.choices(cities, k = 3)
print(first_list)

# Ask 

print("Here are three cities I've picked for you to travel.")
