from point import Point
from figures import *
from constants import FALLINGSPEED, GRIDWIDTH, GRIDHEIGHT
from colors import *

all_shapes = (line_form, l_form_l, l_form_r, t_form, z_form_l, z_form_r, square_form)
all_colors = (RED, GREEN, BLUE, YELLOW, LIGHT_BLUE, PINK)

class Figure:
    """Class represents playing figures"""

    def __init__(self, shape: tuple, position: Point, color, orientation: int = 0, speed: int = FALLINGSPEED):
        self.shape = [[Point(pt[0], pt[1]) for pt in a] for a in shape]
        self.position = position
        self.orientation = orientation
        self.color = color
        self.speed = speed

    def rotate(self, clockwise: bool):
        if clockwise:
            self.orientation = x if (x := self.orientation + 1) < 4 else 0
        else:
            self.orientation = x if (x := self.orientation - 1) >= 0 else 3

    #return True if figure freezes and game needs to create new figure
    def move(self, delta: Point):
        if(delta.y > 1):
            delta.y = 1

        new_position = self.position + delta

        for pt in self.shape[self.orientation]:
            point_position = new_position + pt
            if not (0 <= point_position.x < GRIDWIDTH) or not (0 <= point_position.y):
                return False
            if not ( point_position.y < GRIDHEIGHT):
                return True

        self.position = new_position
