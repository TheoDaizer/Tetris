import pygame
from constants import TILESIZE
from game import Game

from constants import WINDOWWIDTH, WINDOWHEIGHT


class Renderer:
    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.field_surfaces = [pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT)),
                               pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
                               ]
        self.figure_surfaces = [pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT)),
                                pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
                                ]
        self.grid_image = pygame.image.load("resources\\tetris_bg.png")

    def render(self, game_1: Game, game_2: Game):
        """Main rendering function, that call other renderers"""
        if game_1.field_updated:
            self.render_field(game_1.field, 0)
        if game_2.field_updated:
            self.render_field(game_2.field, 1)

        self.render_figure(game_1.figure, 0)
        self.render_figure(game_2.figure, 1)

        self.render_game_screen()

    def render_field(self, field, game_n: int):
        """Rendering game grid with no fill rectangles"""
        self.field_surfaces[game_n].fill("black")  # "clearing screen" by filling it with one color

        for x, y in ((x, y) for y in range(field.height) for x in range(field.width)):
            if field.nodes[y][x].is_active:
                r = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                pygame.draw.rect(self.field_surfaces[game_n], field.nodes[y][x].color, r, 0)

    def render_figure(self, figure, game_n):
        """Rendering figure with filled rectangles of figure's color"""
        self.figure_surfaces[game_n].blit(self.field_surfaces[game_n], (0, 0))

        for pt in figure.shape_position:
            r = pygame.Rect(
                int(pt.x) * TILESIZE,
                int(pt.y) * TILESIZE,
                TILESIZE,
                TILESIZE
                )
            pygame.draw.rect(self.figure_surfaces[game_n], figure.color, r, 0)

    def render_game_screen(self):
        self.game_screen.blit(self.figure_surfaces[0], (0, 0))
        self.game_screen.blit(self.figure_surfaces[1], (WINDOWWIDTH, 0))

        self.game_screen.blit(self.grid_image, (0, 0))
        self.game_screen.blit(self.grid_image, (WINDOWWIDTH, 0))
