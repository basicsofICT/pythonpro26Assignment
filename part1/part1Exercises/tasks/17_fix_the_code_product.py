"""
Quick Start: Terminal (Ctrl+`) | pwd (check location) | cd part1/part1Exercises/tasks (if needed)
Run: python 17_fix_the_code_product.py | Check: python grade_part1.py

Programming exercise: Fix the Code - Product

This program is supposed to ask for three numbers and then print out their product. 
Please fix the program so that it works correctly.

Sample output:
Please type in the first number: 2
Please type in the second number: 4
Please type in the third number: 5
The product is 40
"""

# Fix the code below
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 + number2 + number3

print("The product is", product)
