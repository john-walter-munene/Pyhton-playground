# A class that draws the spirograph.

import turtle

class Spiro():
    """A class that will draw the spirographs."""
    def __init__(self, xc, yc, col, R, r, l):
        """Initializing the class turle attributes"""
        
        # Create the turle object.
        self.t = turtle.Turtle()
        # Set the cursor shape.
        self.t.shape('turtle')
        # Set the step in degrees.
        self.step = 5
        # set the drawing complete flag.
        self.drawingComplete = False
        
        # Set the parameters.
        self.setparams(xc, yc, col, R, r, l)
        
        # Initialize the drawing.
        self.restart()
        
        # call timer
        turtle.ontimer(self.update, self.deltaT)