import pygame
from pygame.surface import Surface

from constants import TILESIZE
from network import NetworkContainer

from constants import FIELDWIDTH, FIELDHEIGHT


class GameFieldRenderer:
    def __init__(self):
        self.game_surface: Surface = Surface((FIELDWIDTH, FIELDHEIGHT))
        self.field_surfaces: Surface = Surface((FIELDWIDTH, FIELDHEIGHT))
        self.figure_surfaces: Surface = Surface((FIELDWIDTH, FIELDHEIGHT))
        self.grid_image = pygame.image.load("resources/tetris_bg.png")

    def render(self, game_container: NetworkContainer):
        """Main rendering function, that call other renderers"""
        if game_container.field is not None:
            self.render_field(game_container.field)
        self.render_figure(game_container.figure, game_container.figure_color)

        return self.render_game_screen()

    def render_field(self, field):
        """Rendering game grid with no fill rectangles"""
        self.field_surfaces.fill("black")  # "clearing screen" by filling it with one color

        for x, y in ((x, y) for y in range(len(field)) for x in range(len(field[0]))):
            if field[y][x] is not None:
                r = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                pygame.draw.rect(self.field_surfaces, field[y][x], r, 0)

    def render_figure(self, figure, figure_color):
        """Rendering figure with filled rectangles of figure's color"""
        self.figure_surfaces.blit(self.field_surfaces, (0, 0))

        for pt in figure:
            r = pygame.Rect(
                int(pt.x) * TILESIZE,
                int(pt.y) * TILESIZE,
                TILESIZE,
                TILESIZE
                )
            pygame.draw.rect(self.figure_surfaces, figure_color, r, 0)

    def render_game_screen(self):
        self.game_surface.blit(self.figure_surfaces, (0, 0))
        self.game_surface.blit(self.grid_image, (0, 0))
        return self.game_surface
