from constants import WINDOWHEIGHT
from constants import WINDOWWIDTH
import random as rnd
from point import Point
from figure import Figure, allShapes

class Grid:

    def __init__(self, x: int, y: int):
        self.grid = [[False for _ in range(x)] for _ in range(y)]


class Game:

    def __init__(self):
        self.grid = Grid(WINDOWWIDTH, WINDOWHEIGHT)

        index = rnd.randrange(len(allShapes))
        self.figure = Figure(allShapes[index], Point(5, 0), (255, 0, 0))


class Node:
    def __init__(self):
        self.is_active = False
        self.color = (0, 0, 0)
