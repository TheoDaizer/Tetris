import random as rnd

from point import Point
from figures import *
from constants import FALLINGSPEED
from colors import *


class Figure:
    """Class represents playing figures"""
    tuple_shapes = (line_form, l_form_l, l_form_r, t_form, z_form_l, z_form_r, square_form)

    all_shapes = [[[Point(pt[0], pt[1]) for pt in var] for var in shape] for shape in tuple_shapes]
    all_colors = (RED, GREEN, BLUE, YELLOW, PINK, LIGHT_BLUE)

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
        self.position = self.default_position
        self.orientation = self.default_orientation
        self.speed = self.default_speed

        self.shape = rnd.choice(self.all_shapes)
        self.color = rnd.choice(self.all_colors)
