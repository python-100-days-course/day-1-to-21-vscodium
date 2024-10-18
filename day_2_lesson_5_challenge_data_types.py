# LESSON 5 DAY 2 - DATA TYPES:

two_digit_number = input("Please enter a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

two_digit_number_str = str(two_digit_number) #convert to string
two_digit_number_added = int(two_digit_number_str[0]) + int(two_digit_number_str[1]) #take 1st and 2nd digits, convert to integers then add
print(f"two_digit_number_added = {two_digit_number_added}") #answer