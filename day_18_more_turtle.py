# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 18 - Intermediate - Python Turtle Package Exploration

# from turtle import Turtle, Screen
import random
# from turtle import * # can be used to import everything, but it's typically avoided because it can be a bit confused
import turtle as t # alias name t can then be used instead of turtle

timmy = t.Turtle()
timmy.shape("turtle")
# timmy.color("blue")

# # Draw a square:
# for n in range(1, 5):
#     timmy.forward(100) # move forward by 100 units
#     timmy.right(90) # turn right (clockwise) 90deg

# # Draw a dashed line:
# for _ in range(15):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# # Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon with random colors, each side is 100 units:
# # 3 sides to 10 sides
#
# def change_color():
#     r = random.random() # each RGB color value is 0 to 1
#     g = random.random()
#     b = random.random()
#     timmy.color(r,g,b)
#     # print(f"RGB = {r}, {g}, {b}") # checking
#
# timmy.pendown() # make sure timmy is drawing
# for n in range(3, 11):
#     angle = 360 / n
#     change_color()
#     for _ in range(n):
#         timmy.forward(100)
#         timmy.right(angle)

# # Random walk, random color, also make lines thicker and speed-up:
# def change_color():
#     r = random.random() # each RGB color value is 0 to 1
#     g = random.random()
#     b = random.random()
#     timmy.color(r,g,b)
#     # print(f"RGB = {r}, {g}, {b}") # checking
#
# def change_direction():
#     random_dir = random.randint(0,3)
#     timmy.setheading(random_dir*90)
#
# timmy.speed(3)
# timmy.width(10)
#
# timmy.pendown() # make sure timmy is drawing
# for _ in range(200):
#     change_color()
#     timmy.forward(50)
#     change_direction()

# # Random color and tuple
# t.colormode(255)
# def change_color():
#     r = random.randint(0, 255) # each RGB color value is 0 to 255 (standard)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color_tuple = (r, g, b)
#     timmy.color(random_color_tuple)
#
# def change_direction():
#     random_dir = random.randint(0,3)
#     timmy.setheading(random_dir*90)
#
# timmy.speed(3)
# timmy.width(10)
#
# timmy.pendown() # make sure timmy is drawing
# for _ in range(200):
#     change_color()
#     timmy.forward(50)
#     change_direction()

# Make a spirograph:
t.colormode(255)
def random_color():
    r = random.randint(0, 255) # each RGB color value is 0 to 255 (standard)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_tuple = (r, g, b)
    timmy.color(random_color_tuple)

timmy.speed("fastest")
timmy.width(2)

deg_delta = 5
for deg in range(0, 360, deg_delta):
    random_color()
    timmy.setheading(deg)
    timmy.circle(200)

# for window, should be at the bottom
screen = t.Screen()
screen.exitonclick()