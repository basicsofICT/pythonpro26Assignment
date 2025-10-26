# Part 5 — Advanced Topics (25 tasks)

Deepen your skills with lists, references, dictionaries, and tuples. Each task file contains a docstring with the spec and a TODO section for your code.

## Structure

```
part5/
├── README.md                     # This guide
└── part5Exercises/
    └── tasks/
        ├── grade_part5.py        # Run this to check your solutions
        └── <task files>.py       # Your exercises
```

## Tasks by section

### 5.1 More lists (7)
- 5.1.1_the_longest_string.py — Find longest string in list
- 5.1.2_number_of_matching_elements.py — Count matching elements across lists
- 5.1.3_go.py — Determine Go game winner
- 5.1.4_sudoku_check_row.py — Validate Sudoku row
- 5.1.5_sudoku_check_column.py — Validate Sudoku column
- 5.1.6_sudoku_check_block.py — Validate 3×3 Sudoku block
- 5.1.7_sudoku_check_grid.py — Validate entire Sudoku grid

### 5.2 References (6)
- 5.2.1_items_multiplied_by_two.py — Double list items in-place
- 5.2.2_remove_the_smallest.py — Remove smallest element
- 5.2.3_sudoku_print_grid.py — Print Sudoku grid
- 5.2.4_sudoku_copy_and_add.py — Copy grid and add number
- 5.2.5_tic_tac_toe.py — Place piece on board
- 5.2.6_transpose_matrix.py — Transpose a matrix

### 5.3 Dictionary (9)
- 5.3.1_times_ten.py — Dictionary with values × 10
- 5.3.2_factorials.py — Factorials dictionary
- 5.3.3_histogram.py — Character histogram
- 5.3.4_phone_book_v1.py — Phone book (single number)
- 5.3.5_phone_book_v2.py — Phone book (multiple numbers)
- 5.3.6_invert_dictionary.py — Swap keys and values
- 5.3.7_numbers_spelled_out.py — Number to word mapping
- 5.3.8_movie_database.py — Add movies to database
- 5.3.9_find_movies.py — Search movie database

### 5.4 Tuple (5)
- 5.4.1_create_tuple.py — Create tuple from numbers
- 5.4.2_the_oldest_person.py — Find oldest person
- 5.4.3_older_people.py — Filter people by age
- 5.4.4_student_database.py — Student course tracker
- 5.4.5_square_of_letters.py — Letter square pattern

## How to work on tasks

1) Open any task file in `part5/part5Exercises/tasks/` and implement the function(s) below the TODO line.
2) Quick test a single file by running it directly.
3) Grade all Part 5 tasks:

   PowerShell (Windows):
   - python part5Exercises\tasks\grade_part5.py

The grader expects exact output as specified by tests. Use the task docstrings for inputs/outputs and formatting.

## Grading and progress

- Each correct task is worth 1 point; there are 25 tasks in Part 5.
- **Part 5 is optional** and not counted toward your total score (143 points max).
- Scores aggregate into the workspace `/.progress/marksheet.md`.
- Tasks are evaluated based on their current implementation each time the grader runs.

> Tip: For reference/dictionary tasks, watch for mutation vs. returning new structures, and match print formatting exactly when required.
