"""
4.5.6 Grade Statistics

Interactive task:
- Repeatedly read integer exam points from the user with prompt: Exam results: 
- Stop when the user enters an empty line
- Valid points are 0..100; values outside this range should be ignored
- Passing points are 50..100
- Convert points to grades as follows:
  0..49 -> 0
  50..59 -> 1
  60..69 -> 2
  70..79 -> 3
  80..89 -> 4
  90..100 -> 5
- After input ends, print exactly:
  Statistics:
  Points average: X.X
  Pass percentage: Y.Y
  Grade distribution:
    5: *****
    4: ****
    3: ***
    2: **
    1: *
    0: 

The example used in the grader expects:
Inputs: 15, 21, 28, 31, 35, 38, 42, ''
Outputs (exact):
Statistics:
Points average: 30.0
Pass percentage: 85.7
Grade distribution:
  5: ***
  4: *
  3: *
  2: 
  1: **
  0: *
"""

# TODO: Write your solution below this line
