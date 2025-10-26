"""
5.2.3 Sudoku: print grid

Please write a function named print_sudoku(sudoku: list), which takes a two-dimensional 
array representing a sudoku grid as its argument. The function should print out the grid.

Empty squares should be replaced by underscores (_). The grid should be divided into 
3x3 blocks by blank lines and vertical bars (|).

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

    print_sudoku(sudoku)

Expected output:
    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _

    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _

    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _
    _ _ _  _ _ _  _ _ _

Another example:
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

    print_sudoku(sudoku)

Expected output:
    9 _ _  _ 8 _  3 _ _
    2 _ _  2 5 _  7 _ _
    _ 2 _  3 _ _  _ _ 4

    2 9 4  _ _ _  _ _ _
    _ _ _  7 3 _  5 6 _
    7 _ 5  _ 6 _  4 _ _

    _ _ 7  8 _ 3  9 _ _
    _ _ 1  _ _ _  _ _ 3
    3 _ _  _ _ _  _ _ 2
"""

# TODO: Implement your solution below this line

