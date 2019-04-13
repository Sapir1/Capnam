# Wall class
from BasePiece import BasePiece

class Wall(BasePiece):
    def __init__(self,gameWindow,x,y):
        # # self.wCoords = wCoords
        # self.pCoords = [{'x': 10,'y': 10},
        #                 {'x': 10, 'y': 10}] #Player coordinates
        # self.gameWindow = gameWindow
        # self.colour = self.gameWindow.WHITE

        self.gameWindow = gameWindow
        #self.pCoords = [{'x': x,'y': y}]
        self.colour = self.gameWindow.WHITE
        self.size = gameWindow.TILESIZE
        self.x = x
        self.y = y
        self.shape = "rectangle"


    #def drawWall(self):
     #   """
      #  Tell gameWindow to draw 'wall' on screen
       # """
        #self.gameWindow.drawCircle(self.pCoords,self.gameWindow.WHITE)
