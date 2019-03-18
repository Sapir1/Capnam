from enum import Enum

class Direction(Enum):
    UP = ('UP', -1)
    DOWN = ('DOWN', 1)
    LEFT = ('LEFT', -1)
    RIGHT = ('RIGHT', 1)