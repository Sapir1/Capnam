"""
the base class for almost everything that will be drawn in the scene
like the pips and the capnam
"""
import pygame
from GameWindow import GameWindow
class baseObject:
    def __init__(self,gameWindow):
        """
        this init function should almost
        always not be used but i have it as
        the defualt settings just in case
        """
        self.gameWindow = gameWindow
        self.colour = self.gameWindow.YELLOW
        self.size = int(self.gameWindow.TILESIZE)
        self.x = [x]
        self.y = [y]
    def draw(self):
        """
        draws the object
        """
        for coord in self.x:
            self.xcoord = coord * self.gameWindow.TILESIZE - int(self.gameWindow.TILESIZE/2) # Multiply to get pixels, subtract so centre lines up -> circle lines up with grid
        for coord in self.y:
            self.ycoord = coord * self.gameWindow.TILESIZE - int(self.gameWindow.TILESIZE/2)
        pygame.draw.circle(self.gameWindow.DISPLAYSURF, self.colour, (self.xcoord,self.ycoord), self.size)
