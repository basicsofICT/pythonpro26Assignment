"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part6 (if needed)

6.2.3 Filtering the contents of a file

The file solutions.csv contains some solutions to mathematics problems:

Arto;2+5;7
Pekka;3-2;1
Erkki;9+3;11
Arto;8-3;4
Pekka;5+5;10
...jne...

As you can see above, on each line the format is name_of_student;problem;result. All the 
operations are either addition or subtraction, and each has exactly two operands.

Please write a function named filter_solutions() which:
• Reads the contents of the file solutions.csv
• writes those lines which have a correct result into the file correct.csv
• writes those lines which have an incorrect result into the file incorrect.csv

The function should have the exact same result, no matter how many times it is called.

Sample output:
>>> filter_solutions()
(The function doesn't return or print anything, but creates/updates correct.csv and incorrect.csv)
"""

# TODO: Implement your solution below
def filter_solutions():
    pass

# if __name__ == "__main__":
#     filter_solutions()

# Save your file and run it using: python 12_filtering_contents.py
# Check: python grade_part6.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 12"         (commit with message)
# 3. git push                                      (push to GitHub)
