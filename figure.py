from point import Point
from figures import *


class Figure:
    def __init__(self, shape: tuple, position: Point, color, orientation: int = 0):
        self.shape = [[Point(x, y) for x, y in form] for form in shape]
        self.position = position
        self.orientation = orientation
        self.color = color

    def move(self, delta: Point):
        self.position.add(delta)


square = Figure(square_form, Point(0, 0), (200, 100, 0), 0)
