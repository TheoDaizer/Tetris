from point import Point
from figures import *

line_shape = [
    (Point(-1,0), Point(0,0), Point(1,0), Point(2,0)),
    (Point(-1,0), Point(0,0), Point(1,0), Point(2,0)),
    (Point(-1,0), Point(0,0), Point(1,0), Point(2,0)),
    (Point(-1,0), Point(0,0), Point(1,0), Point(2,0)),
    ];


all_shapes = (line_shape, );


class Figure:
    """Class represents playing figures"""

    def __init__(self, shape: list, position: Point, color, orientation: int = 0):
        self.shape = shape
        self.position = position
        self.orientation = orientation
        self.color = color

    def move(self, delta: Point):
        self.position.add(delta)


square = Figure(square_form, Point(0, 0), (200, 100, 0), 0)
