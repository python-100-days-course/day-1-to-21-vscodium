# LESSON 12 DAY 3 - LOVE CALCULATOR:

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name1 = name1.lower() # convert all letters to lower case
name2 = name2.lower()
bothnames = name1 + name2

# determine how many times each letter is present
digit1 = bothnames.count("t") + bothnames.count("r") + bothnames.count("u") + bothnames.count("e")
#print(f"digit1 = {digit1}") # for checking
digit2 = bothnames.count("l") + bothnames.count("o") + bothnames.count("v") + bothnames.count("e")
#print(f"digit2 = {digit2}") # for checking

# convert int to str
digit1 = str(digit1)
digit2 = str(digit2)
#print(type(digit1)) # check class

score = digit1 + digit2 # combine digits as a string
score = int(score) # convert back to integer

# determine which message to print based on score
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
