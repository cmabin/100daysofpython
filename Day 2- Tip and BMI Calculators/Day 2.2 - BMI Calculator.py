# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Angela's Solution
#weight_as_int = int(weight)
#height_as_float = float(height)

#Variables
height = float(height)
weight = int(weight)

#Using exponent operator
#bmi = weight_as_int / height_as_float ** 2

bmi = int(weight) / float(height) ** 2

#Multiplication and PEMDAS
#bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)


print(bmi_as_int)