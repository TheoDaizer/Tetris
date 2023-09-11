import pygame
from pygame.surface import Surface

from constants import TILESIZE, FIELDWIDTH, FIELDHEIGHT, GRIDHEIGHT, GRIDWIDTH
from game import GameDataContainer


class GameFieldRenderer:
    def __init__(self):
        self.game_surface: Surface = Surface((FIELDWIDTH, FIELDHEIGHT))
        self.field_surfaces: Surface = Surface((FIELDWIDTH, FIELDHEIGHT))
        self.figure_surfaces: Surface = Surface((FIELDWIDTH, FIELDHEIGHT))

        self.grid_surface = pygame.Surface((FIELDWIDTH, FIELDHEIGHT), pygame.SRCALPHA)
        self.draw_grid()

        self.block_image = pygame.image.load("resources/tetris_block.png")

    def draw_grid(self):
        self.grid_surface.fill((0, 0, 0, 0))
        for x, y in ((x, y) for y in range(GRIDHEIGHT) for x in range(GRIDWIDTH)):
            r = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(self.grid_surface, (100, 100, 100), r, 1)

    def render(self, game_data: GameDataContainer):
        """Main rendering function, that call other renderers"""
        if game_data.field is not None:
            self.render_field(game_data.field)
        self.render_figure(game_data.figure, game_data.figure_shadow, game_data.figure_color)

        return self.render_game_screen()

    def render_field(self, field):
        """Rendering game grid with no fill rectangles"""
        self.field_surfaces.fill("black")  # "clearing screen" by filling it with one color

        for x, y in ((x, y) for y in range(len(field)) for x in range(len(field[0]))):
            if field[y][x] is not None:
                r = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                pygame.draw.rect(self.field_surfaces, field[y][x], r, 0)
                self.field_surfaces.blit(self.block_image, (x * TILESIZE, y * TILESIZE))

    def render_figure(self, figure, shadow, figure_color):
        """Rendering figure with filled rectangles of figure's color"""
        self.figure_surfaces.blit(self.field_surfaces, (0, 0))

        for pt in shadow:
            r = pygame.Rect(
                int(pt.x) * TILESIZE + 1, int(pt.y) * TILESIZE + 1,
                TILESIZE - 2, TILESIZE - 2)
            pygame.draw.rect(self.figure_surfaces, (200, 200, 200), r, 2)

        for pt in figure:
            r = pygame.Rect(
                int(pt.x) * TILESIZE, int(pt.y) * TILESIZE,
                TILESIZE, TILESIZE)
            pygame.draw.rect(self.figure_surfaces, figure_color, r, 0)
            self.figure_surfaces.blit(self.block_image, (int(pt.x) * TILESIZE, int(pt.y) * TILESIZE))

    def render_game_screen(self):
        self.game_surface.blit(self.figure_surfaces, (0, 0))
        self.game_surface.blit(self.grid_surface, (0, 0))
        return self.game_surface
