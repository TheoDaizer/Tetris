import pygame
from pygame.surface import Surface
from .figure import Figure
from .point import Point

from constants import TILESIZE, FIELDWIDTH, FIELDHEIGHT, GRIDHEIGHT, GRIDWIDTH
from game import GameDataContainer


class GameFieldRenderer:

    block_image = pygame.image.load("resources/tetris_block.png")

    def __init__(self):
        self.game_surface: Surface = Surface((FIELDWIDTH, FIELDHEIGHT))
        self.field_surfaces: Surface = Surface((FIELDWIDTH, FIELDHEIGHT))
        self.figure_surfaces: Surface = Surface((FIELDWIDTH, FIELDHEIGHT))

        self.grid_surface = pygame.Surface((FIELDWIDTH, FIELDHEIGHT), pygame.SRCALPHA)
        self.draw_grid()

    def draw_grid(self):
        self.grid_surface.fill((0, 0, 0, 0))
        for x, y in ((x, y) for y in range(GRIDHEIGHT) for x in range(GRIDWIDTH)):
            r = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(self.grid_surface, (100, 100, 100), r, 1)

    def render(self, game_data: GameDataContainer):
        """Main rendering function, that call other renderers"""
        if game_data.field is not None:
            self.render_field(game_data.field)
        self.figure_surfaces.blit(self.field_surfaces, (0, 0))
        self.render_shadow(self.figure_surfaces, game_data.shadow_position,
                           game_data.shape_variant, game_data.orientation)
        self.render_figure(self.figure_surfaces, game_data.figure_position,
                           game_data.shape_variant, game_data.orientation)

        return self.render_game_screen()

    def render_field(self, field):
        """Rendering game grid with no fill rectangles"""
        self.field_surfaces.fill("black")  # "clearing screen" by filling it with one color

        for x, y in ((x, y) for y in range(len(field)) for x in range(len(field[0]))):
            if field[y][x] is not None:
                r = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                pygame.draw.rect(self.field_surfaces, field[y][x], r, 0)
                self.field_surfaces.blit(self.block_image, (x * TILESIZE, y * TILESIZE))

    @staticmethod
    def render_shadow(surface, shadow_position: Point, shape_variant: int, orientation: int):
        """Rendering figure with filled rectangles of figure's color"""

        for pt in Figure.shape_position(shadow_position, shape_variant, orientation):
            shadow_rect = pygame.Rect(
                int(pt.x) * TILESIZE + 1, int(pt.y) * TILESIZE + 1,
                TILESIZE - 2, TILESIZE - 2)
            pygame.draw.rect(surface, (200, 200, 200), shadow_rect, 2)

    @staticmethod
    def render_figure(surface, figure_position: Point, shape_variant: int, orientation: int):
        """Rendering figure with filled rectangles of figure's color"""

        for pt in Figure.shape_position(figure_position, shape_variant, orientation):
            figure_rect = pygame.Rect(
                int(pt.x) * TILESIZE, int(pt.y) * TILESIZE,
                TILESIZE, TILESIZE)
            pygame.draw.rect(surface, Figure.all_colors[shape_variant], figure_rect, 0)
            surface.blit(GameFieldRenderer.block_image, (int(pt.x) * TILESIZE, int(pt.y) * TILESIZE))

    @staticmethod
    def render_figure_box(surface, figure_position: Point, shape_variant: int, orientation: int):
        """Rendering figure with filled rectangles of figure's color"""

        for pt in Figure.shape_position(figure_position, shape_variant, orientation):
            figure_rect = pygame.Rect(
                int(pt.x) * TILESIZE, int(pt.y) * TILESIZE,
                TILESIZE, TILESIZE)
            pygame.draw.rect(surface, Figure.all_colors[shape_variant], figure_rect, 0)
            surface.blit(GameFieldRenderer.block_image, (int(pt.x) * TILESIZE, int(pt.y) * TILESIZE))

    def render_game_screen(self):
        self.game_surface.blit(self.figure_surfaces, (0, 0))
        self.game_surface.blit(self.grid_surface, (0, 0))
        return self.game_surface
