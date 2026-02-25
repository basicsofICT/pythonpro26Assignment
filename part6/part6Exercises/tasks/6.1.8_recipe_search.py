"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part6/part6Exercises/tasks (if needed)
Run: python 6.1.8_recipe_search.py | Check: python grade_part6.py

6.1.8 Recipe search

Task: Implement functions reading recipes from a file with blocks:
- search_by_name(filename: str, word: str) -> list[str]
- search_by_time(filename: str, prep_time: int) -> list[str]
- search_by_ingredient(filename: str, ingredient: str) -> list[str]

Examples (when implemented):
search_by_name("recipes1.txt", "cake") -> ["Pancakes", "Cake pops"]
search_by_time("recipes1.txt", 20) -> ["Pancakes, preparation time 15 min"]
search_by_ingredient("recipes1.txt", "eggs") -> ["Pancakes, preparation time 15 min", ...]
"""

# TODO: Implement your solution below this line
def search_by_name(filename: str, word: str) -> list[str]:
    # Return recipe names containing the search word (case-insensitive)
    pass

def search_by_time(filename: str, prep_time: int) -> list[str]:
    # Return recipes with time <= prep_time, formatted with time
    pass

def search_by_ingredient(filename: str, ingredient: str) -> list[str]:
    # Return recipes containing ingredient, formatted with time
    pass

# Save your file and run it using: python 6.1.8_recipe_search.py
# Check: python grade_part6.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 6.1.8"         (commit with message)
# 3. git push                                      (push to GitHub)
