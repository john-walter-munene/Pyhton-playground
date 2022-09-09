import sys, random, argparse
import numpy as np
import math
import turtle
import random
from PIL import Image
from datetime import datetime 
from math import gcd

class Spiro:
    """A class that draws a Spirograph."""
    # constructor
    def __init__(self, xc, yc, col, R, r, l):
        # Create the turtle object.
        self.t = turtle.Turtle()
        # Set the cursor shape.
        self.t.shape('turtle')
        # Set the step in degrees.
        self.step = 5
        # Set the drawing complete flag.
        self.drawingComplete = False
        # Set the parameters.
        self.setparams(xc, yc, col, R, r, l)
        # Initialize the drawing.
        self.restart()

    # Set the parameters.
    def setparams(self, xc, yc, col, R, r, l):
        # The Spirograph parameters.
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        # Reduce r/R to its smallest form by dividing with the GCD.
        gcdVal = gcd(self.r, self.R)
        self.nRot = self.r//gcdVal
        # Get ratio of radii.
        self.k = r/float(R)
        # Set the color.
        self.t.color(*col)
        # Store the current angle.
        self.a = 0
        
     # Restart the drawing.
    def restart(self):
        # Set the flag.
        self.drawingComplete = False
        # Show the turtle.
        self.t.showturtle()
        # Go to the first point.
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()
        
    # Draw the whole thing.
    def draw(self):
        # Draw the rest of the points.
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360*self.nRot + 1, self.step):
            a = math.radians(i)
            x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc + x, self.yc + y)
        # Drawing is now done so hide the turtle cursor.
        self.t.hideturtle()
        
    
    # Update by one step.
    def update(self):
        # Skip the rest of the steps if done.
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
        # If drawing is complete, set the flag.
        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            # Drawing is now done so hide the turtle cursor.
            self.t.hideturtle()
            
    # Clear everything.
        def clear(self):
            self.t.clear()
            
 
class SpiroAnimator:
    """A class for animating Spirographs."""
    # Constructor.
    def __init__(self, N):
        # set the timer value in milliseconds.
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
            # Call timer.
        turtle.ontimer(self.update, self.deltaT)
        
    # Restart spiro drawing.
    def restart(self):
        for spiro in self.spiros:
            # Clear.
            spiro.clear()
            # Generate random parameters.
            rparams = self.genRandomParams()
            # Set the spiro parameters.
            spiro.setparams(*rparams)
            # Restart drawing.
            spiro.restart()
            
    
    def genRandomParams(self):
        """Generate random parameters."""
        width, height = self.width, self.height
        R = random.randint(50, min(width, height)//2)
        r = random.randint(10, 9*R//10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width//2, width//2)
        yc = random.randint(-height//2, height//2)
        col = (random.random(),
            random.random(),
            random.random())
        return (xc, yc, col, R, r, l)
    
    def update(self):
        """update all spiros"""
        nComplete = 0
        for spiro in self.spiros:
        # Update.
            spiro.update()
            # count completed spiros
            if spiro.drawingComplete:
                nComplete += 1
        # Restart if all spiros are complete.
        if nComplete == len(self.spiros):
            self.restart()
        # Call the timer.
        turtle.ontimer(self.update, self.deltaT)
        
    
    def toggleTurtles(self):
        """Toggle turtle cursor on and off."""
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()
     
    
    def saveDrawing():
        """Save drawings as PNG files."""
        # Hide the turtle cursor.
        turtle.hideturtle()
        # Generate unique filenames.
        dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
        fileName = 'spiro-' + dateStr 
        print('saving drawing to %s.eps/png' % fileName)
        # Get the tkinter canvas.
        canvas = turtle.getcanvas()
        # Save the drawing as a postscipt image.
        canvas.postscript(file = fileName + '.eps')
        # Use the Pillow module to convert the poscript image file to PNG.
        img = Image.open(fileName + '.eps')
        img.save(fileName + '.png', 'png')
        # Show the turtle cursor.
        turtle.showturtle()
    
# main() function
def main():
    """The MaiNn function that runs the program"""
    # Use sys.argv if needed.
    print('generating spirograph...')
    # Create parser.
    descStr = """This program draws Spirographs using the Turtle module. 
    When run with no arguments, this program draws random Spirographs.
    
    Terminology:
    R: radius of outer circle
    r: radius of inner circle
    l: ratio of hole distance to r
    """
    parser = argparse.ArgumentParser(description=descStr)
    
    # Add expected arguments.
    parser.add_argument('--sparams', nargs=3, dest='sparams', required=False, 
    help="The three arguments in sparams: R, r, l.")
    # Parse args.
    args = parser.parse_args()
    # Set the width of the drawing window to 80 percent of the screen width.
    turtle.setup(width=0.8)
    # Set the cursor shape to turtle.
    turtle.shape('turtle')
    # Set the title to Spirographs!
    turtle.title("Spirographs!")
    # Add the key handler to save our drawings.
    turtle.onkey(saveDrawing, "s")
    # start listening 
    turtle.listen()
    
    # Check for any arguments sent to --sparams and draw the Spirograph.
    if args.sparams:
        params = [float(x) for x in args.sparams]
        # draw the Spirograph with the given parameters
        col = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, col, *params)
        spiro.draw()
    else:
        # Create the animator object.
        spiroAnim = SpiroAnimator(4)
        # Add a key handler to toggle the turtle cursor.
        turtle.onkey(spiroAnim.toggleTurtles, "t")
        # Add a key handler to restart the animation.
        turtle.onkey(spiroAnim.restart, "space")
        
    # Start the turtle main loop.
    turtle.mainloop()

# Call main.
if __name__ == '__main__':
    main()
        
