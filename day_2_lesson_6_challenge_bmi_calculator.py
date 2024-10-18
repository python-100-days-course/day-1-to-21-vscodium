# LESSON 6 DAY 2 - BMI CALCULATOR:

# 1st input: enter height in meters e.g: 1.65
height = input("enter height in meters, e.g 1.65: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("enter weight in kilograms, e.g 72: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

height_float = float(height)
weight_float = float(weight)
bmi = int(weight_float / height_float ** 2) #calculate BMI and make the number whole
bmi_str = str(bmi) #convert floating number to string
print(f"BMI = {bmi_str}")