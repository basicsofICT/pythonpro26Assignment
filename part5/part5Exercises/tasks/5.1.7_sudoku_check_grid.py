"""
5.1.7 Sudoku: check grid

Please write a function named sudoku_grid_correct(sudoku: list), which takes a 
two-dimensional array representing a sudoku grid as its argument. The function should 
use the functions from the three previous exercises to determine whether the complete 
sudoku grid is filled in correctly.

The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. 
If all contain each of the numbers 1 to 9 at most once, the function returns True. 
If a single one is filled in incorrectly, the function returns False.

The nine blocks to check begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), 
(3, 6), (6, 0), (6, 3) and (6, 6).

Example:
    sudoku1 = [
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
    
    print(sudoku_grid_correct(sudoku1))

Expected output:
    False
"""

# TODO: Implement your solution below this line

