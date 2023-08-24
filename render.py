import pygame
from constants import TILESIZE
from game import Game, Field
from point import Point
from figure import Figure

def renderField(field: Field, window_surface):
    """Rendering game grid with no fill rectangles"""
    for i in range(len(field.cells)):
        for j in range(len(field.cells[i])):
            r = pygame.Rect(i * TILESIZE, j * TILESIZE, TILESIZE, TILESIZE)

            color = (100, 100, 100);
            #color = (i * 10, i * 10, i * 10);
            #if color[0] > 255:
            #    color = (255, 255, 255)
            #if color[0] < 0:

            #    color = (0, 0, 0)

            pygame.draw.rect(window_surface, color, r, 2)

    #r = pygame.Rect(0, 0, 10, 10)
    #pygame.draw.rect(windowSurface, (255, 0, 0), r, 0)

def renderFigure(figure: Figure, window_surface):
    """Rendering figure with filled rectangles of figure's color"""
    oriented_shape = figure.shape[figure.orientation]
    for i in range(len(figure.shape)):
        r = pygame.Rect(
            (int(figure.position.x) + oriented_shape[i].x) * TILESIZE, 
            (int(figure.position.y) + oriented_shape[i].y) * TILESIZE, 
            TILESIZE, 
            TILESIZE
            )
        pygame.draw.rect(window_surface, figure.color, r, 0)

def render(game: Game, window_surface):
    """Main rendering function, that call other renderers"""
    renderFigure(game.figure, window_surface)
    renderField(game.field, window_surface)