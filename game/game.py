from typing import Optional
from constants import FALLINGSPEED, SPEED_INCREMENT, SPEEDMULTIPLIER, GRIDWIDTH, GRIDHEIGHT, FPS, STARTING_POSITION

from .field import Field
from .figure import Figure
from .point import Point
from .animation import Animation
from .animation import AnimationType


class Game:
    """Class that contains all essential game elements"""
    scores = (100, 300, 700, 1500)

    def __init__(self, seed: Optional[float] = None):
        self.field = Field(GRIDWIDTH, GRIDHEIGHT)
        self.figure = Figure(default_position=Point(STARTING_POSITION[0], STARTING_POSITION[1]), seed=seed)
        self.speed = FALLINGSPEED
        self.speed_multiplier = 1
        self.is_field_updated = False

        self.key_left = False
        self.key_right = False
        self.key_space = False
        self.key_down = False
        self.key_up = False

        self.slide_limit = FPS // 20
        self.slide_counter = 0

        self.score = 0
        self.level = 1
        self.burned_rows_total = 0
        self.burned_rows = 0
        self.is_game_over = False

        self.active_animations = []

    def update(self, time_delta: float):
        self.burned_rows = 0

        if self.key_up:
            self.rotation_handler()
            self.update_shadow()
            self.key_up = False

        if self.key_space:
            dropped_y = self.figure_drop()
            self.score += int(dropped_y) * 2
            self.burned_rows = self.freeze_figure()
            self.update_shadow()

        else:
            dx = self.key_right - self.key_left
            dy = time_delta * self.speed * self.speed_multiplier
            if dy > 1:
                dy = 1

            self.slide_counter += self.key_right or self.key_left
            if ((self.slide_counter == self.slide_limit or self.slide_counter == - FPS // 8 + 1) and
                    not (self.check_collision(Point(dx, 0), self.figure.orientation))):
                if self.slide_counter == self.slide_limit:
                    self.slide_counter = 0
                delta = Point(dx, dy)
            else:
                delta = Point(0, dy)

            if self.check_collision(delta, self.figure.orientation):
                self.burned_rows = self.freeze_figure()
                self.update_shadow()
            else:
                last_pos_y = self.figure.position.y
                self.figure.move(delta)
                if self.key_down and int(self.figure.position.y) - int(last_pos_y) >= 1:
                    self.score += 1
                if delta.x:
                    self.update_shadow()

        if self.burned_rows:
            self.burned_rows_total += self.burned_rows
            self.update_level()
            self.update_speed()
            self.update_burned_score(self.burned_rows)

        for animation in self.active_animations:
            if not animation[0].update(time_delta):
                self.active_animations.remove(animation)

        return self.dump()

    def key_left_down(self):
        self.key_left = True
        self.slide_counter = - FPS // 8

    def key_left_up(self):
        self.key_left = False
        self.slide_counter = 0

    def key_right_down(self):
        self.key_right = True
        self.slide_counter = - FPS // 8

    def key_right_up(self):
        self.key_right = False
        self.slide_counter = 0

    def key_up_down(self):
        self.key_up = True

    def key_down_down(self):
        self.key_down = True
        self.speed_multiplier = SPEEDMULTIPLIER

    def key_down_up(self):
        self.key_down = False
        self.speed_multiplier = 1

    def key_space_down(self):
        self.key_space = True
    
    def freeze_figure(self):
        """Update the field state with current shape and refresh figure."""
        burned_rows_pos = self.field.update(self.figure.position.x,
                                            int(self.figure.position.y),
                                            self.figure.shape_variant,
                                            self.figure.orientation
                                            )
        burned_rows = len(burned_rows_pos)
        for pt in self.figure.shape[self.figure.orientation]:
            pos = pt + self.figure.position
            if pos.y == 0 and not burned_rows:
                return self.game_over()
        self.figure.refresh()

        for row in burned_rows_pos:
            for column in range(GRIDWIDTH):
                self.active_animations.append((Animation(AnimationType.BURN_ANIMATION,
                                                         len(Animation.frames_container[AnimationType.BURN_ANIMATION])),
                                               (column, row)))

        self.is_field_updated = True
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
        """Rotate figure if possible"""
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
        self.level = self.burned_rows_total // 12 + 1

    def update_burned_score(self, burned_rows: int):
        self.score += self.scores[burned_rows - 1] * self.level // 2

    def update_speed(self):
        self.speed = FALLINGSPEED + SPEED_INCREMENT * (self.level - 1)

    def dump(self):
        data = GameDataContainer(game=self)
        self.is_field_updated = False
        return data

    def game_over(self):
        self.is_game_over = True
        self.is_field_updated = False
        self.burned_rows = 0


class GameDataContainer:
    def __init__(self, game: Game):
        self.figure_position = (game.figure.position.x, game.figure.position.y)
        self.shadow_position = (game.figure.shadow_position.x, game.figure.shadow_position.y)
        self.shape_variant = game.figure.shape_variant
        self.next_shape_variant = game.figure.next_shape_variant
        self.orientation = game.figure.orientation

        self.is_field_updated = game.is_field_updated
        self.field = game.field.nodes

        self.score = game.score
        self.level = game.level
        self.burned_rows_total = game.burned_rows_total
        self.burned_rows = game.burned_rows
        self.is_game_over = game.is_game_over

        self.active_animations = game.active_animations
