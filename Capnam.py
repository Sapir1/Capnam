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
        self.startx = 10
        self.starty = 10
        self.pCoords = [{'x': self.startx,'y': self.starty}] #Player coordinates
        #set the colour and size for drawing
        self.colour = self.gameWindow.YELLOW
        self.size = int(self.gameWindow.TILESIZE/2)
        #the score
        self.score = 0

    def movePlayer(self,direction):
        """
        Works out where player should go and starts draw process
        """
        #is there a reason for adding this variable newpos? why not just change the position - Batrex
        if direction == 'UP':
            self.newPos = {'x': self.pCoords[0]['x'], 'y': self.pCoords[0]['y'] - 1}
        elif direction == 'DOWN':
            self.newPos = {'x': self.pCoords[0]['x'], 'y': self.pCoords[0]['y'] + 1}
        elif direction == 'LEFT':
            self.newPos = {'x': self.pCoords[0]['x'] - 1, 'y': self.pCoords[0]['y']}
        elif direction == 'RIGHT':
            self.newPos = {'x': self.pCoords[0]['x'] + 1, 'y': self.pCoords[0]['y']}

        self.pCoords.insert(0, self.newPos) #add new position
        del self.pCoords[-1] # remove last position



    def hitEdge(self):
        # Hit edge code not finished - A-Small-Being
        """
        Check to see if player has hit edge
        """
        if self.pCoords[0]['x'] == 0:
            #too far left
            self.newPos = {'x': self.pCoords[0]['x'] + 1, 'y': self.pCoords[0]['y']}
        elif self.pCoords[0]['x'] == self.gameWindow.TILEWIDTH+1:
            # Too far right
            self.newPos = {'x': self.pCoords[0]['x'] - 1, 'y': self.pCoords[0]['y']}
        elif self.pCoords[0]['y'] == 0:
            # Too far up
            self.newPos = {'x': self.pCoords[0]['x'], 'y': self.pCoords[0]['y'] + 1}
        elif self.pCoords[0]['y'] == self.gameWindow.TILEHEIGHT+1:
            # Too far down
            self.newPos = {'x': self.pCoords[0]['x'], 'y': self.pCoords[0]['y'] - 1}
        else:
            # Fine
            return False
        self.pCoords.insert(0,self.newPos)
        del self.pCoords[-1]
        return True

    def increaseScore(self):
        """
        increments the score
        """
        self.score += 1
