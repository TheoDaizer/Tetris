import sys
import pygame
from constants import *

from containers import Container, MenuContainer, SinglePlayerContainer, HotSeatContainer, NetworkContainer

CONTAINERS = {'menu': MenuContainer, 'sp': SinglePlayerContainer, 'hs': HotSeatContainer, 'mp': NetworkContainer}


class MainWindow:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('PvP Tetris')

        self.clock = pygame.time.Clock()
        self.window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.RESIZABLE)

        self.container: Container = MenuContainer(self.window_surface)

    def run(self):

        while True:
            dt = self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.container.event_handler(event)

            self.container.update(dt)
            if self.container.status:
                self.container = CONTAINERS[self.container.status](self.window_surface)

            self.container.render()
            pygame.display.update()
