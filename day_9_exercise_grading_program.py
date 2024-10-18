# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 9 - Beginner - Coding Exercise

# Grading Program

# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 

# Write a program that converts their scores to grades.

# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values. 

# The final version of the student_grades dictionary will be checked. 

# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary. 

# This is the scoring criteria: 
# - Scores 91 - 100: Grade = "Outstanding" 
# - Scores 81 - 90: Grade = "Exceeds Expectations" 
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail" 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    score = student_scores[name]
    if score <= 70:
        student_grades[name] = "Fail"
    elif score <= 80 and score > 70:
        student_grades[name] = "Acceptable"
    elif score <= 90 and score > 80:
        student_grades[name] = "Exceeds Expectations"
    elif score <= 100 and score > 91:
        student_grades[name] = "Outstanding"
    else:
        print("Oops, grade error?!")

print(student_grades)