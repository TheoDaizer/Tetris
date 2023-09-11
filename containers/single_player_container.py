import sys
import pygame
from pygame.surface import Surface

from game import Game, GameFieldRenderer
from constants import WINDOWWIDTH, WINDOWHEIGHT
from containers import Container


class SinglePlayerContainer(Container):
    def __init__(self):
        self.renderer = GameFieldRenderer()
        self.game = Game()

        self.sp_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.sp_surface.blit(pygame.image.load("resources/background2.jpg"), (0, 0))

    @property
    def new_container(self):
        return 'menu' if self.game.game_over else None

    def update(self, time_delta: float):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self.game.keyboard_input(event)

        self.game.update(time_delta)

    def render(self) -> Surface:
        player = self.game.dump()
        game_field_surface = self.renderer.render(player)
        self.sp_surface.blit(game_field_surface, (WINDOWWIDTH // 4, 50))
        return self.sp_surface
