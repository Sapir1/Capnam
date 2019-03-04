#player class

#import pygame
import random, pygame, sys
from pygame.locals import *

#import gameWindow object
# from GameWindow import drawCircle
#here we end up in an import loop

class Capnam:
    def __init__(self,gameWindow):
        # #directions
        # #this should be in main, and give direction as argument to movePlayer()
        # self.UP = 'up'
        # self.DOWN = 'down'
        # self.LEFT = 'left'
        # self.RIGHT = 'right'

        #start point
        self.startx = 10
        self.starty = 10
        self.gameWindow = gameWindow
        self.pCoords = [{'x': self.startx,'y': self.starty}] #Player coordinates

    def movePlayer(self,direction):
        """
        Works out where player should go and tells game window to redraw player
        """
        # self.pCoords = [{'x': self.startx,'y': self.starty}] #Player coordinates
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

        self.drawPlayer()

    def drawPlayer(self):
        """
        Tells main to tell GameWindow to draw player on screen
        """
        # self.pCoords.insert(0, self.newPos) #add new position
        # del self.pCoords[-1] # remove last position
        self.gameWindow.drawCircle(self.pCoords)

    def hitEdge(self):
        """
        Check to see if player has hit edge
        """
        if self.pCoords[0]['x'] == -1 or self.pCoords[0]['x'] == self.gameWindow.TILEWIDTH or self.pCoords[0]['y'] == -1 or self.pCoords[0]['y'] == self.gameWindow.TILEHEIGHT:
            #new position
            self.newPos = {'x': self.pCoords[0]['x'], 'y': self.pCoords[0]['y']}
            return True
        else:
            return False

    def show(self):
        """
        Debug function
        """
        print("Capnam is here to save the day")
