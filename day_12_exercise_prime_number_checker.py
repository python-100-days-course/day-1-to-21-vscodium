# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 12 - Beginner - Coding Exercise
# Your code passed this test

# Prime Number Checker
# Prime numbers are numbers that can only be cleanly divided by themselves and 1. Wikipedia  
# You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  It should return True or False.

# e.g.
# 7 is a primer number because it is only divisible by 1 and itself.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# Note: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.

# Example Input 1
# 73

# Example Output 1
# True

# Example Input 2
# 75

# Example Output 2
# False

def is_prime(num):
    i = 0 # divisible by number counter
    for n in range(1, num+1):
        if num % n == 0:
            i += 1
    if i == 2:
        return True # it's a prime number
    else:
        return False # not a prime number

keep_going = True
while keep_going:
    number = int(input("Check if number is a prime number: "))
    print(is_prime(number))
    another_num = input("Check another number? 'y' or 'n': ")
    if another_num == "n":
        keep_going == False
