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
        self.sp_surface.blit(pygame.image.load(BACKGROUNDPATH), (0, 0))

        self.manager = pygame_gui.UIManager((WINDOWWIDTH, WINDOWHEIGHT))
        self.sp_ui_panel = pygame_gui.elements.ui_panel.UIPanel(
            relative_rect=pygame.Rect((0, 0), (150, 800)),
            manager=self.manager,
        )

        self.sp_pause_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((0, 0), (100, 100)),
            text='Pause',
            container=self.sp_ui_panel,
            manager=self.manager,
            visible=True
        )
        self.pause_state = False

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
        self.manager.process_events(event)
        if self.pause_state == False:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self.game.keyboard_input(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.sp_pause_button:
                if self.pause_state == False:
                    self.pause_state = True
                else:
                    self.pause_state = False

    def update(self, time_delta: float):
        if self.pause_state == False:
            self.game.update(time_delta)
            self.manager.update(time_delta)
            if self.game.field_updated:
                self.sfx_play()
        else:
            self.manager.update(time_delta)

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
