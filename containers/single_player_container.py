import pygame
import pygame_gui
from pygame.surface import Surface
from pygame.event import Event

from game import Game, GameDataContainer, GameFieldRenderer
from constants import WINDOWWIDTH, WINDOWHEIGHT, BACKGROUND
from gui.gui_constants import game_field_pos_x, game_field_pos_y, game_field_frame
from containers import Container, GameSounds
from gui.single_player_gui import SinglePlayerMenu


class SinglePlayerContainer(Container, GameSounds):
    def __init__(self, window_surface):
        super().__init__(window_surface)
        GameSounds.__init__(self)
        self.music.play(-1)

        self.renderer = GameFieldRenderer()
        self.game = Game()
        self.game_data: GameDataContainer = self.game.dump()

        self.sp_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.sp_surface.blit(pygame.image.load(BACKGROUND), (0, 0))

        self.manager = pygame_gui.UIManager((WINDOWWIDTH, WINDOWHEIGHT))
        self.sp_surface.blit(pygame.image.load(game_field_frame), (game_field_pos_x - 39, game_field_pos_y - 46))

        self.sp_ui_menu = SinglePlayerMenu(self.manager, self.game_data, self.sp_surface, self.music)

        self.sp_surface_background = Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.sp_surface_background.blit(self.sp_surface, (0, 0))

    @property
    def status(self):
        if self.game.is_game_over or self.sp_ui_menu.is_game_over:
            self.music.stop()
            self.game_over.play()
            return 'menu'
        return None

    def event_handler(self, event: Event):
        if not self.sp_ui_menu.pause_state:
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
                if event.key == pygame.K_ESCAPE:
                    self.sp_ui_menu.key_esc_down()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.game.key_down_up()
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.game.key_left_up()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.game.key_right_up()
        else:
            self.manager.process_events(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.sp_ui_menu.key_esc_down()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                self.sp_ui_menu.button_pressed(event)

            if event.type == pygame_gui.UI_BUTTON_ON_HOVERED or event.type == pygame_gui.UI_BUTTON_ON_UNHOVERED:
                self.sp_ui_menu.render_menu()

    def update(self, time_delta: float):
        if not self.sp_ui_menu.pause_state:
            self.game_data = self.game.update(time_delta)
            self.sp_ui_menu.update(self.game_data)

            if self.game_data.is_field_updated:
                self.sfx_play()
        else:
            self.manager.update(time_delta)

    def render(self):
        if not self.sp_ui_menu.pause_state:
            game_field_surface = self.renderer.render(self.game_data)
            self.sp_surface.blit(game_field_surface, (game_field_pos_x, game_field_pos_y))
            self.sp_ui_menu.render()

        self.window_surface.blit(self.sp_surface, (0, 0))

    def sfx_play(self):
        if self.game_data.burned_rows == 4:
            self.burn_tetris.play()
        elif self.game_data.burned_rows:
            self.burn_sound.play()
        else:
            self.freeze_sound.play()
