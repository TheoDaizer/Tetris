from turtle import position
import pygame

from constants import FALLINGSPEED, FASTFALLINGSPEED, GRIDWIDTH, GRIDHEIGHT, FPS, STARTING_POSITION

from point import Point
from figure import Figure


class Node:
    """Game field base object."""
    color = None

    def __repr__(self):
        return ('-', '+')[self.color is not None]

    def __init__(self):
        self.color = Node.color

    @property
    def is_active(self):
        return self.color is not None

    def clean(self):
        self.color = Node.color

    def update(self, color):
        self.color = color


class Field:
    """Class represents playing field.

    Args:
            width: playing field width
            height: playing field height
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.nodes = [[None for _ in range(width)] for _ in range(height)]
        self.rows_counter = [0] * height

    def update(self, shape, color):
        print("----------------")
        for pt in shape:
            x, y = int(pt.x), int(pt.y)

            self.nodes[y][x] = color
            self.rows_counter[y] += 1

            print("(" + str(x) + "," + str(y) + ") freezed")

        # print(*self.field.nodes, sep='\n')
        return self.check_row()

    def check_row(self) -> int:
        burned_rows = 0
        for row_n in range(self.height):
            if self.rows_counter[row_n] == self.width:
                burned_rows += 1
                self.rows_counter[row_n] = 0
                self.remove_row(row_n)
        return burned_rows

    def remove_row(self, row_n: int):
        self.clean_row(row_n)
        clean_row = self.nodes.pop(row_n)
        self.nodes = [clean_row] + self.nodes

        self.rows_counter.pop(row_n)
        self.rows_counter = [0] + self.rows_counter

    def clean_row(self, row_n: int):
        for i in range(self.width):
            self.nodes[row_n][i] = None


class Game:
    """Class that contains all essential game elements"""
    def __init__(self):
        self.field = Field(GRIDWIDTH, GRIDHEIGHT)
        self.figure = Figure(default_position=Point(STARTING_POSITION[0], STARTING_POSITION[1]))
        self.field_updated = False

        self.key_left = False
        self.key_right = False

        self.slide_limit = FPS // 20
        self.slide_counter = 0

    def update(self, dt: int):
        dx = (self.key_right - self.key_left)
        self.slide_counter += self.key_right or self.key_left
        if (self.slide_counter == self.slide_limit and
                not (self.check_collision(Point(dx, 0), self.figure.orientation))):
            self.slide_counter = 0
            delta = Point(dx, dt * self.figure.speed)
        else:
            delta = Point(0, dt * self.figure.speed)

        if self.check_collision(delta, self.figure.orientation):
            self.freeze_figure()
        else:
            self.figure.move(delta)

    def keyboard_input(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.key_left = True
                self.slide_counter = - FPS // 8
                delta = Point(-1, 0)
                if not (self.check_collision(delta, self.figure.orientation)):
                    self.figure.move(delta)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.key_right = True
                self.slide_counter = - FPS // 8
                delta = Point(1, 0)
                if not (self.check_collision(delta, self.figure.orientation)):
                    self.figure.move(delta)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.rotation_handler()

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.figure.speed = FASTFALLINGSPEED

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.figure.speed = FALLINGSPEED
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.key_left = False
                self.slide_counter = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.key_right = False
                self.slide_counter = 0
    
    def freeze_figure(self):
        """Update the field state with current shape and refresh figure."""
        burned_rows = self.field.update(self.figure.shape_position, self.figure.color)
        print('Burned rows: ', burned_rows)
        self.figure.refresh()
        self.field_updated = True

    def check_collision(self, delta: Point, orientation: int):
        """Check for horizontal collision. if there is a collision, the figure doesn't move"""
        if delta.y > 1:
            delta.y = 1

        new_position = self.figure.position + delta
        for pt in self.figure.shape[orientation]:
            point_position = new_position + pt
            if (not (0 <= point_position.x < GRIDWIDTH) or 
                not (0 <= point_position.y < GRIDHEIGHT) or
                    self.field.nodes[int(point_position.y)][int(point_position.x)] is not None):
                #print('Collided: ' + "(" + str(int(pt.x)) + "," + str(int(pt.y)) + ")")
                return True

        return False

    def rotation_handler(self,):
        """If figure can rotate - rotates figure"""
        orientation = (self.figure.orientation + 1) % len(self.figure.shape)
        delta = Point(0, 0)

        for pt in self.figure.shape[orientation]:
            point_position = self.figure.position + pt
            if(point_position.y < 0):
                delta += Point(0, 1)
            if(point_position.x < 0):
                delta += Point(1, 0)
            if(point_position.x >= GRIDWIDTH):
                delta += Point(-1, 0)

        if not self.check_collision(delta, orientation):
            self.figure.move(delta)
            self.figure.rotate()
        