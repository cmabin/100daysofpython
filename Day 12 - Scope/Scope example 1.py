# ################### Scope ####################

# Modifying Global Scope

# enemies = 1 #   Global

# def increase_enemies(): #   Local
#     return enemies + 1
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local Scope - Exists within functions


# def drink_potion()  :
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

# Global Scope - Where you define (create) a function
# player_health = 10

# def drink_potion()  :
#     potion_strength = 2
#     print(player_health)

# drink_potion()

#   Namespace = Anything named/defined by the user. Ex: player_health, def drink_potion()

#   Block Scope - None in Python

# game_level = 3
# def create_enemy()  :
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5   :
#         new_enemy = enemies[0]

#     print(new_enemy)

# Global Constants - Values that remain unchanged. Uppercase, underscored
