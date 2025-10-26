# Part 6 — File Handling & Errors (19 tasks)

This part focuses on reading/writing files and robust input/parameter validation. Each task file contains a docstring with a spec and a TODO section where you add your code.

## Structure

```
part6/
├── README.md                      # This guide
└── part6Exercises/
    └── tasks/
        ├── grade_part6.py         # Run this to check your solutions
        ├── <task files>.py        # Your exercises
        └── data files             # e.g., numbers.txt, matrix.txt, ...
```

## Tasks by section

### 6.1 Reading files (9)
- 6.1.1_largest_number.py — Return largest number from numbers.txt
- 6.1.2_fruit_market.py — Read fruits.csv into dict {name: price}
- 6.1.3_matrix.py — Sum, max, and row sums from matrix.txt
- 6.1.4_course_grading_part1.py — Print total exercises per student (interactive)
- 6.1.5_course_grading_part2.py — Add exam points and grade (interactive)
- 6.1.6_course_grading_part3.py — Tabulated stats (interactive)
- 6.1.7_spell_checker.py — Mark misspelled words using wordlist.txt (interactive)
- 6.1.8_recipe_search.py — Search by name/time/ingredient (functions)
- 6.1.9_city_bikes.py — Station data, distances, and greatest distance

### 6.2 Writing files (7)
- 6.2.1_inscription.py — Write greeting to chosen file (interactive)
- 6.2.2_diary.py — Append/read diary.txt (interactive)
- 6.2.3_filtering_contents.py — Split correct/incorrect to CSVs
- 6.2.4_store_personal_data.py — Append person tuple to people.csv
- 6.2.5_course_grading_part4.py — Save totals and grades to results.csv
- 6.2.6_word_search.py — Pattern search with wildcards (interactive)
- 6.2.7_dictionary_file.py — Persisted dictionary (interactive)

### 6.3 Handling errors (3)
- 6.3.1_reading_input.py — Validate numeric input with messages (interactive)
- 6.3.2_parameter_validation.py — Validate parameters and report errors
- 6.3.3_incorrect_lottery.py — Validate lottery numbers from file

## How to work on tasks

1) Open any task file in `part6/part6Exercises/tasks/` and implement the functions or interactive flow below the TODO line.
2) Quick test a single file by running it directly.
3) Grade all Part 6 tasks:

   PowerShell (Windows):
   - python part6Exercises\tasks\grade_part6.py

The grader expects exact output (including prompts for interactive tasks) based on its tests. Use the docstrings as contracts for input/output.

## Grading and progress

- Each correct task is worth 1 point; there are 19 tasks in Part 6.
- Scores are saved to `/.progress/points.json` and summarized in `/.progress/marksheet.md` at the workspace root.
- Tasks are evaluated based on their current implementation each time the grader runs.

> Tip: For file tasks, use `with open(...) as f:` context managers and be careful with newlines and exact formatting. For interactive tasks, match prompts and spacing exactly.
