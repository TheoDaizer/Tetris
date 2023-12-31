import pygame
from pygame.surface import Surface
from pygame.event import Event

from game import Game, GameDataContainer, GameFieldRenderer
from constants import WINDOWWIDTH, WINDOWHEIGHT, background
from containers import Container, GameSounds


class SinglePlayerContainer(Container, GameSounds):
    def __init__(self, window_surface):
        super().__init__(window_surface)
        GameSounds.__init__(self)
        self.music.play(-1)

        self.renderer = GameFieldRenderer()
        self.game = Game()

        self.game_data: GameDataContainer = self.game.dump()

        self.sp_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.sp_surface.blit(pygame.image.load(background), (0, 0))

    @property
    def status(self):
        if self.game.is_game_over:
            self.music.stop()
            self.game_over.play()
            return 'menu'
        return None

    def event_handler(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.game.key_left_down()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.game.key_right_down()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.game.key_up_down()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.game.key_down_down()
            if event.key == pygame.K_SPACE:
                self.game.key_space_down()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.game.key_down_up()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.game.key_left_up()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.game.key_right_up()

    def update(self, time_delta: float):
        self.game_data = self.game.update(time_delta)
        if self.game_data.is_field_updated:
            self.sfx_play()

    def render(self):
        game_field_surface = self.renderer.render(self.game_data)
        self.sp_surface.blit(game_field_surface, (WINDOWWIDTH // 4, 50))

        self.window_surface.blit(self.sp_surface, (0, 0))

    def sfx_play(self):
        if self.game_data.burned_rows == 4:
            self.burn_tetris.play()
        elif self.game_data.burned_rows:
            self.burn_sound.play()
        else:
            self.freeze_sound.play()
