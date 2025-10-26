"""
Programming exercise: Loyalty Bonus

Calculate a loyalty bonus:
- Less than 100 points → 10% bonus
- 100 points or more → 15% bonus

Fix any issue that gives both bonuses.

Sample output:
    How many points are on your card? 55
    Your bonus is 10 %
    You now have 60.5 points
"""

# TODO: Write your solution below this line
# Save your file and run it using: python 1.3.8_loyalty_bonus.py

# Fix the code below
points = int(input("How many points are on your card? "))

if points < 100:
    points = points * 1.1
    print("Your bonus is 10 %")
if points >= 100:
    points = points * 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")
