import random, sys
from pygame.locals import *
#import classes
from GameWindow import GameWindow
from Capnam import Capnam
from Pip import Pip
from Wall import Wall
from direction import Direction
from Functions import *

def main():
    global gameWindow
    gameWindow = GameWindow()
    global capnam
    capnam = Capnam(gameWindow)

    gameWindow.initialiseGame()
    gameWindow.drawGrid()

    while True:
        runGame()

def runGame():
    direction = Direction.RIGHT
    level = 0
    walls = []
    solid = []
    pips = []

    genlevel(gameWindow, walls, solid, pips)

    # main game loop
    while True:
        events = gameWindow.getEvents()
        for event in events: # event handling loop
            print(event)
            if event.type == QUIT:
                gameWindow.terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction = Direction.LEFT
                elif event.key == K_RIGHT:
                    direction = Direction.RIGHT
                elif event.key == K_UP:
                    direction = Direction.UP
                elif event.key == K_DOWN:
                    direction = Direction.DOWN
                elif event.key == K_ESCAPE:
                    gameWindow.terminate()
        #draw the grid
        gameWindow.drawGrid()
        #check for the pips and capnam colliding
        for index,pip in enumerate(pips):
            if checkcollision(pip,capnam):
                capnam.increaseScore()
                del pips[index]


        #draw the walls
        for i in walls:
            i.draw()

        #draw the pips
        for i in pips:
            i.draw()


        #draw and update the capnam
        if capnam.hitDetect(direction, solid):
            capnam.draw()
        else:
            capnam.movePlayer(direction)
            capnam.draw()

        #Generate a new level once no pips left, resetting capnam
        if len(pips) == 0:
            direction = Direction.RIGHT
            capnam.x = capnam.startx
            capnam.y = capnam.startx
            level += 1
            walls.clear()
            solid.clear()
            genlevel(gameWindow, walls, solid, pips)


        # Displays score on screen
        gameWindow.displayText(capnam.score, 0, 0)
        gameWindow.displayText(level, gameWindow.WINDOWWIDTH - (len(str(level))*15), 0)

        gameWindow.updatePygame()
        gameWindow.FPSCLOCK.tick(gameWindow.FPS)






if __name__ == '__main__':
    main()
