# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 5 - Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_total = nr_letters + nr_symbols + nr_numbers

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

letters_i_max = len(letters) - 1
numbers_i_max = len(numbers) - 1
symbols_i_max = len(symbols) - 1

pwd_letters = ""
for n in range(1, nr_letters + 1):
    random_letter = letters[random.randint(0, letters_i_max)]
    # print(random_letter) #for checking
    pwd_letters = pwd_letters + random_letter
    # print(pwd_letters) #for checking
# print(pwd_letters) #for checking

pwd_symbols = ""
for n in range(1, nr_symbols + 1):
    random_symbol = symbols[random.randint(0, symbols_i_max)]
    # print(random_symbol) #for checking
    pwd_symbols = pwd_symbols + random_symbol
    # print(pwd_symbols) #for checking
# print(pwd_symbols) #for checking

pwd_numbers = ""
for n in range(1, nr_numbers + 1):
    random_number = numbers[random.randint(0, numbers_i_max)]
    # print(random_number) #for checking
    pwd_numbers = pwd_numbers + random_number
    # print(pwd_numbers) #for checking
# print(pwd_numbers) #for checking

password_easy = pwd_letters + pwd_symbols + pwd_numbers
print(f"password_easy = {password_easy}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password_easy_new = password_easy[1:nr_total] #removes 1st letter in the word
# print(password_easy_new)
# print("\n\nHard Level - Order of characters randomised")

password_hard = ""
password_easy_mod = password_easy # changes with each loop
nr_total_var = nr_total # changes with each loop
# print(f"nr_total = {nr_total}") # for checking
for n in range(1, nr_total + 1):
    # print(f"n = {n}") # for checking
    # print(f"nr_total_var = {nr_total_var}") # for checking
    random_character_num = random.randint(0, nr_total_var-1)
    random_character = password_easy_mod[random_character_num]
    password_hard = password_hard + random_character
    # this logic removes the random_character from password_easy_mod
    if random_character_num == 0: # if 1st character needs to be removed
        password_easy_mod = password_easy_mod[1:nr_total_var]
    elif random_character_num == nr_total_var: # if last character needs to be removed
        password_easy_mod = password_easy_mod[0:nr_total_var-1]
    else: # if middle character needs to be removed
        password_easy_mod = password_easy_mod[0:random_character_num] + password_easy_mod[random_character_num+1:nr_total_var]
    nr_total_var = nr_total_var - 1
    # print(f"random_character_num = {random_character_num}") # for checking
    # print(f"random_character = {random_character}") # for checking
    # print(f"password_easy_mod = {password_easy_mod}") # for checking
    # print(f"password_hard = {password_hard}") # for checking

print(f"password_hard = {password_hard}")