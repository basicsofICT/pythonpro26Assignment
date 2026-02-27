"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part6 (if needed)
Run: python 6.3.2_parameter_validation.py | Check: python grade_part6.py

6.3.2 Parameter validation

Task: Write a function new_person(name: str, age: int) that validates parameters.
- Name must be non-empty, not all spaces, and max 40 characters
- Age must be between 0 and 150
- Raise ValueError with appropriate message if validation fails

Sample output:
>>> person = new_person("John", 25)
>>> print(person)
('John', 25)
>>> person = new_person("", 25)
ValueError: Invalid name
>>> person = new_person("John", 200)
ValueError: Invalid age
"""

def new_person(name: str, age: int) -> tuple:
    # TODO: Validate name (non-empty, not all spaces, max 40 chars)
    # TODO: Raise ValueError("Invalid name") if name is invalid
    # TODO: Validate age (0-150)
    # TODO: Raise ValueError("Invalid age") if age is invalid
    # TODO: Return tuple (name, age) if all valid
    pass

# Test cases for grader
# try:
#     person = new_person("John", 25)
#     print(person)
# except ValueError as e:
#     print(f"Error: {e}")

# try:
#     person = new_person("", 25)
#     print(person)
# except ValueError as e:
#     print(f"Error: {e}")

# try:
#     person = new_person("John", 200)
#     print(person)
# except ValueError as e:
#     print(f"Error: {e}")



# Save your file and run it using: python 18_parameter_validation.py
# Check: python grade_part6.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 18"         (commit with message)
# 3. git push                                      (push to GitHub)
