# Importing the Turtle Library
from turtle import *

color('blue','yellow')
# Fill Colour Will Be Yellow and The Boundary Colour will be Blue
begin_fill()
while True:
    forward(120)                        # Cursor Moves 120 steps forward
    right(100)                          # After 120 steps the cursor bends at an angle of 100 degrees
    if abs(pos()) < 1:                  # When Cursor Reaches the Starting point, the movement of cursor stops
        break
end_fill()
done()