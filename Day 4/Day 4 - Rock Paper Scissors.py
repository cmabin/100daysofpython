rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Store user input
images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors? \n"))
if choice >= 3 or choice < 0 :
  print("You typed an invalid number, you lose!")
else :
  print("You chose:")
  print(images[choice])

# Generate random choice
  import random
  its_choice = random.randint(0, 2)
  print("I chose:")
  print(images[its_choice])

# Compare input and give result

# if choice == 0 :
#   print(f"You picked Rock. \n{rock}") # or {images[choice]}
# elif choice == 1 :
#   print(f"You picked Paper. \n{paper}")
# elif choice == 2 :
#   print(f"You picked Scissors. \n{scissors}")

# if its_choice == 0 :
#   print(f"I picked Rock. \n{rock}")
# elif its_choice == 1 :
#   print(f"I picked Paper.\n{paper}")
# elif its_choice == 2 :
#   print(f"I picked Scissors. \n{scissors}")

# if choice >= 3 or choice < 0 :
#   print("You typed an invalid number, you lose!")
  if choice == 0 and its_choice == 2 :
    print("You win.")
  elif its_choice == 0 and choice == 2 :
    print("You lose.")
  elif choice < its_choice :
    print("You lose.")
  elif choice > its_choice :
    print("You win.")
  elif choice == its_choice :
    print("It's a tie.")
