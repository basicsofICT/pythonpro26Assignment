"""
4.1.6 A Shape

Task: Define a function shape(size, ch1, height2, ch2) which first prints a left-aligned
triangle of `ch1` from 1..size, and then prints a rectangle of width `size` and height
`height2` using `ch2`.

Example (when implemented):
shape(5, "X", 3, "*") -> prints:
X
XX
XXX
XXXX
XXXXX
*****
*****
*****
"""

# TODO: Implement your solution below this line
def line(length: int, text: str):
    # Print a line of the requested length using the first character of text
    # If text is empty, use '*'
    pass

def shape(size: int, ch1: str, height2: int, ch2: str):
    # First print a left-aligned triangle of ch1 from 1..size
    # Then print a rectangle width=size and height=height2 of ch2
    pass

# You can test locally by uncommenting the call below
# shape(5, "X", 3, "*")
