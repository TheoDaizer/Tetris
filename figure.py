from point import Point
from figures import *

all_shapes = (line_form, l_form_l, l_form_r, t_form, z_form_l, z_form_r, square_form);

class Figure:
    """Class represents playing figures"""

    def __init__(self, shape: tuple, position: Point, color, orientation: int = 0):
        self.shape = [[Point(pt[0],pt[1]) for pt in a] for a in shape]
        self.position = position
        self.orientation = orientation
        self.color = color

    def move(self, delta: Point):
        self.position += delta


#square = Figure(square_form, Point(0, 0), (200, 100, 0), 0)
