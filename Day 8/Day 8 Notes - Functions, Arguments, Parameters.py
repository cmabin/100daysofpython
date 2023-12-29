# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet() :
#     print("Hello")
#     print("Hi There")
#     print("How are you?")

# greet()

# Function that allows for input

# def greet_with_name(name) :
#     print(f"Hello {name}")
#     print(f"Hi There {name}")

# greet_with_name("Cee-Jay")

# Functions with more than one input
def greet_with(name, location) :
    print(f"Hello {name}")
    print(f"How's the weather in {location} today?")

# name = input("What's your name? ")
# location = input("Where are you from? ")

greet_with(name="Cee-Jay", location="Philadelphia")

# Functions with keyword arguments
# greet_with()