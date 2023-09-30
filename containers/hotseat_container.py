import pygame
from pygame.surface import Surface
from pygame.event import Event

from game import Game, GameDataContainer, GameFieldRenderer
from constants import WINDOWWIDTH, WINDOWHEIGHT, background
from containers import Container, GameSounds

from datetime import datetime


class HotSeatContainer(Container, GameSounds):
    def __init__(self, window_surface):
        super().__init__(window_surface)
        GameSounds.__init__(self)
        self.music.play(-1)

        self.renderer_1 = GameFieldRenderer()
        self.renderer_2 = GameFieldRenderer()

        seed = datetime.now().timestamp()
        self.game_1 = Game(seed)
        self.game_2 = Game(seed)

        self.game_data_1: GameDataContainer = self.game_1.dump()
        self.game_data_2: GameDataContainer = self.game_2.dump()

        self.hs_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.hs_surface.blit(pygame.image.load(background), (0, 0))

    @property
    def status(self):
        if self.game_data_1.is_game_over and self.game_data_2.is_game_over:
            self.music.stop()
            self.game_over.play()
            return 'menu'
        return None

    def event_handler(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.game_1.key_left_down()
            if event.key == pygame.K_LEFT:
                self.game_2.key_left_down()

            if event.key == pygame.K_d:
                self.game_1.key_right_down()
            if event.key == pygame.K_RIGHT:
                self.game_2.key_right_down()

            if event.key == pygame.K_w:
                self.game_1.key_up_down()
            if event.key == pygame.K_UP:
                self.game_2.key_up_down()

            if event.key == pygame.K_s:
                self.game_1.key_down_down()
            if event.key == pygame.K_DOWN:
                self.game_2.key_down_down()

            if event.key == pygame.K_SPACE:
                self.game_1.key_space_down()
            if event.key == pygame.K_KP_ENTER:
                self.game_2.key_space_down()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                self.game_1.key_down_up()
            if event.key == pygame.K_DOWN:
                self.game_2.key_down_up()

            if event.key == pygame.K_a:
                self.game_1.key_left_up()
            if event.key == pygame.K_LEFT:
                self.game_2.key_left_up()

            if event.key == pygame.K_d:
                self.game_1.key_right_up()
            if event.key == pygame.K_RIGHT:
                self.game_2.key_right_up()

    def update(self, time_delta: float):
        if not self.game_data_1.is_game_over:
            self.game_data_1 = self.game_1.update(time_delta)

        if not self.game_data_2.is_game_over:
            self.game_data_2 = self.game_2.update(time_delta)

        if self.game_data_1.is_field_updated or self.game_data_2.is_field_updated:
            self.sfx_play()

    def render(self):
        if not self.game_data_1.is_game_over:
            game_field_surface_1 = self.renderer_1.render(self.game_data_1)
            self.hs_surface.blit(game_field_surface_1, (0, 50))

        if not self.game_data_2.is_game_over:
            game_field_surface_2 = self.renderer_2.render(self.game_data_2)
            self.hs_surface.blit(game_field_surface_2, (WINDOWWIDTH // 2, 50))

        self.window_surface.blit(self.hs_surface, (0, 0))

    def sfx_play(self):
        if self.game_data_2.burned_rows == 4 or self.game_data_2.burned_rows == 4:
            self.burn_sound.play()
        elif self.game_data_1.burned_rows or self.game_data_2.burned_rows:
            self.burn_tetris.play()
        else:
            self.freeze_sound.play()
