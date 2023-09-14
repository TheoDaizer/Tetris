import pygame
from typing import Optional
from constants import FALLINGSPEED, SPEEDMULTIPLIER, GRIDWIDTH, GRIDHEIGHT, FPS, STARTING_POSITION

from .field import Field
from .figure import Figure
from .point import Point


class Game:
    """Class that contains all essential game elements"""
    def __init__(self, seed: Optional[float] = None):
        self.field = Field(GRIDWIDTH, GRIDHEIGHT)
        self.figure = Figure(default_position=Point(STARTING_POSITION[0], STARTING_POSITION[1]), seed=seed)
        self.speed = FALLINGSPEED
        self.speed_multiplier = 1
        self.field_updated = False

        self.key_left = False
        self.key_right = False
        self.key_space = False

        self.slide_limit = FPS // 20
        self.slide_counter = 0

        self.burned_rows = 0
        self.is_burned = False
        self.game_over = False

    def update(self, dt: float):
        self.is_burned = False
        if self.key_space:
            return self.figure_drop()

        dx = (self.key_right - self.key_left)
        dy = dt * self.speed * self.speed_multiplier
        if dy > 1:
            dy = 1

        self.slide_counter += self.key_right or self.key_left
        if (self.slide_counter == self.slide_limit and
                not (self.check_collision(Point(dx, 0), self.figure.orientation))):
            self.slide_counter = 0
            delta = Point(dx, dy)
        else:
            delta = Point(0, dy)

        if self.check_collision(delta, self.figure.orientation):
            self.freeze_figure()
            self.update_shadow()
        else:
            self.figure.move(delta)
            if delta.x:
                self.update_shadow()

    def key_left_down(self):
        self.key_left = True
        self.slide_counter = - FPS // 8
        delta = Point(-1, 0)
        if not (self.check_collision(delta, self.figure.orientation)):
            self.figure.move(delta)
            self.update_shadow()

    def key_left_up(self):
        self.key_left = False
        self.slide_counter = 0

    def key_right_down(self):
        self.key_right = True
        self.slide_counter = - FPS // 8
        delta = Point(1, 0)
        if not (self.check_collision(delta, self.figure.orientation)):
            self.figure.move(delta)
            self.update_shadow()

    def key_right_up(self):
        self.key_right = False
        self.slide_counter = 0

    def key_up_down(self):
        self.rotation_handler()
        self.update_shadow()

    def key_down_down(self):
        self.speed_multiplier = SPEEDMULTIPLIER

    def key_down_up(self):
        self.speed_multiplier = 1

    def key_space_down(self):
        self.key_space = True
    
    def freeze_figure(self):
        """Update the field state with current shape and refresh figure."""
        burned_rows = self.field.update(Figure.shape_position(self.figure.position,
                                                              self.figure.shape_variant,
                                                              self.figure.orientation), self.figure.color)
        print('Burned rows: ', burned_rows)
        for pt in self.figure.shape[self.figure.orientation]:
            pos = pt + self.figure.position
            if pos.y == 0 and not burned_rows:
                self.game_over = True
                break
        self.figure.refresh()
        if burned_rows:
            self.is_burned = True
            self.burned_rows += burned_rows
            print('Burned rows total: ', self.burned_rows)
            self.speed = FALLINGSPEED * (self.burned_rows // 10 + 1)
            print('Current speed: ', self.speed * 1000)

        self.field_updated = True
        return burned_rows

    def check_collision(self, delta: Point, orientation: int):
        """Check for horizontal collision. if there is a collision, the figure doesn't move"""

        new_position = self.figure.position + delta
        for pt in self.figure.shape[orientation]:
            point_position = new_position + pt
            if (not (0 <= point_position.x < GRIDWIDTH) or 
                not (0 <= point_position.y < GRIDHEIGHT) or
                    self.field.nodes[int(point_position.y)][int(point_position.x)] is not None):
                return True

        return False

    def rotation_handler(self):
        """If figure can rotate - rotates figure"""
        orientation = (self.figure.orientation + 1) % len(self.figure.shape)
        delta = Point(0, 0)

        for pt in self.figure.shape[orientation]:
            point_position = self.figure.position + pt
            if point_position.y < 0:
                delta += Point(0, 1)
            if point_position.x < 0:
                delta += Point(1, 0)
            if point_position.x >= GRIDWIDTH:
                delta += Point(-1, 0)

        if not self.check_collision(delta, orientation):
            self.figure.move(delta)
            self.figure.rotate()
       
    def figure_drop(self):
        self.figure.move(Point(0, self.figure.shadow_position.y - self.figure.position.y))
        self.freeze_figure()
        self.update_shadow()
        self.key_space = False

    def update_shadow(self):
        for field_y in range(int(self.figure.position.y) + 1, GRIDHEIGHT + 1):
            delta = Point(0, field_y - self.figure.position.y)
            if self.check_collision(delta, self.figure.orientation):
                self.figure.shadow_position = Point(self.figure.position.x, field_y - 1)
                break

    def dump(self):
        return GameDataContainer(game=self)


class GameDataContainer:
    def __init__(self, game: Game):
        self.figure_position = game.figure.position
        self.shadow_position = game.figure.shadow_position
        self.shape_variant = game.figure.shape_variant
        self.orientation = game.figure.orientation
        self.field = None
        if game.field_updated:
            game.field_updated = False
            self.field = game.field.nodes
