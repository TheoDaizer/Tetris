import pygame
import sys

from constants import *
import game
from render import render

if __name__ == '__main__':

    pygame.init()
    clock = pygame.time.Clock()

    window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    game = game.Game()

    clock.tick() #time restart
    while True:
        dt = clock.tick(FPS) # time from previous frame in milliseconds. argument provides fps limitation

        #input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #elif event.type == :
            #    pass
       
        game.update(dt)

        window_surface.fill("black") # "clearing screen" by fillin it with one color
        render(game, window_surface) 
        pygame.display.flip() # updating screen
