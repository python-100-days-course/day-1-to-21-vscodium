# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 9 - Beginner - Scope and Number Guessing Game

# Local scope vs global scope

# Global scope
player_health = 10
potion_strength = 4

# Local scope, potion_strength is only available inside the function
def drink_potion():
    potion_strength = 2 # local variable, it's best practice to keep local and global variables with different names
    print(f"potion_strength = {potion_strength}, local to drink_potion()")


# print(potion_strength) # 'potion_strength' is not defined, since it's not a global variable
drink_potion()
print(f"potion_strength = {potion_strength}, global variable")
print(player_health) # works, since variable has a global scope

# Namespace (anything named) is has scope

# There is no Block Scope in Python! (some other languages do) Blocks are anything indented like if, for, while, etc. Only functions have local scope.
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

# Example of a Block:
if game_level < 5:
    new_enemy = enemies[0]

# Variable is still accessible even though defined inside a block (if statement in this case)
print(new_enemy) # note: variable might undefined if the if statement is not met, so this is not great code, can be defined beforehand

# Modifying variables with global scope inside a function, not best practice
def increase_enemies():
    global enemies # allows global scope variables to be used inside a function, not good practice to do this, can create bugs
    enemies.append("Sorcerer") # add an enemy
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Modifying variables with global scope inside a function, this is the proper way to do it
def increase_enemies_2(enemy):
    enemy.append("Snake") # add an enemy
    return enemy

print(f"enemies outside function: {increase_enemies_2(enemies)}")

# Python constants and global scope
# It's acceptable to use global constants in functions with "global"
PI = 3.15159 # constants are all uppercase
GOOGLE_URL = "https://www.google.com"
# example:
def calc():
    global PI # this is ok
    num = PI * 7
    print(f"PI * 7 = {num}")
calc()