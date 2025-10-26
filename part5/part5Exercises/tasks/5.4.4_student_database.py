"""
5.4.4 Student database

In this exercise you will write a simple student database. Before attempting this 
exercise, please complete exercise 5.3.8 Movie database, which is a similar task.

Please write a function named add_student(database: dict, name: str), which adds a 
student to a database.

Also write a function named add_course(database: dict, name: str, course: tuple), 
which adds a completed course to the record of a student in the database.

The course is a tuple consisting of the name of the course and the grade:

    course = ("Introduction to Programming", 5)

The database is a dictionary, where the keys are the names of the students. The 
values are dictionaries with the following structure:

    {
        "completed_courses": [(course1), (course2), ...],
        "credits": total_credits,
        "gpa": grade_point_average
    }

You should also write the functions print_student(database: dict, name: str) and 
summary(database: dict).

Example:
    database = {}
    add_student(database, "Peter")
    add_course(database, "Peter", ("Introduction to Programming", 5))
    add_course(database, "Peter", ("Advanced Course in Programming", 4))
    add_course(database, "Peter", ("Data Structures and Algorithms", 3))
    
    print_student(database, "Peter")

Expected output:
    Peter:
     3 completed courses, grade average 4.0
     Introduction to Programming 5
     Advanced Course in Programming 4
     Data Structures and Algorithms 3

Example of summary:
    summary(database)

Expected output:
    students 1
    most courses completed 3 Peter
"""

# TODO: Implement your solution below this line

