import random, pygame, sys
from pygame.locals import *
#import classes
from GameWindow import GameWindow
from Capnam import Capnam

#directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


def main():
    global gameWindow
    gameWindow = GameWindow()
    gameWindow.initialiseGame()
    gameWindow.drawGrid()

    while True:
        runGame()


def runGame():
    direction = 'RIGHT'
    capnam = Capnam(gameWindow)
    capnam.drawPlayer()
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            print(event)
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction = 'LEFT'
                elif event.key == K_RIGHT:
                    direction = 'RIGHT'
                elif event.key == K_UP:
                    direction = 'UP'
                elif event.key == K_DOWN:
                    direction = 'DOWN'
                elif event.key == K_ESCAPE:
                    terminate()
        capnam.movePlayer(direction)
        if capnam.hitEdge():
            capnam.drawPlayer()

        gameWindow.drawGrid()
        pygame.display.update()
        gameWindow.FPSCLOCK.tick(gameWindow.FPS)



def terminate():
    pygame.quit()
    sys.exit()



if __name__ == '__main__':
    main()
