#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

coinflip = random.randint(0, 1)

if coinflip == 0 :
  print("Heads.")
else :
  print("Tails.")