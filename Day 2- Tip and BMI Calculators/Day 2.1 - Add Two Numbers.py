# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Check the data type
print(type(two_digit_number))

#Get the first and second digits via subscript, can convert string to int here also.
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

# Add them together
result = int(first_digit) + int(second_digit)

print(result)