import math

def draw(self):
    """Drawing the complete spiralgraphs"""
    # Draw the rest of the points.
    R, k, l = self.R, self.k, self.l
    for i in range(0, 360*self.nRot + 1, self.step):
      a = math.radians(i)
    x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
    y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
    self.t.setpos(self.xc + x, self.yc + y)
    # drawing is now done so hide the turtle cursor
    self.t.hideturtle()
    