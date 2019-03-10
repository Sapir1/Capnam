import random, pygame, sys
from pygame.locals import *
#import classes
from GameWindow import GameWindow
from Capnam import Capnam
from pip import pip

#directions to be made ENUM? it would be needed in both main and Capnam, ideas? - A-Small-Being
# UP = 'up'
# DOWN = 'down'
# LEFT = 'left'
# RIGHT = 'right'

def checkcollision(obj1,obj2):
    """
    checks the collision between objects
    """
    if obj1.pCoords == obj2.pCoords:
        return True
    else:
        return False
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
    pips = []
    for x in range(gameWindow.TILEWIDTH):
        for y in range(gameWindow.TILEHEIGHT):
            pips.append(pip(gameWindow,x+1,y+1))
    #declare the font
    font = pygame.font.SysFont('Comic Sans MS', 30)
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
        gameWindow.drawGrid()
        #check for the pip and capnam colliding
        #we cant use the name pip here because that is already a class name
        for index,item in enumerate(pips):
            if checkcollision(item,capnam):
                capnam.increaseScore()
                del pips[index]

        #draw the pips
        for i in pips:
            i.drawObject()

        #draw and update the capnam
        if capnam.hitEdge():
            capnam.drawObject()
        else:
            capnam.movePlayer(direction)
            capnam.drawObject()

        #display the score
        capnam.displayScore(font)

        pygame.display.update()
        gameWindow.FPSCLOCK.tick(gameWindow.FPS)



def terminate():
    pygame.quit()
    sys.exit()



if __name__ == '__main__':
    main()
