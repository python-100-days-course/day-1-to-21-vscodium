# LESSON 14 DAY 4 - BANKER ROULETTE
 This code needs to be fixed, names_string should be defined

names = names_string.split(", ")
# names_string contains the input values provided.
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

names_length = len(names) - 1 # list index starts with 0
random_name_num = random.randint(0, names_length) # select a radom name
print(f"{names[random_name_num]} is going to buy the meal today!") # prints