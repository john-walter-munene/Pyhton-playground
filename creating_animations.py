import math
# Function to makethe updates.
def update(self):
    """Update by one step."""
    if self.drawingComplete:
        return
    
    # Increment the angle.
    self.a += self.step
    # Draw a step.
    R, k, l = self.R, self.k, self.l
    # Set the angle.
    a = math.radians(self.a)
    x = self.R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
    y = self.R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
    self.t.setpos(self.xc + x, self.yc + y)
    # if drawing is complete, set the flag
    if self.a >= 360*self.nRot:
        self.drawingComplete = True
    # drawing is now done so hide the turtle cursor
    self.t.hideturtle()