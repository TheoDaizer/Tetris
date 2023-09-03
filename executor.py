import pygame
import sys

from constants import *
from renderer import Renderer
from network import Network

if __name__ == '__main__':
    network = Network()

    pygame.init()
    clock = pygame.time.Clock()

    game_screen = pygame.display.set_mode((WINDOWWIDTH * 2, WINDOWHEIGHT))
    game_1 = network.get_game()

    game_renderer = Renderer(game_screen)

    clock.tick()  # time restart
    while True:
        dt = clock.tick(FPS)  # time from previous frame in milliseconds. argument provides fps limitation
        game_2 = network.send(game_1)
        for user_input in pygame.event.get():
            if user_input.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if user_input.type == pygame.KEYDOWN or user_input.type == pygame.KEYUP:
                game_1.keyboard_input(user_input)

        game_1.update(dt)

        game_renderer.render(game_1, game_2)
        pygame.display.flip()  # updating screen
        # print(dt)
