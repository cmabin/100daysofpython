print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇



choice1 = input("You're on the beach. Where do you want to go? Type 'Forest' or 'Shore': \n")
choice1 = choice1.lower()
if (choice1 == "forest") :
  choice2 = input("You found an old map. Pick it up? Type 'Yes' or 'No': \n")
  choice2 = choice2.lower()
  if (choice2 == "yes") :
      choice3 = input("You come to a fork in the road. Which way will you go? Type 'Left', 'Right', or 'Straight': \n")
      choice3 = choice3.lower()
      if (choice3 == 'left') :
        print("See, I knew you were smart! You follow the path into a cave where, deep inside, is a hot spring with... Is that... a beer mug? You grab the handle and take a sip, instantly feeling rejuvenated and ready to swim home!")
      elif (choice3 == 'straight') :
        print("The castle! You barge through the doors, fly like a gymnast past the poisonous dart and spear traps, and run into the treasure room!\nWhere an undead soldier adds your skull to his collection. Game over.")
      elif (choice3 == 'right') :
        print("Yeah... That part of the map is pretty faded... You couldn't see the drawing of the Lion, but you're dinner now. Game over.")
  else :
    print("I bet you wish you had that map, now that you're lost in the Forever Woods. Game over.")
else :
  print("Watch those random sinkholes... Game over.")
