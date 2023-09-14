import pygame
from typing import Optional
from constants import FALLINGSPEED, SPEED_INCREMENT, SPEEDMULTIPLIER, GRIDWIDTH, GRIDHEIGHT, FPS, STARTING_POSITION

from .field import Field
from .figure import Figure
from .point import Point


class Game:
    """Class that contains all essential game elements"""
    scores = (100, 300, 700, 1500)

    def __init__(self, seed: Optional[float] = None):
        self.field = Field(GRIDWIDTH, GRIDHEIGHT)
        self.figure = Figure(default_position=Point(STARTING_POSITION[0], STARTING_POSITION[1]), seed=seed)
        self.speed = FALLINGSPEED
        self.speed_multiplier = 1
        self.field_updated = False

        self.key_left = False
        self.key_right = False
        self.key_space = False
        self.key_down = False

        self.slide_limit = FPS // 20
        self.slide_counter = 0

        self.score = 0
        self.level = 1
        self.burned_rows = 0
        self.is_burned = False
        self.game_over = False

    def update(self, dt: float):
        print(self.score)

        self.is_burned = False
        current_burned_rows = 0

        if self.key_space:
            dropped_y = self.figure_drop()
            self.score += int(dropped_y)
            current_burned_rows = self.freeze_figure()
            self.update_shadow()

        if not self.key_space:
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
                current_burned_rows = self.freeze_figure()
                self.update_shadow()
            else:
                self.figure.move(delta)
                if delta.x:
                    self.update_shadow()

        if current_burned_rows:
            self.is_burned = True
            self.burned_rows += current_burned_rows
            self.update_level()
            self.update_speed()
            self.update_burned_score(current_burned_rows)

    def keyboard_input(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.key_left = True
                self.slide_counter = - FPS // 8
                delta = Point(-1, 0)
                if not (self.check_collision(delta, self.figure.orientation)):
                    self.figure.move(delta)
                    self.update_shadow()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.key_right = True
                self.slide_counter = - FPS // 8
                delta = Point(1, 0)
                if not (self.check_collision(delta, self.figure.orientation)):
                    self.figure.move(delta)
                    self.update_shadow()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.rotation_handler()
                self.update_shadow()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.speed_multiplier = SPEEDMULTIPLIER
                self.key_down = True
            if event.key == pygame.K_SPACE:
                self.key_space = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.key_down = False
                self.speed_multiplier = 1
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.key_left = False
                self.slide_counter = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.key_right = False
                self.slide_counter = 0
    
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
        dy = self.figure.shadow_position.y - self.figure.position.y
        self.figure.move(Point(0, dy))
        self.key_space = False
        return dy

    def update_shadow(self):
        for field_y in range(int(self.figure.position.y) + 1, GRIDHEIGHT + 1):
            delta = Point(0, field_y - self.figure.position.y)
            if self.check_collision(delta, self.figure.orientation):
                self.figure.shadow_position = Point(self.figure.position.x, field_y - 1)
                break

    def update_level(self):
        self.level = self.burned_rows // 12 + 1

    def update_burned_score(self, burned_rows: int):
        self.score += Game.scores[burned_rows - 1] * self.level / 2

    def update_speed(self):
        self.speed = FALLINGSPEED + SPEED_INCREMENT * (self.level - 1)

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
