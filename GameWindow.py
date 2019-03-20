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
        self.TILESIZE = 40
        #check it works
        assert self.WINDOWWIDTH % self.TILESIZE == 0, "Window width must be a multiple of tile size."
        assert self.WINDOWHEIGHT % self.TILESIZE == 0, "Window height must be a multiple of tile size."
        #Width and height in tiles
        self.TILEWIDTH = int(self.WINDOWWIDTH / self.TILESIZE)
        self.TILEHEIGHT = int(self.WINDOWHEIGHT / self.TILESIZE)

        #Colors            R    G    B
        self.WHITE     = (255, 255, 255)
        self.BLACK     = (  0,   0,   0)
        self.BLUE      = (  0,   0, 255)
        self.RED       = (255,   0,   0)
        self.YELLOW    = (255, 255,   0)
        self.DARKGRAY  = ( 40,  40,  40)
        self.BGCOLOR = self.BLACK

    def initialiseGame(self):
        global FPSCLOCK, DISPLAYSURF
        pygame.init()
        pygame.font.init()
        self.FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        pygame.display.set_caption('Capnam')
        #declare the font
        self.font = pygame.font.SysFont('calibri', 30)

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

    # def drawCircle(self,pCoords,color):
    #     """
    #     Called from Main, draws circle on screen in x,y position
    #     """
    #     for coord in pCoords:
    #         self.x = coord['x'] * self.TILESIZE - 10 # Multiply to get pixels, subtract so centre lines up -> circle lines up with grid
    #         self.y = coord['y'] * self.TILESIZE - 10
    #         pygame.draw.circle(self.DISPLAYSURF, self.YELLOW, (self.x,self.y), 10)

    def displayText(self,text):
        """
        displays the score as text
        """
        #first rendering the text onto a surface
        textSurface = self.font.render(str(text),True,self.RED)
        #then displaying that to the main display surface
        self.DISPLAYSURF.blit(textSurface,(0,0))

    def drawCircle(self,x,y,colour,size):
        """
        draws a circle
        """
        # Multiply to get pixels, subtract so centre lines up -> circle lines up with grid
        xcoord = x * self.TILESIZE - int(self.TILESIZE/2)
        ycoord = y * self.TILESIZE - int(self.TILESIZE/2)
        pygame.draw.circle(self.DISPLAYSURF, colour, (xcoord,ycoord), size)
    
    def drawRect(self,x,y,colour,size):
        """
        draws a rectangle
        """
        # Multiply to get pixels, subtract so corner lines up -> rectangle is drawn in correct tile
        xcoord = x * self.TILESIZE - self.TILESIZE
        ycoord = y * self.TILESIZE - self.TILESIZE
        
        pygame.draw.rect(self.DISPLAYSURF, colour, (xcoord,ycoord,size,size))

