import pygame
from pygame.surface import Surface
from pygame.event import Event

from game import Game, GameFieldRenderer
from constants import WINDOWWIDTH, WINDOWHEIGHT
from containers import Container


class SinglePlayerContainer(Container):
    def __init__(self, window_surface):
        super().__init__(window_surface)

        self.renderer = GameFieldRenderer()
        self.game = Game()

        self.sp_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.sp_surface.blit(pygame.image.load("resources/background2.jpg"), (0, 0))

        self.freeze_sound = pygame.mixer.Sound('resources/sfx-1.mp3')
        self.freeze_sound.set_volume(0.5)

        self.burn_sound = pygame.mixer.Sound('resources/sfx-2.mp3')
        self.burn_sound.set_volume(0.5)

        self.game_over = pygame.mixer.Sound('resources/game-over.mp3')
        self.game_over.set_volume(0.1)

        self.music = pygame.mixer.Sound('resources/8_bit_-_Korobejniki.mp3')
        self.music.set_volume(0.5)
        self.music.play(-1)

    @property
    def status(self):
        if self.game.game_over:
            self.music.stop()
            self.game_over.play()
            return 'menu'
        return None

    def event_handler(self, event: Event):
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self.game.keyboard_input(event)

    def update(self, time_delta: float):
        self.game.update(time_delta)
        if self.game.field_updated:
            self.sfx_play()

    def render(self):
        player = self.game.dump()
        game_field_surface = self.renderer.render(player)
        self.sp_surface.blit(game_field_surface, (WINDOWWIDTH // 4, 50))

        self.window_surface.blit(self.sp_surface, (0, 0))

    def sfx_play(self):
        if self.game.is_burned:
            self.burn_sound.play()
        else:
            self.freeze_sound.play()
