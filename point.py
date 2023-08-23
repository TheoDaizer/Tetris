

class Point:
    """Class for representing 2D vector"""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def add(self, point):
        self.x += point.x
        self.y += point.y

    def __repr__(self):
        return f'x:{self.x} y:{self.y}'
