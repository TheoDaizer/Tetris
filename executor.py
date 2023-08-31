import pygame
import sys

from constants import *
from game import Game
from renderer import Renderer

if __name__ == '__main__':

    pygame.init()
    clock = pygame.time.Clock()

    game_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    tetris_game = Game()

    game_renderer = Renderer(tetris_game, game_surface)
    #game_renderer.renderBackGround();

    clock.tick()  # time restart
    while True:
        dt = clock.tick(FPS)  # time from previous frame in milliseconds. argument provides fps limitation

        for user_input in pygame.event.get():
            if user_input.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if user_input.type == pygame.KEYDOWN or user_input.type == pygame.KEYUP:
                tetris_game.keyboard_input(user_input)
       
        tetris_game.update(dt)

        game_renderer.render() 
        pygame.display.flip()  # updating screen
        #print(dt)