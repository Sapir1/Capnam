#this file contains general functions

from GameWindow import GameWindow
import random
from Pip import Pip
from Wall import Wall
from direction import Direction

def genlevel(gameWindow, walls, solid, pips):
    """
    generates a new level
    """
    #do we want to make this a pure function - batrex

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

def checkcollision(obj1,obj2):
    """
    checks the collision between any two objects
    """

    if obj1.x == obj2.x and obj1.y == obj2.y:
        return True
    else:
        return False
