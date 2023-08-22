import pygame
import sys

from constants import *
import game
from render import render

if __name__ == '__main__':

    pygame.init()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    game = game.Game()

    while True:
        #input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
       
        #update()

        render(game, windowSurface)
        pygame.display.flip()
