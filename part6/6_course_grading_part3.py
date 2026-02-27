"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part6 (if needed)

NB: This task is optional and not graded, but you can still check it using: python grade_part6.py

Course grading, part 3

This exercise will continue from the previous one. Now we shall print out some statistics 
based on the CSV files.

Sample output:
Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv
name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade   
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3

Each row contains the information for a single student. The number of exercises completed, 
the number of exercise points awarded, the number of exam points awarded, the total number 
of points awarded, and the grade are all displayed in tidy columns. The width of the column 
for the name should be 30 characters, while the other columns should be 10 characters wide.
"""

# TODO: Implement your solution below
def calculate_grade(total_points):
    pass

if False:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    student_info = "students.csv"
    exercise_data = "exercises.csv"
    exam_data = "exam.csv"

# Read students, exercises, and exam data
# Calculate grades and print results



# Save your file and run it using: python 6_course_grading_part3.py
# Check: python grade_part6.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 6"         (commit with message)
# 3. git push                                      (push to GitHub)
