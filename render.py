import pygame
from constants import TILESIZE
from game import Game, Grid

def renderGrid(grid: Grid, windowSurface):
    for i in range(len(grid.grid)):
        for j in range(len(grid.grid[i])):
            r = pygame.Rect(i * TILESIZE, j * TILESIZE, TILESIZE, TILESIZE)

            color = (100, 100, 100);
            #color = (i * 10, i * 10, i * 10);
            #if color[0] > 255:
            #    color = (255, 255, 255)
            #if color[0] < 0:
            #    color = (0, 0, 0)

            pygame.draw.rect(windowSurface, color, r, 2)

    #r = pygame.Rect(0, 0, 10, 10)
    #pygame.draw.rect(windowSurface, (255, 0, 0), r, 0)


def render(game: Game, windowSurface):
    renderGrid(game.grid, windowSurface)