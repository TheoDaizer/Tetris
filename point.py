

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def add(self, point):
        self.x += point.x
        self.y += point.y