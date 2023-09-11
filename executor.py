import pygame
from constants import *

from containers import Container, MenuContainer, SinglePlayerContainer

CONTAINERS = {'menu': MenuContainer, 'sp': SinglePlayerContainer}


class SurfaceInterface:
    def __init__(self):
        self.container: Container = MenuContainer()

    def run(self):
        while True:
            dt = clock.tick(FPS)

            self.container.update(dt)
            if self.container.new_container is not None:
                self.container = CONTAINERS[self.container.new_container]()

            self.container.render(window_surface)
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