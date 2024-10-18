# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 8 - Beginner - Function Parameters and Caesar Cipher

# function with a parameter of name
def greet(name):
    print(f"Hey {name}!")
    print(f"How is it going {name}?")
# an argument "John" is passed to the fucntion
greet("John")

# Coding Exercise 7: Life in Weeks
def life_in_weeks(age):
    weeks_left = (90 - age)*52
    print(f"You have {weeks_left} weeks left.")
age_num = int(input("How old are you?\n"))
life_in_weeks(age_num)

# Lesson 62 challenge, multiple parameters:
def greet_with(name, location):
    print(f"Hi {name}.")
    print(f"What is it like in {location}?")
# Positional Arguments:
greet_with("Alex", "Japan")
# Keyword Arguments, order doesn't matter:
greet_with(location="Black Hole", name="Sam")

