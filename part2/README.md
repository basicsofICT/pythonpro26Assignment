# Part 2: Conditionals & Loops (22 points)

📚 Topics: Comparisons, boolean logic, nested conditionals, while loops, simple input validation

📖 Reading materials: https://dipaish.github.io/programming-24/part-2

## Folders
- `part2Exercises/tasks/` — Write your solutions here (one file per task)
- `.progress/` — Your scores are saved here

## Instructions
1. Write each solution as its own Python file in: `part2Exercises/tasks/`
2. Test a task by running it:

   Windows (PowerShell/CMD)
   ```bat
   python part2Exercises\tasks\2.3.4_fizzbuzz.py
   ```

   macOS/Linux
   ```bash
   python part2Exercises/tasks/2.3.4_fizzbuzz.py
   ```

3. Grade Part 2:

   Windows
   ```bat
   cd part2\part2Exercises\tasks
   python grade_part2.py
   ```

   macOS/Linux
   ```bash
   cd part2/part2Exercises/tasks
   python grade_part2.py
   ```

Each task is worth 1 point. Your score persists across grading sessions.

---

## Task Overview (22 total)

| Section | Tasks | Topics |
|---------|-------|--------|
| 2.1 Programming terminology | 3 | Fixing syntax, string length, type conversion |
| 2.2 More conditionals | 4 | Comparisons, min/max logic, string ordering |
| 2.3 Combining conditions | 7 | and/or logic, ranges, FizzBuzz, leap years, tax |
| 2.4 Simple loops | 8 | while loops, counters, validation, repetition |

### Task Files Location
All tasks are in: `part2Exercises/tasks/`

File naming follows the pattern:
- `2.1.1_fix_syntax.py`, `2.1.2_number_of_characters.py`, ... `2.4.8_working_with_numbers.py`

> Tip: Open each task file to see detailed instructions and sample input/output.

---

## Grading
Run the grader to check your solutions:

Windows
```bat
cd part2\part2Exercises\tasks
python grade_part2.py
```

macOS/Linux
```bash
cd part2/part2Exercises/tasks
python grade_part2.py
```

The automated grader will:
- Check each task's output against expected results
- Award 1 point per correct task (22 points total)
- Save your cumulative score to: `workspace/.progress/points.json`
- Generate a progress report at: `workspace/.progress/marksheet.md`
- Show your Part 2 score and total score across all 6 parts

Tasks are evaluated based on their current implementation each time the grader runs.

---

## Save Your Work — Git Commit & Push

Important: After completing tasks, commit and push your changes to GitHub.

Step 1: Check what changed
```bash
git status
```

Step 2: Add your completed task files
```bash
# Add specific files
git add part2/part2Exercises/tasks/2.3.4_fizzbuzz.py
git add part2/part2Exercises/tasks/2.4.1_shall_we_continue.py

# OR add all changed files at once
git add .
```

Step 3: Commit with a message
```bash
git commit -m "Complete Part 2 tasks: fizzbuzz, shall_we_continue"
```

Step 4: Push to GitHub
```bash
git push
```

> Best Practice: Commit after completing each task or section to track progress and create a backup.

> Reminder: Your local progress (`workspace/.progress/`) is tracked. Push regularly to avoid losing work!

---

## Summary

- Total Points: 22
- Sections: 4 (terminology, conditionals, combined conditions, loops)
- Key Concepts: Comparisons, if/elif/else, boolean logic, while loops, input validation
- Progress Tracking: Scores saved in `workspace/.progress/points.json`
- Progress Report: View in `workspace/.progress/marksheet.md`

Good luck and have fun! 🚀
