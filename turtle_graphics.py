import math, turtle

# Draw the circle using turtle
def draw_circle_turle(x, y, r):
    """Initialize the start of the circle and then draw it."""
    
    # Move to the start of the circle.
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()
    
    # Draw the circle.
    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))
        
draw_circle_turle(100, 100, 50)
turtle.mainloop()
    