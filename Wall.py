# Wall class

class Wall:
    def __init__(self,gameWindow):
        # self.wCoords = wCoords
        self.wCoords = [{'x': 9,'y': 9},
                        {'x': 9, 'y': 10}] #Player coordinates
        self.gameWindow = gameWindow

    def drawWall(self):
        """
        Tell gameWindow to draw 'wall' on screen
        """
        self.gameWindow.drawCircle(self.wCoords,self.gameWindow.WHITE)
