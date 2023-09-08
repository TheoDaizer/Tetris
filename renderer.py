﻿import pygame
from constants import TILESIZE
from network import NetworkContainer

from constants import WINDOWWIDTH, WINDOWHEIGHT, GRIDHEIGHT, GRIDWIDTH


class Renderer:
    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.field_surfaces = [pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT)),
                               pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
                               ]
        self.figure_surfaces = [pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT)),
                                pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
                                ]
        self.background_surface = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT), pygame.SRCALPHA)

        self.background_surface.fill((0, 0, 0, 0))
        for x, y in ((x, y) for y in range(GRIDHEIGHT) for x in range(GRIDWIDTH)):
                r = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                pygame.draw.rect(self.background_surface, (100, 100, 100), r, 1)

    def render(self, game_1: NetworkContainer, game_2: NetworkContainer):
        """Main rendering function, that call other renderers"""
        if game_1.field is not None:
            self.render_field(game_1.field, 0)
        self.render_figure(game_1.figure, game_1.figure_color,  0)

        if game_2:
            if game_2.field is not None:
                self.render_field(game_2.field, 1)
            self.render_figure(game_2.figure, game_2.figure_color, 1)

        self.render_game_screen()

    def render_field(self, field, game_n: int):
        """Rendering game grid with no fill rectangles"""
        self.field_surfaces[game_n].fill("black")  # "clearing screen" by filling it with one color

        for x, y in ((x, y) for y in range(len(field)) for x in range(len(field[0]))):
            if field[y][x] is not None:
                r = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                pygame.draw.rect(self.field_surfaces[game_n], field[y][x], r, 0)

    def render_figure(self, figure, figure_color, game_n):
        """Rendering figure with filled rectangles of figure's color"""
        self.figure_surfaces[game_n].blit(self.field_surfaces[game_n], (0, 0))

        for pt in figure:
            r = pygame.Rect(
                int(pt.x) * TILESIZE,
                int(pt.y) * TILESIZE,
                TILESIZE,
                TILESIZE
                )
            pygame.draw.rect(self.figure_surfaces[game_n], figure_color, r, 0)

    def render_game_screen(self):

        self.game_screen.blit(self.figure_surfaces[0], (0, 0))
        self.game_screen.blit(self.figure_surfaces[1], (WINDOWWIDTH, 0))

        self.game_screen.blit(self.background_surface, (0, 0))
        self.game_screen.blit(self.background_surface, (WINDOWWIDTH, 0))
