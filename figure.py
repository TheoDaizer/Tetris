from point import Point
from figures import *
from constants import FALLINGSPEED, GRIDSIZE

all_shapes = (line_form, l_form_l, l_form_r, t_form, z_form_l, z_form_r, square_form);

class Figure:
    """Class represents playing figures"""

    def __init__(self, shape: tuple, position: Point, color, orientation: int = 0, speed: int = FALLINGSPEED):
        self.shape = [[Point(pt[0],pt[1]) for pt in a] for a in shape]
        self.position = position
        self.orientation = orientation
        self.color = color
        self.speed = speed

    #move figure
    def move(self, delta: Point):
        new_position = self.position + delta;
        oriented_shape = self.shape[self.orientation]
        off_bounds = False

        for pt in oriented_shape:
            if ((new_position + pt).x < 0 or (new_position + pt).x >= GRIDSIZE[0] or (new_position + pt).y < 0 or (new_position + pt).y >= GRIDSIZE[1]):
                off_bounds = True

        if(off_bounds):
            return
        
        self.position = new_position


#square = Figure(square_form, Point(0, 0), (200, 100, 0), 0)
