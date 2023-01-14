import turtle
import random

turtle.bgcolor('black') 
# Canvas Colour

turtle.colormode(255)                                           
turtle.speed(0)

for x in range(500): 

    r,b,g=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    turtle.pencolor(r,g,b)                                      
    # Setting the colour of the line based on the random generated r,g,b values
    
    turtle.fd(x+50)
    # Here we move forward by x+50 which means initially we move forward by 50 units 
    # then by 51 units then 52 so on till 50+499 units.
    
    turtle.rt(91)
    # After each movement, the cursor moves 91 degrees to the right.

turtle.exitonclick()
# Canvas doesn't close automatically and would close only on click.

turtle.getscreen().getcanvas().postscript(file='Turtle-Spiral.png')