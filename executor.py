import pygame
import sys

from constants import *
from renderer import Renderer
from network import Network, NetworkContainer

if __name__ == '__main__':
    network = Network()

    pygame.init()
    clock = pygame.time.Clock()

    game_screen = pygame.display.set_mode((WINDOWWIDTH * 2, WINDOWHEIGHT))
    game = network.get_game()

    game_renderer = Renderer(game_screen)

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

        player = NetworkContainer(game)
        player_2 = network.send(player)

        game_renderer.render(player, player_2)
        pygame.display.flip()  # updating screen
        # print(dt)
