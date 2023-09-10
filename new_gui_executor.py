import sys

import pygame
from constants import *

from containers import MenuContainer, Container


class SurfaceInterface:
    def __init__(self):
        self.container: Container = MenuContainer()

    def run(self):
        while True:

            # events = pygame.event.get()
            # for event in events:
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         sys.exit()

            dt = clock.tick(FPS)
            self.container.update(dt)
            window_surface.blit(background, (0, 0))

            window_surface.blit(self.container.render(), (0, 0))
            pygame.display.update()


if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption('PvP Tetris')
    clock = pygame.time.Clock()

    window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.RESIZABLE)

    background = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
    background.fill(pygame.Color('#000000'))

    game_field_surface = pygame.Surface((WINDOWWIDTH * 2 // 3, WINDOWHEIGHT))
    game_interface_surface = pygame.Surface((WINDOWWIDTH // 3, WINDOWHEIGHT))

    interface = SurfaceInterface()

    interface.run()
