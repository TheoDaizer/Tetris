from constants import FALLINGSPEED, FASTFALLINGSPEED, WINDOWHEIGHT, WINDOWWIDTH, GRIDWIDTH, GRIDHEIGHT
import random as rnd
import pygame
from point import Point
from figure import Figure, all_shapes, all_colors


class Node:
    def __init__(self, state = False, color = (0, 0, 0)):
        self.is_active = False
        self.color = (0, 0, 0)

class Field:
    """Class represents playing field"""

    def __init__(self, x: int, y: int):
        self.cells = [[Node() for _ in range(x)] for _ in range(y)]


class Game:
    """Class that contains all essential game elements"""

    def __init__(self):
        self.field = Field(WINDOWWIDTH, WINDOWHEIGHT)

        index_shape = rnd.randrange(len(all_shapes))
        index_color = rnd.randrange(len(all_colors))
        self.figure = Figure(all_shapes[index_shape], Point(4, 0), all_colors[index_color])

    def update(self, dt: int):
        delta = Point(0, dt * self.figure.speed)
        if(self.check_vert_collision(delta)):
            self.freeze_figure()
        else:
            self.figure.move(delta)

    def keyboard_input(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                delta = Point(-1, 0)
                if not (self.check_hor_collision(delta)):
                    self.figure.move(delta)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                delta = Point(1, 0)
                if not (self.check_hor_collision(delta)):
                    self.figure.move(delta)
            if event.key == pygame.K_q:
                self.figure.rotate(False)
            if event.key == pygame.K_e:
                self.figure.rotate(True)

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.figure.speed = FASTFALLINGSPEED
            #if event.key == pygame.K_UP:
            #    self.figure.move(Point(0, -1))

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.figure.speed = FALLINGSPEED

    def freeze_figure(self):
        for pt in self.figure.shape[self.figure.orientation]:
            pos = pt + self.figure.position;
            self.field.cells[int(pos.x)][int(pos.y)].is_active = True
            self.field.cells[int(pos.x)][int(pos.y)].color = self.figure.color

        index_shape = rnd.randrange(len(all_shapes))
        index_color = rnd.randrange(len(all_colors))
        self.figure = Figure(all_shapes[index_shape], Point(4, 0), all_colors[index_color])

    # check for horizontal collision. if there is a collision, the figure doesnt move
    def check_hor_collision(self, delta: Point):
        if(delta.y > 1):
            delta.y = 1

        new_position = self.figure.position + delta
        for pt in self.figure.shape[self.figure.orientation]:
            point_position = new_position + pt
            if not (0 <= point_position.x < GRIDWIDTH) or (self.field.cells[int(point_position.x)][int(point_position.y)].is_active):
                return True
        return False

    # check for vert collision. if there is a collision, new figure creates and fiels state updates
    def check_vert_collision(self, delta: Point):
        if(delta.y > 1):
            delta.y = 1

        new_position = self.figure.position + delta
        for pt in self.figure.shape[self.figure.orientation]:
            point_position = new_position + pt
            if not (0 <= point_position.y < GRIDHEIGHT) or (self.field.cells[int(point_position.x)][int(point_position.y)].is_active):
                return True
        return False