# LESSON 8 DAY 3 - ODD OR EVEN

# Which number do you want to check?
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

remainder = number % 2 # modulo calculates remainder of a division
if remainder == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#print(str(remainder))