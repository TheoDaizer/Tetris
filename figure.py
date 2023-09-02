import random as rnd

from point import Point
from figures import *
from constants import FALLINGSPEED
from colors import *

all_shapes = (line_form, l_form_l, l_form_r, t_form, z_form_l, z_form_r, square_form)

all_colors = (RED, GREEN, BLUE, YELLOW, PINK, LIGHT_BLUE)


class Figure:
    """Class represents playing figures"""

    def __init__(self, default_position: Point, default_orientation: int = 0, default_speed: int = FALLINGSPEED):
        self.default_position = default_position
        self.default_orientation = default_orientation
        self.default_speed = default_speed

        self.position = None
        self.orientation = None
        self.speed = None
        self.color = None
        self.shape = None

        self.refresh()

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

    def refresh(self):
        index_shape = rnd.randrange(len(all_shapes))
        index_color = rnd.randrange(len(all_colors))

        self.position = self.default_position
        self.orientation = self.default_orientation
        self.speed = self.default_speed

        self.shape = [[Point(pt[0], pt[1]) for pt in a] for a in all_shapes[index_shape]]
        self.color = all_colors[index_color]
