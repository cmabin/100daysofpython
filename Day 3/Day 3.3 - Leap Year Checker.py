# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

divide4 = year % 4
divide100 = year % 100
divide400 = year % 400

if divide4 == 0 and divide100 >= 0 and divide400 >= 0 :
  print("Leap year.")
else :
  print("Not a leap year.")

# if year % 4 == 0 :
#   if year % 100 == 0 :
#     if year % 400 == 0 :
#       print("Leap year.")
#     else :
#       print("Not leap year.")
#   else :
#     print("Leap year.")
# else :
#   print("Not leap year.")

