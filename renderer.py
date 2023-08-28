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
        self.renderFigure(self.game.figure)
        self.renderField(self.game.field)
        self.renderBackGround()

    def renderField(self, field: Field):
        """Rendering game grid with no fill rectangles"""
        for i in range(len(field.cells)):
            for j in range(len(field.cells[i])):
                r = pygame.Rect(i * TILESIZE, j * TILESIZE, TILESIZE, TILESIZE)
                
                if(field.cells[i][j].is_active):
                    pygame.draw.rect(self.game_surface, field.cells[i][j].color, r, 0)
    

    
    def renderFigure(self, figure: Figure):
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
    
    def renderBackGround(self):
        self.game_surface.blit(self.bg_image, (0, 0))