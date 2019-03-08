#Game window class

#Import pygame - not sure what is needed here - A-Small-Being
import pygame, sys
from pygame.locals import *

class GameWindow:
    def __init__(self):
        #set variables
        self.FPS = 8
        self.WINDOWWIDTH = 640
        self.WINDOWHEIGHT = 640
        self.TILESIZE = 20
        #check it works
        assert self.WINDOWWIDTH % self.TILESIZE == 0, "Window width must be a multiple of tile size."
        assert self.WINDOWHEIGHT % self.TILESIZE == 0, "Window height must be a multiple of tile size."
        #Width and height in tiles
        self.TILEWIDTH = int(self.WINDOWWIDTH / self.TILESIZE)
        self.TILEHEIGHT = int(self.WINDOWHEIGHT / self.TILESIZE)

        #Colors       R    G    B
        self.WHITE     = (255, 255, 255)
        self.BLACK     = (  0,   0,   0)
        self.YELLOW    = (255, 255,   0)
        self.DARKGRAY  = ( 40,  40,  40)
        self.BGCOLOR = self.BLACK

    def initialiseGame(self):
        global FPSCLOCK, DISPLAYSURF
        pygame.init()
        self.FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        pygame.display.set_caption('Capnam')

    def drawGrid(self):
        """
        draws grid on screen
        """
        #fills background
        self.DISPLAYSURF.fill(self.BGCOLOR)
        #draws grid
        for x in range(0, self.WINDOWWIDTH, self.TILESIZE): # draw vertical lines
            pygame.draw.line(self.DISPLAYSURF, self.DARKGRAY, (x, 0), (x, self.WINDOWHEIGHT))
        for y in range(0, self.WINDOWHEIGHT, self.TILESIZE): # draw horizontal lines
            pygame.draw.line(self.DISPLAYSURF, self.DARKGRAY, (0, y), (self.WINDOWWIDTH, y))

    def drawCircle(self,pCoords):
        """
        Called from Main, draws circle on screen in x,y position
        """
        for coord in pCoords:
            self.x = coord['x'] * self.TILESIZE - 10 # Multiply to get pixels, subtract so centre lines up -> circle lines up with grid
            self.y = coord['y'] * self.TILESIZE - 10
            # I think this is the problem - A-Small-Being
            pygame.draw.circle(self.DISPLAYSURF, self.YELLOW, (self.x,self.y), 10)
