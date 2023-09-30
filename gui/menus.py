import sys
from typing import Optional

import pygame

from pygame_gui.ui_manager import UIManager
from pygame.event import Event

from gui import Buttons
from gui.abc_menu import Menu


class MainMenu(Menu):
    def __init__(self, manager: UIManager, buttons: Optional[Buttons] = None):
        super().__init__(manager, buttons)
        self.buttons.main_menu()

    def process_events(self, event: Event):
        if event.ui_element == self.buttons.single_player_button:
            return SinglePlayerMenu(self.manager, self.buttons)

        if event.ui_element == self.buttons.multiplayer_button:
            return MultiplayerMenu(self.manager, self.buttons)

        if event.ui_element == self.buttons.settings_button:
            return SettingsMenu(self.manager, self.buttons)

        if event.ui_element == self.buttons.exit_button:
            pygame.quit()
            sys.exit()


class SinglePlayerMenu(Menu):
    def __init__(self, manager: UIManager, buttons: Buttons):
        super().__init__(manager, buttons)
        self.buttons.single_player()

    def process_events(self, event: Event):
        if event.ui_element == self.buttons.new_game_button:
            self._new_container = 'sp'
            return self

        if event.ui_element == self.buttons.high_scores_button:
            return HighscoresMenu(self.manager, self.buttons)

        if event.ui_element == self.buttons.sp_btm_button:
            return MainMenu(self.manager, self.buttons)


class MultiplayerMenu(Menu):
    def __init__(self, manager: UIManager, buttons: Buttons):
        super().__init__(manager, buttons)
        self.buttons.multiplayer()

    def process_events(self, event: Event):
        if event.ui_element == self.buttons.hotseat_button:
            self._new_container = 'hs'
            return self

        if event.ui_element == self.buttons.start_server_button:
            self._new_container = 'srv'
            return self

        if event.ui_element == self.buttons.join_server_button:
            self._new_container = 'cln'
            return self

        if event.ui_element == self.buttons.mp_btm_button:
            return MainMenu(self.manager, self.buttons)


class HighscoresMenu(Menu):
    def __init__(self, manager: UIManager, buttons: Buttons):
        super().__init__(manager, buttons)
        self.buttons.highscores()

    def process_events(self, event: Event):
        if event.ui_element == self.buttons.hs_btm_button:
            return MainMenu(self.manager, self.buttons)


class SettingsMenu(Menu):
    def __init__(self, manager: UIManager, buttons: Buttons):
        super().__init__(manager, buttons)
        self.buttons.settings()

    def process_events(self, event: Event):
        if event.ui_element == self.buttons.set_btm_button:
            return MainMenu(self.manager, self.buttons)

        if event.ui_element == self.buttons.settings_resolution:
            #open constants and edit window-parameters
            lines = open('constants.py', 'r').readlines()
            lines[0] = "WINDOWWIDTH = 600\n"
            lines[1] = "WINDOWHEIGHT = 800\n"
            lines[2] = """BACKGROUNDPATH = \"resources/background2.jpg\"\n"""
            new_const = open('constants.py', 'w')
            new_const.writelines(lines)
            new_const.close()
            return SettingsMenu(self.manager, self.buttons)

        if event.ui_element == self.buttons.settings_resolution_2:
            # open constants and edit window-parameters
            lines = open('constants.py', 'r').readlines()
            lines[0] = "WINDOWWIDTH = 1200\n"
            lines[1] = "WINDOWHEIGHT = 800\n"
            lines[2] = """BACKGROUNDPATH = \"resources/background3.jpg\"\n"""
            new_const = open('constants.py', 'w')
            new_const.writelines(lines)
            new_const.close()
            return SettingsMenu(self.manager, self.buttons)

        # if event.ui_element == self.buttons.settings_resolution_dd.current_state == "1600x1200":
        #     print("test")
        #     return MainMenu(self.manager, self.buttons)
