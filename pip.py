"""
the pip class
"""
from baseObject import baseObject
class pip(baseObject):
    def __init__(self,gameWindow,x,y):
        #an instance of gameWindow
        self.gameWindow = gameWindow
        #the x and y
        self.pCoords = [{'x': x,'y': y}]
        #set the colour and size for drawing
        self.colour = self.gameWindow.BLUE
        self.size = int(gameWindow.TILESIZE/4)
