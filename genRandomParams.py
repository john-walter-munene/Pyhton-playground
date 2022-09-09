
import random

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