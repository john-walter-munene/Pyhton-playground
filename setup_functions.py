import math
# set the parameters.

def setparams(self, xc, yc, col, R, r, l):
    # The Spirograph parameters.
    self.xc = xc
    self.yc = yc
    self.R = int(R)
    self.r = int(r)
    self.l = l
    self.col = col
    
    # Reduce r/R to its smallest form by dividing with the GCD.
    gcdVal = math.gcd(self.r, self.R)
    self.nRot = self.r//gcdVal
    # Get ratio of radii.
    self.k = r/float(R)
    # set the color.
    self.t.color(*col)
    # Store the current angle.
    self.a = 0 
