import sys

import pygame

from pygame_gui.ui_manager import UIManager
from pygame.event import Event

from gui import Buttons


class GameMenu:
    def __init__(self, manager: UIManager, buttons: Buttons):
        self.manager = manager
        self.buttons = buttons

        self._button_container = 'main'
        self._is_changed = False
        self._window_container = None

        self.buttons.main_menu()

    @property
    def button_container(self):
        return self._button_container

    @button_container.setter
    def button_container(self, value):
        self.is_changed = True
        self._button_container = value

    @property
    def window_container(self):
        return self._window_container

    @property
    def is_changed(self):
        return self._is_changed

    @is_changed.setter
    def is_changed(self, value: bool):
        self._is_changed = value

    def process_events(self, event: Event):
        #  Main Menu
        if self.button_container == 'main':
            if event.ui_element == self.buttons.single_player_button:
                self.button_container = 'single'
                self.buttons.single_player()
            if event.ui_element == self.buttons.multiplayer_button:
                self.button_container = 'multi'
                self.buttons.multiplayer()
            if event.ui_element == self.buttons.settings_button:
                self.button_container = 'settings'
                self.buttons.settings()
            if event.ui_element == self.buttons.exit_button:
                pygame.quit()
                sys.exit()

        #  Single player Menu
        elif self.button_container == 'single':
            if event.ui_element == self.buttons.new_game_button:
                self._window_container = 'sp'
            if event.ui_element == self.buttons.high_scores_button:
                self.button_container = 'highscores'
                self.buttons.highscores()
            if event.ui_element == self.buttons.sp_btm_button:
                self.button_container = 'main'
                self.buttons.main_menu()

        #  Multiplayer Menu
        elif self.button_container == 'multi':
            if event.ui_element == self.buttons.start_server_button:
                pass
            if event.ui_element == self.buttons.start_multiplayer_button:
                pass
            if event.ui_element == self.buttons.mp_btm_button:
                self.button_container = 'main'
                self.buttons.main_menu()

        #  Highscores Menu
        elif self.button_container == 'highscores':
            if event.ui_element == self.buttons.hs_btm_button:
                self.button_container = 'main'
                self.buttons.main_menu()

        #  Settings Menu
        elif self.button_container == 'settings':
            if event.ui_element == self.buttons.set_btm_button:
                self.button_container = 'main'
                self.buttons.main_menu()
