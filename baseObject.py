"""
the base class for anything that needs to be drawn in the scene
"""
import pygame
from GameWindow import GameWindow
class baseObject:
    def __init__(self,gameWindow):
        self.gameWindow = gameWindow
        self.colour = self.gameWindow.YELLOW
        self.size = int(self.gameWindow.TILESIZE)
        self.pCoords = [{'x': 1,'y': 1}]
    def drawObject(self):
        """
        draws the object
        """
        for coord in self.pCoords:
            self.x = coord['x'] * self.gameWindow.TILESIZE - int(self.gameWindow.TILESIZE/2) # Multiply to get pixels, subtract so centre lines up -> circle lines up with grid
            self.y = coord['y'] * self.gameWindow.TILESIZE - int(self.gameWindow.TILESIZE/2)
            pygame.draw.circle(self.gameWindow.DISPLAYSURF, self.colour, (self.x,self.y), self.size)
