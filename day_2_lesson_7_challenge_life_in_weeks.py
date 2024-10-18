# LESSON 7 DAY 2 - LIFE IN WEEKS:

age = input("enter age: ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

years_left = 90 - int(age) # years left to live assuming living to 90
weeks_left = years_left * 52 # convert to weeks left to live
print(f"You have {weeks_left} weeks left.")