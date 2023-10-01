import pygame
from typing import Optional

from pygame.surface import Surface
from .figures import SHAPES
from .colors import COLORS
from constants import TILESIZE, FIELDWIDTH, FIELDHEIGHT, GRIDHEIGHT, GRIDWIDTH
from .game import GameDataContainer
from .animation import Animation

GRID_COLOR = (100, 100, 100)


class GameFieldRenderer:
    block_image = pygame.image.load("resources/tetris_block.png")
    block_shadow_image = pygame.image.load("resources/tetris_block_shadow.png")
    bg_image = pygame.image.load("resources/background_col.png")

    def __init__(self):
        self.game_surface: Surface = Surface((FIELDWIDTH, FIELDHEIGHT))
        self.field_surfaces: Surface = Surface((FIELDWIDTH, FIELDHEIGHT))
        self.figure_surfaces: Surface = Surface((FIELDWIDTH, FIELDHEIGHT), pygame.SRCALPHA)

        self.animations_surfaces: Surface = Surface((FIELDWIDTH, FIELDHEIGHT), pygame.SRCALPHA)

        self.grid_surface = pygame.Surface((FIELDWIDTH, FIELDHEIGHT), pygame.SRCALPHA)
        self.draw_grid()

        self.game_surface.blit(self.bg_image, (0, 0))
        self.field_surfaces.blit(self.bg_image, (0, 0))
        self.figure_surfaces.blit(self.bg_image, (0, 0))

        self.field: list = [[None for _ in range(FIELDWIDTH)] for _ in range(FIELDHEIGHT)]

    def draw_grid(self):
        self.grid_surface.fill((255, 255, 255, 0))
        for x, y in ((x, y) for y in range(GRIDHEIGHT) for x in range(GRIDWIDTH)):
            pygame.draw.line(self.grid_surface, GRID_COLOR, (x * TILESIZE, y * TILESIZE),
                             (x * TILESIZE, (y + 1) * TILESIZE))
            pygame.draw.line(self.grid_surface, GRID_COLOR, (x * TILESIZE, y * TILESIZE),
                             ((x + 1) * TILESIZE, y * TILESIZE))

    def render(self, game_data: GameDataContainer):
        """Main rendering function, that call other renderers"""

        if game_data.is_field_updated:
            self.field = game_data.field
            self.field_surfaces.blit(self.bg_image, (0, 0))
            self.render_field(game_data.field)

        self.figure_surfaces.blit(self.field_surfaces, (0, 0))
        self.render_shadow(game_data.shadow_position, game_data.shape_variant, game_data.orientation)
        self.render_figure(game_data.figure_position, game_data.shape_variant, game_data.orientation)

        self.animations_surfaces.fill((0, 0, 0, 0))
        self.render_animations(game_data.active_animations)

        return self.render_game_screen()

    def render_block(self, surface, position: tuple[int, int], shape_variant: int, x_shift: bool = False):
        x, y = position
        rect = pygame.Rect(x * TILESIZE + x_shift, y * TILESIZE, TILESIZE, TILESIZE)
        pygame.draw.rect(surface, COLORS[shape_variant], rect, 0)
        surface.blit(self.block_image, (x * TILESIZE + x_shift, y * TILESIZE))
        if (y+1) < GRIDHEIGHT and self.field[y+1][x] is None:
            surface.blit(self.block_shadow_image, (x * TILESIZE + x_shift, (y + 1) * TILESIZE))

    def render_field(self, field):
        """Rendering game grid with no fill rectangles"""
        for x, y in ((x, y) for y in range(GRIDHEIGHT) for x in range(GRIDWIDTH)):
            if field[y][x] is not None:
                self.render_block(self.field_surfaces, (x, y), field[y][x], x_shift=True)

    def render_shadow(self, shadow_position: tuple[int, int], shape_variant: int, orientation: int):
        """Rendering figure with filled rectangles of figure's color"""
        for dx, dy in SHAPES[shape_variant][orientation]:
            x = shadow_position[0] + dx
            y = shadow_position[1] + dy
            shadow_rect = pygame.Rect(x * TILESIZE + 1, y * TILESIZE + 1, TILESIZE - 2, TILESIZE - 2)
            pygame.draw.rect(self.figure_surfaces, COLORS[shape_variant], shadow_rect, 2)

    def render_figure(self, figure_position: tuple[int, int], shape_variant: int, orientation: int):
        """Rendering figure with filled rectangles of figure's color"""
        for dx, dy in SHAPES[shape_variant][orientation]:
            x = figure_position[0] + dx
            y = int(figure_position[1]) + dy
            self.render_block(self.figure_surfaces, (x, y), shape_variant, x_shift=True)

    def render_animations(self, active_animations):
        for animation in active_animations:
            self.animations_surfaces.blit(Animation.frames_container[animation[0].animation_type][animation[0].frame],
                                          (animation[1][0] * TILESIZE, animation[1][1] * TILESIZE))

    def render_game_screen(self):

        self.game_surface.blit(self.field_surfaces, (0, 0))
        self.game_surface.blit(self.figure_surfaces, (0, 0))

        self.game_surface.blit(self.animations_surfaces, (0, 0))
        # self.game_surface.blit(self.grid_surface, (0, 0))

        return self.game_surface
