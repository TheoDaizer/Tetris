import random
from typing import Optional
from .point import Point
from .figures import *
from .colors import *

from constants import GRIDHEIGHT


class Figure:
    """Class represents playing figures"""
    tuple_shapes = (I_FORM, J_FORM, L_FORM, T_FORM, Z_FORM, S_FORM, O_FORM)

    all_shapes = [[[Point(pt[0], pt[1]) for pt in var] for var in shape] for shape in tuple_shapes]
    all_colors = (LIGHT_BLUE, BLUE, ORANGE, PURPLE, GREEN, RED, YELLOW)

    def __init__(self, default_position: Point, default_orientation: int = 0, seed: Optional[float] = None):
        self.rnd = random.Random()
        self.rnd.seed(seed)

        self.default_position = default_position
        self.default_orientation = default_orientation
        self.default_shadow_position = Point(self.default_position.x, GRIDHEIGHT - 2)

        self.position = None
        self.orientation = None
        self.shape_variant = None

        self.shadow_position = None

        self.next_shape_variant = self.rnd.randrange(len(self.all_shapes))

        self.refresh()

    @staticmethod
    def shape_position(position: Point, shape_variant: int, orientation: int):
        shape = Figure.all_shapes[shape_variant][orientation]
        return [Point(position.x + pt.x, position.y + pt.y) for pt in shape]

    @property
    def shape(self):
        return self.all_shapes[self.shape_variant]

    @property
    def next_shape(self):
        return self.all_shapes[self.next_shape_variant]

    @property
    def color(self):
        return self.all_colors[self.shape_variant]

    @property
    def next_color(self):
        return self.all_colors[self.next_shape_variant]

    def rotate(self):
        self.orientation = (self.orientation + 1) % len(self.shape)

    def move(self, delta: Point):
        self.position = self.position + delta

    def refresh(self):
        self.position = self.default_position
        self.shadow_position = self.default_shadow_position
        self.orientation = self.default_orientation

        self.shape_variant = self.next_shape_variant
        self.next_shape_variant = self.rnd.randrange(len(self.all_shapes))
