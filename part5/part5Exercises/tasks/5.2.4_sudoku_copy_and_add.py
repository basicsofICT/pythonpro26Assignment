"""
5.2.4 Sudoku: copy and add

Please write a function named copy_and_add(sudoku: list, row_no: int, column_no: int, 
number: int), which takes a sudoku grid, and the coordinates of a single square, as 
its arguments. The function should return a copy of the grid with the number added 
to the specified square.

The function should not modify the original grid.

Example:
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)

Expected output:
    Original:
    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _

    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _

    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _

    Copy:
    2 _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _

    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _

    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _
"""

# TODO: Implement your solution below this line

