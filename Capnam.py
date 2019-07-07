#player class

import sys
from BasePiece import BasePiece
from direction import Direction

class Capnam(BasePiece):
    def __init__(self,gameWindow):
        #directions to be made ENUM? it would be needed in both main and Capnam, ideas? - A-Small-Being
        # self.UP = 'up
        # self.DOWN = direction.DOWN'
        # self.LEFT = direction.LEFT
        # self.RIGHT = direction.RIGHT

        # instance of object gameWindow from class GameWindow
        self.gameWindow = gameWindow

        #start point
        self.startx = int((self.gameWindow.WINDOWHEIGHT / self.gameWindow.TILESIZE) / 2)
        self.starty = int((gameWindow.WINDOWWIDTH / self.gameWindow.TILESIZE) / 2)
        #coordinates
        self.x = self.startx
        self.y = self.starty
        #set the colour and size for drawing
        self.colour = self.gameWindow.YELLOW
        self.size = int(self.gameWindow.TILESIZE/2)
        #the score
        self.score = 0
        self.shape = "circle"

    def movePlayer(self,direction):
        """
        Works out where player should go and starts draw process
        """
        if direction == Direction.UP:
            self.y -= 1
        elif direction == Direction.DOWN:
            self.y += 1
        elif direction == Direction.LEFT:
            self.x -= 1
        elif direction == Direction.RIGHT:
            self.x += 1




    def hitDetect(self, direction, solid):
        # Hit edge code not finished - A-Small-Being
        """
        Check to see if player has hit edge or wall
        """
        modX = self.x
        modY = self.y
        if direction == Direction.LEFT:
            modX -= 1
        elif direction == Direction.RIGHT:
            modX += 1
        elif direction == Direction.UP:
            modY -= 1
        elif direction == Direction.DOWN:
            modY += 1

        if (modX, modY) in solid:
            return True

        if modX == 0:
            #too far left
            pass
        elif modX == self.gameWindow.TILEWIDTH + 1:
            # Too far right
            pass
        elif modY == 0:
            # Too far up
            pass
        elif modY == self.gameWindow.TILEHEIGHT + 1:
            # Too far down
            pass
        else:
            # Fine
            return False
        return True


    def increaseScore(self):
        """
        increments the score
        """
        self.score += 1
