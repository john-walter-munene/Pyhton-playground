# Restarting the program
def restart(self):
    """Restarting Spiro drawings"""
    for spiro in self.spiros:
        # Clear.
        spiro.clear()
        # Generate random parameters.
        rparams = self.genRandomParams()
        # Set the spiro parameters.
        spiro.setparams(*rparams)
        # Restart drawing.
        spiro.restart()