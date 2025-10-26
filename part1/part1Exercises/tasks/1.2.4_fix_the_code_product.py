"""
Programming exercise: Fix the Code - Product

Fix this broken program so that it correctly multiplies three numbers and prints the product.

Sample output:
    Please type in a number: 2
    2 x 5 x 8 = 80
"""

# TODO: Write your solution below this line
# Save your file and run it using: python 1.2.4_fix_the_code_product.py
"""
    Please type in the second number: 3
    Please type in the third number: 5
    The product is 30
"""

# Fix the code below
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 + number2 + number3

print("The product is", product)
