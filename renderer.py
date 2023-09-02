import pygame
from constants import TILESIZE
from game import Game, Field
from figure import Figure


class Renderer:
    def __init__(self, game: Game, game_surface):
        self.game = game
        self.game_surface = game_surface
        self.bg_image = pygame.image.load("resources\\tetris_bg.png")

    def render(self):
        """Main rendering function, that call other renderers"""
        self.render_figure(self.game.figure)
        self.render_field(self.game.field)
        self.render_background()

    def render_field(self, field: Field):
        """Rendering game grid with no fill rectangles"""
        for y in range(field.height):
            for x in range(field.width):
                r = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                
                if field.nodes[y][x].is_active:
                    pygame.draw.rect(self.game_surface, field.nodes[y][x].color, r, 0)
    

    
    def render_figure(self, figure: Figure):
        """Rendering figure with filled rectangles of figure's color"""
        self.game_surface.fill("black")  # "clearing screen" by filling it with one color
        for pt in figure.shape_position:
            r = pygame.Rect(
                int(pt.x) * TILESIZE, 
                int(pt.y) * TILESIZE, 
                TILESIZE, 
                TILESIZE
                )
            pygame.draw.rect(self.game_surface, figure.color, r, 0)
    
    def render_background(self):
        self.game_surface.blit(self.bg_image, (0, 0))