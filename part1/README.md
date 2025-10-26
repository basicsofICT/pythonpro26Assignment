# Part 1: Python Programming Fundamentals (31 points)

📚 **Topics:** Print statements, Variables, Arithmetic operations, Conditional statements

📖 **Reading materials:** https://dipaish.github.io/programming-24/part-1 

## Folders
- `part1Exercises/tasks/` — Write your solutions here (one file per task)
- `.progress/` — Your scores are saved here

## Instructions
1. Write each solution as its own Python file in: `part1Exercises/tasks/`
2. Test a task by running it:

   **Windows (PowerShell/CMD)**  
   ```bat
   python part1Exercises\tasks\1_emoticon.py
   ```

   **macOS/Linux**  
   ```bash
   python part1Exercises/tasks/1_emoticon.py
   ```

3. Grade Part 1:

   **Windows**  
   ```bat
   python part1Exercises\grade_part1.py
   ```

   **macOS/Linux**  
   ```bash
   python part1Exercises/grade_part1.py
   ```

Each task is worth **1 point**. Your score persists across grading sessions.

---

## Task Overview (31 total)

| Section | Tasks | Topics |
|---------|-------|--------|
| **Getting Started** | 10 | Basic print statements, user input, string concatenation |
| **1.1 More About Variables** | 3 | Variable usage, expression printing, fixing print errors |
| **1.2 Arithmetic Operations** | 8 | Math operators, calculations, integer division |
| **1.3 Conditional Statements** | 10 | if/elif/else, comparisons, boolean logic |

### Task Files Location
All tasks are in: `part1Exercises/tasks/`

**File naming convention:**
- Basic tasks: `1_emoticon.py`, `2_seven_brothers.py`, ... `10_story.py`
- Section tasks: `1.1.1_extra_space.py`, `1.2.1_times_five.py`, `1.3.1_orwell.py`, etc.

> 💡 **Tip:** Open task files to see detailed instructions, sample inputs/outputs, and requirements for each exercise.

---

## Grading
Run the grader to check your solutions:

**Windows**
```bat
cd part1\part1Exercises\tasks
python grade_part1.py
```

**macOS/Linux**
```bash
cd part1/part1Exercises/tasks
python grade_part1.py
```

The auotmated grader will:
- ✓ Check each task's output against expected results
- ✓ Award 1 point per correct task (31 points total)
- ✓ Save your cumulative score to: `workspace/.progress/points.json`
- ✓ Generate a progress report at: `workspace/.progress/marksheet.md`
- ✓ Show your Part 1 score and total score across all 6 parts

Tasks are evaluated based on their current implementation each time the grader runs.

---

## 💾 Save Your Work - Git Commit & Push

**Important:** After completing tasks, commit and push your changes to GitHub!

### Step 1: Check what changed
```bash
git status
```

### Step 2: Add your completed task files
```bash
# Add specific files
git add part1/part1Exercises/tasks/1_emoticon.py
git add part1/part1Exercises/tasks/1.2.1_times_five.py

# OR add all changed files at once
git add .
```

### Step 3: Commit with a message
```bash
git commit -m "Complete Part 1 tasks: emoticon, times_five"
```

### Step 4: Push to GitHub
```bash
git push
```

> 💡 **Best Practice:** Commit after completing each task or section. This creates a backup and tracks your progress!

> ⚠️ **Reminder:** Your local progress (`workspace/.progress/`) is tracked. Push regularly to avoid losing work!

---

## Summary

- **Total Points:** 31
- **Sections:** 4 (Getting Started, Variables, Arithmetic, Conditionals)
- **Key Concepts:** Print, input, variables, operators, if/elif/else statements
- **Progress Tracking:** Scores saved in `workspace/.progress/points.json`
- **Progress Report:** View your progress in `workspace/.progress/marksheet.md`

Each task is worth **1 point**. Complete tasks stay marked as passed across grading sessions. Good luck! 🚀
