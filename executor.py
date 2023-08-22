import pygame
import sys

from constants import *
import game
from render import render

if __name__ == '__main__':

    pygame.init()
    window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    game = game.Game();

    while True:
        #input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #elif event.type == :
            #    pass
       
        #update()

        render(game, window_surface)
        pygame.display.flip()

        

