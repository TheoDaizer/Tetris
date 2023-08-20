from point import Point

lineShape = [(Point(-1,0), Point(0,0), Point(1,0), Point(2,0)),
             (Point(-1,0), Point(0,0), Point(1,0), Point(2,0)),
             (Point(-1,0), Point(0,0), Point(1,0), Point(2,0)),
             (Point(-1,0), Point(0,0), Point(1,0), Point(2,0)),
             ];


allShapes = (lineShape, );


class Figure:

    def __init__(self, shape: list, position: Point, color, orientation: int = 0):
        self.shape = shape
        self.position = position
        self.orientation = orientation
        self.color = color

    def move(self, delta: Point):
        #проверки
        self.position.add(delta)