# LESSON 15 DAY 4 - TREASURE MAP

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# Note:
# A, B, C = column
# 1, 2, 3 = row
# Example: A3 is 1st column, 3rd row

# Obtain vertical map index
vertical_position = int(position[1]) - 1

# Obtain horizontal map index
if position[0] == "A":
  horizontal_position = 0
elif position[0] == "B":
  horizontal_position = 1
elif position[0] == "C":
  horizontal_position = 2
else:
  print("error")

# Placing X inside the map
map[vertical_position][horizontal_position] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")