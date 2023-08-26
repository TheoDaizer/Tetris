import sys


class Point:
    """Class for representing 2D vector"""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __repr__(self):
        return f'x:{self.x} y:{self.y}'


if __name__ == '__main__':
    p = Point(2, 3)
    p2 = 2
    print(sys.getsizeof(p))
    print(sys.getsizeof(p2))
