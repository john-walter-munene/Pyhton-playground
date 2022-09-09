import math
# The restart() method.

def restart(self):
    """Restart drawings"""
    
    # Set the flag.
    self.drawingComplete = False
    # Show the turtle.
    self.t.showturtle()
    
    # Go to the first point.
    R, k, l = self.R, self.k, self.l
    a = 0.0
    x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
    y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
    self.t.setpos(self.xc + x, self.yc + y)
    self.t.down()
