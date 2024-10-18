# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 16 - Intermediate - Object Oriented Programming (OOP)

# Procedural Programming (most done up until now) vs Object Oriented Programming (OOP)

# Older languages like Fortran and Cobol used mostly procedural programming

# OOP:

# Objects have attributes (what it has, like variables) and methods (what it does, like functions)

# Class is a blueprint from which other objects can be generated.

# Class: is written in Pascal case, 1st letter of word capitalized

# Note: "Turtle" package doesn't work in VSCodium?
from turtle import Turtle, Screen

timmy = Turtle() # Assigned Turtle class to timmy, making an object
print(timmy)
timmy.shape("turtle")
timmy.color("DarkMagenta")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight) # Prints an attribute canvheight of my_screen object
my_screen.exitonclick() # Method exitonclick of my_screen object is triggered, will exit the screen when it's clicked

