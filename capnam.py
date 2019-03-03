import random, pygame, sys
from pygame.locals import *

#setup
FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 640
TILESIZE = 20
assert WINDOWWIDTH % TILESIZE == 0, "Window width must be a multiple of TILE size."
assert WINDOWHEIGHT % TILESIZE == 0, "Window height must be a multiple of TILE size."
TILEWIDTH = int(WINDOWWIDTH / TILESIZE)
TILEHEIGHT = int(WINDOWHEIGHT / TILESIZE)

#Colors       R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
YELLOW    = (255, 255,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0

def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Capnam')

    
    while True:
        runGame()


def runGame():
    # Start point
    startx = 10
    starty = 10
    pCoords = [{'x': startx,'y': starty}] #Player coordinates
    direction = RIGHT


    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            print(event)
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction = LEFT
                elif event.key == K_RIGHT:
                    direction = RIGHT
                elif event.key == K_UP:
                    direction = UP
                elif event.key == K_DOWN:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # check if theplayer has hit the edge
        if pCoords[HEAD]['x'] == -1 or pCoords[HEAD]['x'] == TILEWIDTH or pCoords[HEAD]['y'] == -1 or pCoords[HEAD]['y'] == TILEHEIGHT:
            newPos = {'x': pCoords[HEAD]['x'], 'y': pCoords[HEAD]['y']}


        # move the player
        if direction == UP:
            newPos = {'x': pCoords[HEAD]['x'], 'y': pCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newPos = {'x': pCoords[HEAD]['x'], 'y': pCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newPos = {'x': pCoords[HEAD]['x'] - 1, 'y': pCoords[HEAD]['y']}
        elif direction == RIGHT:
            newPos = {'x': pCoords[HEAD]['x'] + 1, 'y': pCoords[HEAD]['y']}
        pCoords.insert(0, newPos) #add new position
        del pCoords[-1] # remove last position
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawPlayer(pCoords)
        pygame.display.update()
        FPSCLOCK.tick(FPS)



def terminate():
    pygame.quit()
    sys.exit()


def drawPlayer(pCoords):
    for coord in pCoords:
        x = coord['x'] * TILESIZE - 10 # Multiply to get pixels, subtract so centre lines up -> circle lines up with grid
        y = coord['y'] * TILESIZE - 10
        pygame.draw.circle(DISPLAYSURF, YELLOW, (x,y), 10)
    

def drawGrid():
    for x in range(0, WINDOWWIDTH, TILESIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, TILESIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    main()
