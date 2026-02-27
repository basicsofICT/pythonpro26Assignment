"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part6 (if needed)

6.2.4 Store personal data

Please write a function named store_personal_data(person: tuple), which takes a tuple 
containing some identifying information as its argument.

The tuple contains the following elements:
• Name (string)
• Age (integer)
• Height (float)

This should be processed and written into the file people.csv. The file may already contain 
some data; the new entry goes to the end of the file. The data should be written in the 
format:

name;age;height

Each entry should be on a separate line. If we call the function with the argument 
("Paul Paulson", 37, 175.5), the function should write this line to the end of the file:

Paul Paulson;37;175.5
"""

# TODO: Implement your solution below
def store_personal_data(person: tuple):
    pass

# if __name__ == "__main__":
#     store_personal_data(("Paul Python", 42, 178.5))

# Save your file and run it using: python 13_store_personal_data.py
# Check: python grade_part6.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 13"         (commit with message)
# 3. git push                                      (push to GitHub)
