# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 9 - Beginner - Dictionaries, Nesting and the Secret Auction


# Dictionaries have Keys (like words in a dictionaries), and Values (like the difinition), {Key: Value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Enter the key to retrieve the corresponding value in a dictionary
print(programming_dictionary["Bug"])

print(type(programming_dictionary))

# To add to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(f"programming_dictionary = {programming_dictionary}")

empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(f"programming_dictionary = {programming_dictionary}")

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(f"programming_dictionary = {programming_dictionary}")

# Loop through a dictionary
print("For loop output:")
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Lists and other dictionaries can be stored as a value in a dictionary

# Lists nested inside the dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Challenge: print Lille
print(travel_log["France"][1])

# 2D list, challenge: print D
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Challenge: print Stuttgart
travel_log_nested = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
print(travel_log_nested["Germany"]["cities_visited"][2])
