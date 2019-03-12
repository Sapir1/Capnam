# Wall class
from baseObject import baseObject

class Wall(baseObject):
    def __init__(self,gameWindow,x,y):
        # # self.wCoords = wCoords
        # self.pCoords = [{'x': 10,'y': 10},
        #                 {'x': 10, 'y': 10}] #Player coordinates
        # self.gameWindow = gameWindow
        # self.colour = self.gameWindow.WHITE

        self.gameWindow = gameWindow
        #self.pCoords = [{'x': x,'y': y}]
        self.colour = self.gameWindow.WHITE
        self.size = int(gameWindow.TILESIZE/2)
        self.x = [x]
        self.y = [y]
        

    #def drawWall(self):
     #   """
      #  Tell gameWindow to draw 'wall' on screen
       # """
        #self.gameWindow.drawCircle(self.pCoords,self.gameWindow.WHITE)
