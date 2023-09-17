import pygame
from pygame.surface import Surface
from pygame.event import Event

from game import Game, GameFieldRenderer
from constants import WINDOWWIDTH, WINDOWHEIGHT
from containers import Container, GameSounds

from network import Network

from queue import Queue


class NetworkContainer(Container, GameSounds):
    def __init__(self, window_surface):
        super().__init__(window_surface)
        GameSounds.__init__(self)
        # self.music.play(-1)

        self.network = Network()
        seed = self.network.get_seed()

        self.renderer_1 = GameFieldRenderer()
        self.renderer_2 = GameFieldRenderer()

        self.game_1: Game = Game(seed)
        self.game_2: Game = Game(seed)

        self.input_mask = 0
        self.game_1_buffer = {}
        self.game_2_buffer = None

        self.mp_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.mp_surface.blit(pygame.image.load("resources/background2.jpg"), (0, 0))

        self.window_surface.blit(self.mp_surface, (0, 0))

    @property
    def status(self):
        if self.game_1.is_game_over and self.game_2.is_game_over:
            self.music.stop()
            self.game_over.play()
            return 'menu'
        return None

    def event_handler(self, event: Event):
        self.input_mask = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.input_mask ^= 1
                self.game_1.key_left_down()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.input_mask ^= 2
                self.game_1.key_right_down()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.input_mask ^= 4
                self.game_1.key_up_down()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.input_mask ^= 8
                self.game_1.key_down_down()
            if event.key == pygame.K_SPACE:
                self.input_mask ^= 16
                self.game_1.key_space_down()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.input_mask ^= 16
                self.game_1.key_down_up()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.input_mask ^= 32
                self.game_1.key_left_up()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.input_mask ^= 64
                self.game_1.key_right_up()

    def update(self, time_delta: float):
        if self.game_2_buffer is None:
            self.game_2_buffer = self.network.send(self.game_1_buffer)
            return

        if not self.game_1.is_game_over:
            self.game_1.update(time_delta)

        if not self.game_2.is_game_over:
            self.game_2.update()

        if self.game_1.is_field_updated or self.game_2.is_field_updated:
            self.sfx_play()

        self.game_2 = self.network.send(self.game_1_buffer)

        if self.game_1.is_field_updated:
            self.sfx_play()

    def render(self):
        if self.game_2 is None:
            self.game_2 = self.network.send(self.game_1_buffer)
            return

        if not self.game.is_game_over:
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
