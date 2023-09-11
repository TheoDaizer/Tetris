import random as rnd
from typing import Optional
from .point import Point
from .figures import *
from .colors import *

from constants import GRIDHEIGHT


class Figure:
    """Class represents playing figures"""
    tuple_shapes = (I_FORM, J_FORM, L_FORM, T_FORM, Z_FORM, S_FORM, O_FORM)

    all_shapes = [[[Point(pt[0], pt[1]) for pt in var] for var in shape] for shape in tuple_shapes]
    all_colors = (LIGHT_BLUE, BLUE, ORANGE, PINK, GREEN, RED, YELLOW)

    def __init__(self, default_position: Point, default_orientation: int = 0, seed: Optional[float] = None):
        rnd.seed(seed)

        self.default_position = default_position
        self.default_orientation = default_orientation
        self.default_shadow_position = Point(self.default_position.x, GRIDHEIGHT - 1)

        self.position = None
        self.orientation = None
        self.shadow_position = None
        self.color = None
        self.shape = None

        self.refresh()

    @property
    def shape_position(self):
        shape = self.shape[self.orientation]
        return [Point(self.position.x + pt.x, self.position.y + pt.y) for pt in shape]

    @property
    def shadow_shape_position(self):
        shape = self.shape[self.orientation]
        return [Point(self.shadow_position.x + pt.x, self.shadow_position.y + pt.y) for pt in shape]

    def rotate(self):
        self.orientation = (self.orientation + 1) % len(self.shape)

    def move(self, delta: Point):
        self.position = self.position + delta

    def refresh(self):
        self.position = self.default_position
        self.shadow_position = self.default_shadow_position
        self.orientation = self.default_orientation

        shape_var = rnd.randrange(len(self.all_shapes))
        self.shape = self.all_shapes[shape_var]
        self.color = self.all_colors[shape_var]
