import pygame
import pygame_gui
from pygame.surface import Surface
from pygame.event import Event

from game import Game, GameFieldRenderer
from constants import WINDOWWIDTH, WINDOWHEIGHT, BACKGROUNDPATH
from containers import Container


class SinglePlayerContainer(Container):
    def __init__(self, window_surface):
        super().__init__(window_surface)

        self.renderer = GameFieldRenderer()
        self.game = Game()

        self.sp_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.sp_surface.blit(pygame.image.load(BACKGROUNDPATH), (0, 0))
        self.gamefield_pos_x =  150 + (WINDOWWIDTH - 150) // 8
        self.gamefield_pos_y = 50

        self.manager = pygame_gui.UIManager((WINDOWWIDTH, WINDOWHEIGHT))
        self.sp_ui_panel = pygame_gui.elements.ui_panel.UIPanel(
            relative_rect=pygame.Rect((0, 0), (150, 800)),
            manager=self.manager,
        )

        self.sp_pause_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((25, 25), (100, 100)),
            text='Pause',
            container=self.sp_ui_panel,
            manager=self.manager,
            visible=True
        )

        self.sp_btm_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((25, 125), (100, 100)),
            text='BTM',
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

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.sp_pause_button:
                if self.pause_state == False:
                    self.pause_state = True
                    self.music.stop()
                else:
                    self.pause_state = False
                    self.music.play(-1)

            if event.ui_element == self.sp_btm_button:
                self.game.game_over = True
                self.music.stop()
                self.game_over.play()
                return 'menu'

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
        self.sp_surface.blit(game_field_surface, (self.gamefield_pos_x, self.gamefield_pos_y))
        self.manager.draw_ui(self.sp_surface)

        self.window_surface.blit(self.sp_surface, (0, 0))

    def sfx_play(self):
        if self.game.is_burned:
            self.burn_sound.play()
        else:
            self.freeze_sound.play()
