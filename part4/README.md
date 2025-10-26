# Part 4 — Functions & Lists (37 tasks)

Master function design, list manipulation, definite iteration and string/list utilities. Each task has a docstring with instructions and a TODO section where you add your solution.

## Structure

```
part4/
├── README.md                  # This guide
├── .progress/
│   └── points.json            # Part 4 scores (auto-generated)
└── part4Exercises/
    └── tasks/
        ├── grade_part4.py     # Run this to check your solutions
        └── <task files>.py    # Your exercises (listed below)
```

## Tasks by section

### 4.1 More functions (10)
- 4.1.1_line.py — Draw line with character
- 4.1.2_a_box_of_hashes.py — Draw hash box (10×h)
- 4.1.3_a_square_of_hashes.py — Draw hash square (n×n)
- 4.1.4_a_square.py — Draw square with given character
- 4.1.5_a_triangle.py — Left-aligned triangle
- 4.1.6_a_shape.py — Triangle + rectangle combo
- 4.1.7_a_spruce.py — Centered spruce tree
- 4.1.8_the_greatest_number.py — Greatest of three numbers
- 4.1.9_same_characters.py — Compare characters by index
- 4.1.10_first_second_last_words.py — First/second/last words

### 4.2 Lists (8)
- 4.2.1_change_value.py — Modify list element (interactive)
- 4.2.2_add_items.py — Read N items into list (interactive)
- 4.2.3_addition_and_removal.py — Add/remove loop (interactive)
- 4.2.4_same_word_twice.py — Stop on duplicate word (interactive)
- 4.2.5_list_twice.py — Track list and sorted view (interactive)
- 4.2.6_length_of_list.py — Return list length
- 4.2.7_arithmetic_mean.py — Arithmetic mean of list
- 4.2.8_range_of_list.py — Range (max − min)

### 4.3 Definite iteration (12)
- 4.3.1_star_studded.py — Characters separated by '*'
- 4.3.2_negative_to_positive.py — List from −n..n
- 4.3.3_list_of_stars.py — Print a line of stars per number
- 4.3.4_anagrams.py — Check if two strings are anagrams
- 4.3.5_palindromes.py — Check if a string is a palindrome
- 4.3.6_sum_of_positives.py — Sum only positive numbers
- 4.3.7_even_numbers.py — Filter even numbers
- 4.3.8_sum_of_lists.py — Element-wise sum of two lists
- 4.3.9_distinct_numbers.py — Sorted unique values
- 4.3.10_length_of_longest.py — Length of longest string
- 4.3.11_shortest.py — Shortest string
- 4.3.12_all_the_longest.py — All strings with max length

### 4.4 Print statement formatting (1)
- 4.4.1_integers_to_strings.py — Format to 2 decimal places

### 4.5 More strings and lists (6)
- 4.5.1_everything_reversed.py — Reverse list and each string
- 4.5.2_most_common_character.py — Most frequent character
- 4.5.3_no_vowels_allowed.py — Remove vowels from string
- 4.5.4_no_shouting_allowed.py — Remove ALL-CAPS strings
- 4.5.5_neighbours_in_list.py — Longest neighbours series
- 4.5.6_grade_statistics.py — Grade statistics (interactive)

## How to work on tasks

1) Open any task file in `part4/part4Exercises/tasks/` and implement the function(s) below the TODO line.
2) Quick test a single file:

   PowerShell (Windows):
   - python part4Exercises\tasks\4.1.1_line.py

3) Grade all Part 4 tasks:

   PowerShell (Windows):
   - python part4Exercises\tasks\grade_part4.py

The grader expects exact output (including prompts for interactive tasks). Use the docstrings as contracts for inputs/outputs.

## Grading and progress

- Each correct task is worth 1 point; there are 37 tasks in Part 4.
- Scores are saved to `part4/.progress/points.json` and aggregated into the workspace `/.progress/marksheet.md`.
- Tasks are evaluated based on their current implementation each time the grader runs.

> Tip: For interactive tasks, double‑check your prompt text and spacing. Even a small mismatch will fail the test.
