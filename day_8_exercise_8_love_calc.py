
# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 8 - Beginner - Exercise 8 - Love Calculator

# 💪 This is a difficult challenge! 💪 

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

# 2. Then check for the number of times the letters in the word LOVE occurs.   

# 3. Then combine these numbers to make a 2 digit number and print it out.  

true_str = "true"
love_str = "love"

def calculate_love_score(name1, name2):
    true_count = 0 # couldn't define outside the function?
    love_count = 0 # couldn't define outside the function?
    names_added = (name1 + name2).lower()
    for char in true_str:
        true_count += names_added.count(char)
    for char in love_str:
        love_count += names_added.count(char)
    # print(names_added) # check
    # print(f"true_count = {true_count}") # check
    # print(f"love_count = {love_count}") # check
    score = str(true_count) + str(love_count)
    print(f"Love Score = {score}")
calculate_love_score("Kanye West", "Kim Kardashian")

# # test1, works:
# def calculate_love_score(name1, name2):
#     names_added = (name1 + name2).lower()
#     true_count = names_added.count("t")
#     print(names_added)
#     print(f"true_count = {true_count}")
# calculate_love_score("Romeo", "Juliet")

# # test 2, works:
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# names_added = (name1 + name2).lower()
# for char in true_str:
#     true_count += names_added.count(char)
# for char in love_str:
#     love_count += names_added.count(char)
# print(names_added)
# print(f"true_count = {true_count}")
# print(f"love_count = {love_count}")