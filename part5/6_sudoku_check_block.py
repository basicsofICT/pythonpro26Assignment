"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part5 (if needed)
Run: python 5.1.6_sudoku_check_block.py | Check: python grade_part5.py

5.1.6 Sudoku: check block

Please write a function named block_correct(sudoku: list, row_no: int, column_no: int), 
which takes a two-dimensional array representing a sudoku grid, and two integers referring 
to the row and column indexes of a single square, as its arguments. Rows and columns are 
indexed from 0.

The function should return True or False depending on whether the 3 by 3 block to the 
right and down from the given indexes is filled in correctly. That is, whether the block 
contains each of the numbers 1 to 9 at most once.

Example:
    sudoku = [
      [9, 0, 0, 0, 8, 0, 3, 0, 0],
      [2, 0, 0, 2, 5, 0, 7, 0, 0],
      [0, 2, 0, 3, 0, 0, 0, 0, 4],
      [2, 9, 4, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 7, 3, 0, 5, 6, 0],
      [7, 0, 5, 0, 6, 0, 4, 0, 0],
      [0, 0, 7, 8, 0, 3, 9, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 3],
      [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))

Expected output:
    False
    True
"""

# TODO: Write your solution below this line



# Save your file and run it using: python 5.1.6_sudoku_check_block.py
# Check: python grade_part5.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 5.1.6"         (commit with message)
# 3. git push                                      (push to GitHub)
