import pygame
from constants import TILESIZE
from game import Game, Field
from figure import Figure


def renderField(field: Field, window_surface):
    """Rendering game grid with no fill rectangles"""
    for i in range(len(field.cells)):
        for j in range(len(field.cells[i])):
            r = pygame.Rect(i * TILESIZE, j * TILESIZE, TILESIZE, TILESIZE)
            
            if(field.cells[i][j].is_active):
                pygame.draw.rect(window_surface, field.cells[i][j].color, r, 0)

            color = (100, 100, 100)
            pygame.draw.rect(window_surface, color, r, 2)


def renderFigure(figure: Figure, window_surface):
    """Rendering figure with filled rectangles of figure's color"""
    #oriented_shape = figure.shape[figure.orientation]
    for pt in figure.shape_position:
        r = pygame.Rect(
            int(pt.x) * TILESIZE, 
            int(pt.y) * TILESIZE, 
            TILESIZE, 
            TILESIZE
            )
        pygame.draw.rect(window_surface, figure.color, r, 0)


def render(game: Game, window_surface):
    """Main rendering function, that call other renderers"""
    renderFigure(game.figure, window_surface)
    renderField(game.field, window_surface)
