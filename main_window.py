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

    def run(self, render_fps: bool = False):
        if render_fps:
            pygame.font.init()
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
            if render_fps:
                self.render_fps(dt)
            pygame.display.update()

    def render_fps(self, dt: int):

        my_font = pygame.font.SysFont('Arial', 30)

        text_surface = my_font.render(f'{1000 // dt}', False, (0, 0, 0))
        self.window_surface.blit(text_surface, (10, 10))
