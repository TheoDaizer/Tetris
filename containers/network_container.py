from typing import Optional

import pygame
from pygame.surface import Surface
from pygame.event import Event

from game import Game, GameDataContainer, GameFieldRenderer
from constants import WINDOWWIDTH, WINDOWHEIGHT, FPS, BACKGROUNDPATH
from containers import Container, GameSounds

from _thread import start_new_thread
from network import Network
from time import sleep


class NetworkContainer(Container, GameSounds):
    def __init__(self, window_surface):
        super().__init__(window_surface)
        GameSounds.__init__(self)
        self.music.play(-1)

        self.network = Network()
        seed = self.network.get_seed()

        self.renderer_1 = GameFieldRenderer()
        self.renderer_2 = GameFieldRenderer()

        self.game: Game = Game(seed)
        self.game_field = None

        self.game_1: GameDataContainer = self.game.dump()
        self.game_2: Optional[GameDataContainer] = None
        start_new_thread(self.__update_game_2, tuple())

        self.input_mask = 0

        self.mp_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.mp_surface.blit(pygame.image.load(BACKGROUNDPATH), (0, 0))

        self.window_surface.blit(self.mp_surface, (0, 0))

    @property
    def status(self):
        if self.game.is_game_over and self.game_2.is_game_over:
            self.music.stop()
            self.game_over.play()
            return 'menu'
        return None

    def event_handler(self, event: Event):
        self.input_mask = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.input_mask ^= 1
                self.game.key_left_down()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.input_mask ^= 2
                self.game.key_right_down()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.input_mask ^= 4
                self.game.key_up_down()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.input_mask ^= 8
                self.game.key_down_down()
            if event.key == pygame.K_SPACE:
                self.input_mask ^= 16
                self.game.key_space_down()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.input_mask ^= 16
                self.game.key_down_up()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.input_mask ^= 32
                self.game.key_left_up()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.input_mask ^= 64
                self.game.key_right_up()

    def __update_game_2(self):
        sleep_time = 0.5 / FPS
        while True:
            self.game_1.field = self.game_field
            self.game_2 = self.network.send(self.game_1)
            sleep(sleep_time)

    def update(self, time_delta: float):
        if self.game_2 is None:
            return

        if not self.game.is_game_over:
            self.game.update(time_delta)
            if self.game.is_field_updated:
                self.game_field = self.game.field.nodes

    def render(self):
        if self.game_2 is None:
            return

        if not self.game.is_game_over:
            self.game_1 = self.game.dump()
            game_field_surface_1 = self.renderer_1.render(self.game_1)
            self.mp_surface.blit(game_field_surface_1, (0, 50))

        if not self.game_2.is_game_over:
            game_field_surface_2 = self.renderer_2.render(self.game_2)
            self.mp_surface.blit(game_field_surface_2, (WINDOWWIDTH // 2, 50))

        self.window_surface.blit(self.mp_surface, (0, 0))

    def sfx_play(self):
        if self.game.burned_rows == 4:
            self.burn_sound.play()
        elif self.game.burned_rows:
            self.burn_tetris.play()
        else:
            self.freeze_sound.play()
