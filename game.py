from constants import WINDOWHEIGHT
from constants import WINDOWWIDTH
import random as rnd
from point import Point
from figure import Figure, all_shapes

class Grid:
    """Class represents playing field"""

    def __init__(self, x: int, y: int):
        self.grid = [[False for _ in range(x)] for _ in range(y)]


class Game:
    """Class that contains all essential game elements"""

    def __init__(self):
        self.grid = Grid(WINDOWWIDTH, WINDOWHEIGHT)

        index = rnd.randrange(len(all_shapes));
        self.figure = Figure(all_shapes[index], Point(5,0), (255,0,0))


#class Node:
#    def __init__(self):
#        self.is_active = False
#        self.color = (0, 0, 0)
