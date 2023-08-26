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

    clock.tick()  # time restart
    while True:
        dt = clock.tick(FPS)  # time from previous frame in milliseconds. argument provides fps limitation

        for user_input in pygame.event.get():
            if user_input.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if user_input.type == pygame.KEYDOWN or user_input.type == pygame.KEYUP:
                game.keyboard_input(user_input)
       
        game.update(dt)

        window_surface.fill("black")  # "clearing screen" by filling it with one color
        render(game, window_surface) 
        pygame.display.flip()  # updating screen
