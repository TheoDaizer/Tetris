from constants import FALLINGSPEED, FASTFALLINGSPEED, WINDOWHEIGHT, WINDOWWIDTH
import random as rnd
import pygame
from point import Point
from figure import Figure, all_shapes

class Field:
    """Class represents playing field"""

    def __init__(self, x: int, y: int):
        self.cells = [[False for _ in range(x)] for _ in range(y)]


class Game:
    """Class that contains all essential game elements"""

    def __init__(self):
        self.field = Field(WINDOWWIDTH, WINDOWHEIGHT)

        index = rnd.randrange(len(all_shapes));
        self.figure = Figure(all_shapes[index], Point(5,0), (255,0,0))

    def update(self, dt :int):
        self.figure.move(Point(0, dt * self.figure.speed))
    
    def keyboard_input(self, event):
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                self.figure.move(Point(-1, 0))
            elif(event.key == pygame.K_RIGHT):
                self.figure.move(Point(1, 0))
            elif(event.key == pygame.K_DOWN):
                self.figure.speed = FASTFALLINGSPEED;
        elif(event.type == pygame.KEYUP):
            if(event.key == pygame.K_DOWN):
                self.figure.speed = FALLINGSPEED;

#class Node:
#    def __init__(self):
#        self.is_active = False
#        self.color = (0, 0, 0)
