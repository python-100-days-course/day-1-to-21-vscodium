# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 5 - Beginner - Python Loops

# For loop
fruits = ["Apple", "Mango", "Kiwi"]
for fruit in fruits:
    print(fruit)

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

total_exam_score = sum(student_scores)
print(f"total_exam_score = {total_exam_score}")

#for loop for simple sum function
total_exam_score_2 = 0
for score in student_scores:
    total_exam_score_2 += score
print(f"total_exam_score_2 = {total_exam_score_2}")

print(f"Max of student_scores list = {max(student_scores)}")

# Range function with for loop
# note: last number is not printed, (from, to, step)
for number in range (1, 8, 3):
    print(number)

#challenge, add numbers from 1 to 100:
total = 0
for number in range (1, 101):
    total += number
print(f"total = {total}")
