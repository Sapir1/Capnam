"""
the pip class
"""
from baseObject import baseObject
class pip(baseObject):
    def __init__(self,gameWindow,x,y):
        #the instance of gameWindow (same instance)
        self.gameWindow = gameWindow
        self.x = x
        self.y = y
        #set the colour and size for drawing
        self.colour = self.gameWindow.BLUE
        self.size = int(gameWindow.TILESIZE/4)
