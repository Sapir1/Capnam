import random, sys 
from pygame.locals import *
#import classes
from GameWindow import GameWindow
from Capnam import Capnam
from Pip import Pip
from Wall import Wall
from direction import Direction
from level_gen import gen_level

#we might want to divide this script up later or it will get really large and hard to read - Batrex

def checkcollision(obj1,obj2):
    """
    checks the collision between any two objects
    """

    if obj1.x == obj2.x and obj1.y == obj2.y:
        return True
    else:
        return False

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

    gen_level(gameWindow, walls, solid, pips)    

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
                    terminate()
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
            capnam.x = 10
            capnam.y = 10
            level += 1
            walls.clear()
            solid.clear()
            gen_level(gameWindow, walls, solid, pips)


        # Displays score on screen
        gameWindow.displayText(capnam.score, 0, 0)
        gameWindow.displayText(level, gameWindow.WINDOWWIDTH - (len(str(level))*15), 0)

        gameWindow.updatePygame()
        gameWindow.FPSCLOCK.tick(gameWindow.FPS)






if __name__ == '__main__':
    main()
