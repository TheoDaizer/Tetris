import pygame
from constants import TILESIZE
from game import Game

from constants import WINDOWWIDTH, WINDOWHEIGHT


class Renderer:
    def __init__(self, game: Game, game_screen):
        self.game = game
        self.game_screen = game_screen
        self.field_surface = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.figure_surface = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.grid_image = pygame.image.load("resources\\tetris_bg.png")

    def render(self):
        """Main rendering function, that call other renderers"""
        if self.game.field_updated():
            self.render_field()
        self.render_figure()
        self.render_game_screen()

    def render_field(self):
        """Rendering game grid with no fill rectangles"""
        self.field_surface.fill("black")  # "clearing screen" by filling it with one color

        field = self.game.field
        for y in range(field.height):
            for x in range(field.width):
                if field.nodes[y][x].is_active:
                    r = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                    pygame.draw.rect(self.field_surface, field.nodes[y][x].color, r, 0)

    def render_figure(self):
        """Rendering figure with filled rectangles of figure's color"""
        self.figure_surface.blit(self.field_surface, (0, 0))

        figure = self.game.figure
        for pt in figure.shape_position:
            r = pygame.Rect(
                int(pt.x) * TILESIZE,
                int(pt.y) * TILESIZE,
                TILESIZE,
                TILESIZE
                )
            pygame.draw.rect(self.figure_surface, figure.color, r, 0)

    def render_game_screen(self):
        self.game_screen.blit(self.figure_surface, (0, 0))
        self.game_screen.blit(self.grid_image, (0, 0))
