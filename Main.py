import random, pygame, sys
from pygame.locals import *
#import classes
from GameWindow import GameWindow
from Capnam import Capnam

#directions to be made ENUM? it would be needed in both main and Capnam, ideas? - A-Small-Being
# UP = 'up'
# DOWN = 'down'
# LEFT = 'left'
# RIGHT = 'right'


def main():
    global gameWindow
    gameWindow = GameWindow()
    gameWindow.initialiseGame()
    gameWindow.drawGrid()

    while True:
        runGame()


# runGame might be adapted to be in Capnam() - A-Small-Being
def runGame():
    direction = 'RIGHT'
    # Hazel Move this!!!
    capnam = Capnam(gameWindow)
    capnam.drawObject()
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

        # This code doesn't work yet
        gameWindow.drawGrid()
        if capnam.hitEdge():
            capnam.drawObject()
        else:
            capnam.movePlayer(direction)
            capnam.drawObject()

        pygame.display.update()
        gameWindow.FPSCLOCK.tick(gameWindow.FPS)



def terminate():
    pygame.quit()
    sys.exit()



if __name__ == '__main__':
    main()
