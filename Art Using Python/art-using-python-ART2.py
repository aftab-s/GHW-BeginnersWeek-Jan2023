# Importing the Turtle Library
from turtle import *

color('black','gray')
# Fill Colour Will Be Yellow and The Boundary Colour will be Blue
begin_fill()
while True:
    forward(30)                        # Cursor Moves 120 steps forward
    right(80)                          # After 120 steps the cursor bends at an angle of 100 degrees
    backward(50)
    left(45)
    if abs(pos()) < 1:                  # When Cursor Reaches the Starting point, the movement of cursor stops
        break
color('violet','red')
while True:
    backward(120)
    left(45)
    if abs(pos()) < 1:                  # When Cursor Reaches the Starting point, the movement of cursor stops
        break

end_fill()
done()