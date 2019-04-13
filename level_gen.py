from GameWindow import GameWindow
import random
from Pip import Pip
from Wall import Wall
from direction import Direction

def gen_level(gameWindow, walls, solid, pips):  
    #create the walls
    for x in range(1, gameWindow.TILEWIDTH + 1):
        for y in range(1, gameWindow.TILEHEIGHT + 1):
            if random.randint(0, 10) == 0:
                walls.append(Wall(gameWindow,x,y))
    #define and fill solids
    for wall in walls:
        solid.append((wall.x, wall.y))

    #create the Pips
    for x in range(1, gameWindow.TILEWIDTH + 1):
        for y in range(1, gameWindow.TILEHEIGHT + 1):
                if (x, y) not in solid:
                    pips.append(Pip(gameWindow,x,y))

