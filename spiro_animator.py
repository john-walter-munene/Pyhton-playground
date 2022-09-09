# animatispiral_constructor
import turtle
from spiral_constructor import Spiro
class SpiroAnimator():
    """A class for animating spirographs."""
    def __init__(self, N ):
        # Set the timer value in milliseconds.
        self.deltaT = 10
        # Get the window dimensions.
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        # Create the Spiro objects.
        self.spiros = []
        for i in range(N):
            # Generate random parameters.
            rparams = self.genRandomParams()
            # Set the spiro parameters.
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
            
        # call timer
        turtle.ontimer(self.update, self.deltaT)

    def update(self):
    # Update all spiros.
        nComplete = 0
        for spiro in self.spiros:
            #   Update.
            spiro.update()
            # Count completed spiros.
            if spiro.drawingComplete:
                nComplete += 1
        # Restart if all spiros are complete.
        if nComplete == len(self.spiros):
            self.restart()
        # Call the timer.
        turtle.ontimer(self.update, self.deltaT)