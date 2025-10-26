# Part 3: Loops with Conditions, Strings & Functions

This part introduces more advanced programming concepts including conditional loops, string manipulation, and defining your own functions.

## Topics Covered

### Section 3.1: Loops with Conditions (7 tasks)
Learn to use `while` loops with conditions, working with powers, and calculating sums:
- 3.1.1: Print Numbers - Even numbers 2-30
- 3.1.2: Fix the Code: Countdown - Syntax error fixing
- 3.1.3: Numbers - Print 1 to n
- 3.1.4: Powers of Two - Sequence up to limit
- 3.1.5: Powers of Base n - Any base powers
- 3.1.6: Sum of Consecutive Numbers v1 - Result only
- 3.1.7: Sum of Consecutive Numbers v2 - Show calculation

### Section 3.2: Working with Strings (15 tasks)
Master string operations including repetition, comparison, slicing, and searching:
- 3.2.1: String Multiplied - Repeat string n times
- 3.2.2: The Longer String - Compare string lengths
- 3.2.3: End to Beginning - Reverse character by character
- 3.2.4: Second and Second to Last Characters - Character comparison
- 3.2.5: A Line of Hashes - Print line of # characters
- 3.2.6: A Rectangle of Hashes - Print hash rectangle
- 3.2.7: Underlining - Underline strings with dashes
- 3.2.8: Right-Aligned - Right-align with padding
- 3.2.9: A Framed Word - Center word in frame
- 3.2.10: Substrings Part 1 - Substrings from start
- 3.2.11: Substrings Part 2 - Substrings from end
- 3.2.12: Does It Contain Vowels - Check for a, e, o
- 3.2.13: Find the First Substring - First 3-char match
- 3.2.14: Find All the Substrings - All 3-char matches
- 3.2.15: The Second Occurrence - Non-overlapping search

### Section 3.3: More Loops (5 tasks)
Advanced loop techniques including nested loops and list processing:
- 3.3.1: Multiplication - Multiplication table
- 3.3.2: First Letters of Words - Extract first characters
- 3.3.3: Factorial - Calculate n!
- 3.3.4: Flip the Pairs - Swap adjacent characters
- 3.3.5: Taking Turns - Alternate between two strings

### Section 3.4: Defining Functions (7 tasks)
Learn to create reusable code by defining your own functions:
- 3.4.1: Seven Brothers - Return list of names
- 3.4.2: The First Character - Return first char
- 3.4.3: Mean - Calculate average of three numbers
- 3.4.4: Print Many Times - Print string n times
- 3.4.5: A Square of Hashes - Print hash square
- 3.4.6: Chessboard - Print 1/0 chessboard pattern
- 3.4.7: A Word Squared - Word in special pattern

## Getting Started

1. Navigate to the tasks directory:
   ```bash
   cd part3/part3Exercises/tasks
   ```

2. Each task file contains:
   - A description of what to implement
   - Example interactions showing expected input/output
   - Detailed instructions
   - A TODO comment marking where to write your solution

3. Open any task file (e.g., `3.1.1_print_numbers.py`) and complete the implementation

4. Test your solution:
   ```bash
   python 3.1.1_print_numbers.py
   ```

## Grading

To check your progress on Part 3:

```bash
# From the tasks directory
python grade_part3.py

# Or from the workspace root
python part3/part3Exercises/tasks/grade_part3.py
```

The grader will:
- Test all 34 tasks automatically
- Show which tasks pass/fail
- Save your score to `.progress/points.json`
- Update the course-wide marksheet at `.progress/marksheet.md`

**Total Points Available:** 34 (1 point per task)

## Tips for Success

- **Read examples carefully**: The interaction examples show exact formatting expected
- **Test incrementally**: Run your code frequently to catch errors early
- **Use string methods**: Python has powerful string methods (`.split()`, `.find()`, etc.)
- **Functions return values**: In Section 3.4, most functions should `return` rather than `print`
- **Check edge cases**: Consider what happens with empty strings, zero inputs, etc.

## Git Workflow

Once you've completed tasks, commit your work:

```bash
# Add specific files
git add part3/part3Exercises/tasks/3.1.1_print_numbers.py
git add part3/part3Exercises/tasks/3.2.1_string_multiplied.py

# Or add all Part 3 changes
git add part3/

# Commit with a descriptive message
git commit -m "Complete Part 3 Section 3.1 - Loops with conditions"

# Push to remote repository
git push origin main
```

## Common Mistakes to Avoid

1. **Off-by-one errors**: When using ranges, remember `range(1, 6)` generates 1,2,3,4,5 (not 6)
2. **String indexing**: Negative indices work backwards: `s[-1]` is last char, `s[-2]` is second-to-last
3. **Input vs prompt**: Input prompts should match examples exactly (including spacing, colons)
4. **Function definitions**: Must use exact function names specified in instructions
5. **Overlapping substrings**: Task 3.2.15 requires non-overlapping matches

## Additional Resources

- Python string methods: https://docs.python.org/3/library/stdtypes.html#string-methods
- While loops: https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming
- Defining functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions

## Progress Tracking

Your progress is automatically tracked in:
- **Points file**: `.progress/points.json` (JSON format, per-task scoring)
- **Marksheet**: `.progress/marksheet.md` (Human-readable progress report)

Both files are automatically updated each time you run the grader.

---

**Ready to start?** Open `3.1.1_print_numbers.py` and begin coding! 🚀
