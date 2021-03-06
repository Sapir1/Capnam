"""
the base class for almost everything (all the pieces) that will be drawn in the scene
like the pips and the capnam
"""
from GameWindow import GameWindow
class BasePiece:
    def __init__(self,gameWindow):
        """
        this init function should almost
        always not be used but i have it as
        the defualt settings just in case
        """
        self.gameWindow = gameWindow
        self.colour = self.gameWindow.YELLOW
        self.size = int(self.gameWindow.TILESIZE)
        self.x = x
        self.y = y
    def draw(self):
        """
        draws the object
        """
        if (self.shape == "circle") :
            self.gameWindow.drawCircle(self.x,self.y,self.colour,self.size)

        if (self.shape == "rectangle") :
            self.gameWindow.drawRect(self.x,self.y,self.colour, self.size)
