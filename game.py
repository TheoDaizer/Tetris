import pygame
import random as rnd
from copy import deepcopy

from constants import FALLINGSPEED, FASTFALLINGSPEED, WINDOWHEIGHT, WINDOWWIDTH, GRIDWIDTH, GRIDHEIGHT

from point import Point
from figure import Figure, all_shapes, all_colors
from colors import BLACK, RED


class Node:
    """Game field base object."""
    color = BLACK

    def __repr__(self):
        return ('-', '+')[self.is_active]

    def __init__(self):
        self.is_active = False
        self.color = Node.color

    def clean(self):
        self.is_active = False
        self.color = Node.color


class Field:
    """Class represents playing field.

    Args:
            width: playing field width
            height: playing field height
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.nodes = [[Node() for _ in range(width)] for _ in range(height)]
        # for x in range(1,10):
        #    for y in range(6,20):
        #        self.nodes[x][y] = Node(True, RED)
        # self.nodes[9][6] = Node(False)
        # self.nodes[4][5] = Node(True, RED)
        # self.nodes[5][5] = Node(True, RED)
        # self.nodes[6][5] = Node(True, RED)
        # self.nodes[7][5] = Node(True, RED)
        # self.nodes[8][5] = Node(True, RED)

    def update(self):
        """Update playing field nodes' state."""
        for y in range(self.height):
            is_full_line = True

            for x in range(self.width):
                if not self.nodes[y][x].is_active:
                    is_full_line = False
                    break

            if is_full_line:
                self.remove_row(y)

    def clean_row(self, row_n: int):
        for node in self.nodes[row_n]:
            node.clean()

    def remove_row(self, row_n: int):
        self.clean_row(row_n)
        clean_row = self.nodes.pop(row_n)
        self.nodes = [clean_row] + self.nodes


class Game:
    """Class that contains all essential game elements"""

    def __init__(self):
        self.field = Field(GRIDWIDTH, GRIDHEIGHT)

        index_shape = rnd.randrange(len(all_shapes))
        index_color = rnd.randrange(len(all_colors))
        self.figure = Figure(all_shapes[index_shape], Point(4, 0), all_colors[index_color])

    def update(self, dt: int):
        delta = Point(0, dt * self.figure.speed)
        if self.check_vert_collision(delta, self.figure.orientation):
            self.freeze_figure()
            self.field.update()
        else:
            self.figure.move(delta)

    def keyboard_input(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                delta = Point(-1, 0)
                if not (self.check_hor_collision(delta, self.figure.orientation)):
                    self.figure.move(delta)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                delta = Point(1, 0)
                if not (self.check_hor_collision(delta, self.figure.orientation)):
                    self.figure.move(delta)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                delta = Point(0, 0)
                orientation = (self.figure.orientation + 1) % len(self.figure.shape)
                if not self.check_hor_collision(delta, orientation) and not self.check_vert_collision(delta, orientation):
                    self.figure.rotate()

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.figure.speed = FASTFALLINGSPEED

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.figure.speed = FALLINGSPEED
    
    def freeze_figure(self):
        """Creates new figure, updates the field state with previous "freezed" figure"""
        print("----------------")
        for pt in self.figure.shape[self.figure.orientation]:
            pos = pt + self.figure.position
            self.field.nodes[int(pos.y)][int(pos.x)].is_active = True
            self.field.nodes[int(pos.y)][int(pos.x)].color = self.figure.color
            print("(" + str(int(pos.x)) + "," + str(int(pos.y)) + ") freezed")

        # print(*self.field.nodes, sep='\n')

        index_shape = rnd.randrange(len(all_shapes))
        index_color = rnd.randrange(len(all_colors))
        self.figure = Figure(all_shapes[index_shape], Point(4, 0), all_colors[index_color])

    def check_hor_collision(self, delta: Point, orientation: int):
        """Check for horizontal collision. if there is a collision, the figure doesnt move"""
        if delta.y > 1:
            delta.y = 1

        new_position = self.figure.position + delta
        for pt in self.figure.shape[orientation]:
            point_position = new_position + pt
            if (not (0 <= point_position.x < GRIDWIDTH) or
                    self.field.nodes[int(point_position.y)][int(point_position.x)].is_active):
                return True
        return False

    def check_vert_collision(self, delta: Point, orientation: int):
        """Check for vert collision. if there is a collision, new figure creates and fields state updates"""
        if delta.y > 1:
            delta.y = 1

        new_position = self.figure.position + delta
        for pt in self.figure.shape[orientation]:
            point_position = new_position + pt
            if (not (0 <= point_position.y < GRIDHEIGHT) or
                    self.field.nodes[int(point_position.y)][int(point_position.x)].is_active):
                return True
        return False
