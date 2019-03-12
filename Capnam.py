#player class

import pygame,sys
from baseObject import baseObject

class Capnam(baseObject):
    def __init__(self,gameWindow):
        #directions to be made ENUM? it would be needed in both main and Capnam, ideas? - A-Small-Being
        # self.UP = 'up
        # self.DOWN = 'down'
        # self.LEFT = 'left'
        # self.RIGHT = 'right'

        # instance of object gameWindow from class GameWindow
        self.gameWindow = gameWindow

        #start point
        self.x = [10]
        self.y = [10]
        #set the colour and size for drawing
        self.colour = self.gameWindow.YELLOW
        self.size = int(self.gameWindow.TILESIZE/2)
        #the score
        self.score = 0

    def movePlayer(self,direction):
        """
        Works out where player should go and starts draw process
        """
        if direction == 'UP':
            self.y[0] -= 1
        elif direction == 'DOWN':
            self.y[0] += 1
        elif direction == 'LEFT':
            self.x[0] -= 1
        elif direction == 'RIGHT':
            self.x[0] += 1




    def hitEdge(self):
        # Hit edge code not finished - A-Small-Being
        """
        Check to see if player has hit edge
        """
        if self.x[0] < 1:
            #too far left
            self.x[0] = 1
        elif self.x[0] > self.gameWindow.TILEWIDTH:
            # Too far right
            self.x[0] = self.gameWindow.TILEWIDTH
        elif self.y[0] == 0:
            # Too far up
            self.y[0] += 1
        elif self.y[0] == self.gameWindow.TILEHEIGHT+1:
            # Too far down
            self.y[0] -= 1
        else:
            # Fine
            return False
        return True
        

    def increaseScore(self):
        """
        increments the score
        """
        self.score += 1
