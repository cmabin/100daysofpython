from typing import ValuesView


# Dictionaries = Keys and Values

# {Key: Value}
# Bug, An error in a program that prevents the program from running as expected.

# Creating a dictionary

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.", 
    }

# Retrieving items from dictionary

# print(programming_dictionary["Bug"])

# Adding items to dictionary later

programming_dictionary["Loop"] = "The action of doing something again and again."
# print(programming_dictionary)

# Creating empty dictionaries

empty_dictionary = {}

# Wipe existing dictionary

# programming_dictionary = {}

# Edit dictionary items

programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# Looping through a dictionary

for key in programming_dictionary :
    print(key)
    print(programming_dictionary[key])

# Nesting

# {key: [list] key2: {dict}}

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lillie", "Dijon"]
}

# Nest a dict in a dict.

travel_log = {
    "France": {"cities_visited": ["Paris", "Lillie", "Dijon"], "total_visits": 12},
    "USA": {"cities_visited": ["Honolulu", "Kansas City", "Bakersfield"], "total_visits": 3}
}

# Nest dict in a list

# [{
#   key: [list],
#   key2:{dict},
# }
# {
#   key: value,
#   key2: value,
# }]

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lillie", "Dijon"], 
        "total_visits": 12
    },
    {
        "country":"USA",
        "cities_visited": ["Honolulu", "Kansas City", "Bakersfield"], 
        "total_visits": 3
    }
]
