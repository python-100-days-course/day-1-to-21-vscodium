# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 5 - Lesson 39 - Challenge
# Goal: create a for loop for max function

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

max_student_score = 0
for score in student_scores:
    if score > max_student_score:
        max_student_score = score
print(f"max_student_score = {max_student_score}")