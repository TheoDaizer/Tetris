from point import Point
from figures import *
from constants import FALLINGSPEED
from colors import *

all_shapes = (line_form, l_form_l, l_form_r, t_form, z_form_l, z_form_r, square_form)

all_colors = (RED, GREEN, BLUE, YELLOW, PINK, LIGHT_BLUE)


class Figure:
    """Class represents playing figures"""

    def __init__(self, shape: tuple, position: Point, color, orientation: int = 0, speed: int = FALLINGSPEED):
        self.shape = [[Point(pt[0], pt[1]) for pt in a] for a in shape]
        self.position = position
        self.orientation = orientation
        self.color = color
        self.speed = speed

    @property
    def shape_position(self):
        shape = self.shape[self.orientation]
        return [Point(self.position.x + pt.x, self.position.y + pt.y) for pt in shape]

    def rotate(self):
        self.orientation = (self.orientation + 1) % len(self.shape)

    def move(self, delta: Point):
        if delta.y > 1:
            delta.y = 1

        self.position = self.position + delta
