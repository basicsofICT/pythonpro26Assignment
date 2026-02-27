"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part5 (if needed)
Run: python 5.2.5_tic_tac_toe.py | Check: python grade_part5.py

5.2.5 Tic-Tac-Toe

Tic-Tac-Toe is played on a 3 by 3 grid, by two players who take turns inputting 
noughts and crosses. If either player succeeds in placing three of their own symbols 
on any row, column or diagonal, they win. If neither player manages this, it is a draw.

Please write a function named play_turn(game_board: list, x: int, y: int, piece: str), 
which places the given symbol at the given coordinates on the board. The values of the 
coordinates on the board are between 0 and 2.

NB: when compared to the sudoku exercises, the arguments the function takes are the 
other way around here. The column x comes first, and the row y second.

The board consists of the following strings:
    "": empty square
    "X": player 1 symbol
    "O": player 2 symbol

The function should return True if the square was empty and the symbol was successfully 
placed on the game board. The function should return False if the square was occupied, 
or if the coordinates weren't valid.

Example:
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)

Expected output:
    True
    [['', '', 'X'], ['', '', ''], ['', '', '']]
"""

# TODO: Write your solution below this line



# Save your file and run it using: python 5.2.5_tic_tac_toe.py
# Check: python grade_part5.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 5.2.5"         (commit with message)
# 3. git push                                      (push to GitHub)
