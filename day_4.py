# Day 4 - 4/04/2024

# Radomisation and Python Lists - Beginner

import random
import day_4_module # custom module

random_integer = random.randint(1, 10) #generates a random number between 1 and 10, including 1 and 10
print(f"random_integer = {random_integer}")

print(f"day_4_module.pi = {day_4_module.pi}") # prints value of variable pi defined in the custom module

random_float = random.random() # outputs a random floating number between [0, 1), doesn't include 1
print("random_float = " + str(random_float))

random_float2 = random.random() * 5 # outputs a random floating number between [0, 5), doesn't include 5 (4.999999...)
print("random_float2 = " + str(random_float2))

# fruits = ["apple", "banana", "kiwi"] # list with items, mixed types are allowed
# print(fruits[0]) # prints the 1st item in the list
# fruits.append("pear") # add an item to end of the list
# print(fruits[-1]) # prints the last item in the list

# nested lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(f"dirty_dozen = {dirty_dozen}")
print(dirty_dozen[0][0]) # prints 1st item in the 1st list


