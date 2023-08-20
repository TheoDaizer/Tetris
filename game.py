#import constants
from constants import WINDOWHEIGHT
from constants import WINDOWWIDTH

class Grid:

    def __init__(self, x: int, y: int):
        self.grid = [[False for _ in range(x)] for _ in range(y)];


class Game:
    def __init__(self):
        self.grid = Grid(WINDOWWIDTH, WINDOWHEIGHT)
    


#grid = Grid(10,20)
#print(*grid.grid, sep='\n')

#class Game:
    