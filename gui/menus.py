import sys

import pygame
import pygame_gui

from gui import Buttons


class MainMenu:
    def __init__(self, manager, buttons: Buttons):
        self.manager = manager
        self.btn = buttons

        buttons.hide()
        buttons.single_player_button.visible = True
        buttons.multiplayer_button.visible = True
        buttons.settings_button.visible = True
        buttons.exit_button.visible = True

        self.interface = self

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                print('+++')
                if event.ui_element == self.btn.single_player_button:
                    self.interface = SinglePlayerMenu(self.manager, self.btn)
                if event.ui_element == self.btn.multiplayer_button:
                    self.interface = 'multi_player_menu'

                if event.ui_element == self.btn.settings_button:
                    self.interface = 'settings_menu'

                if event.ui_element == self.btn.exit_button:
                    self.terminate()
            self.manager.process_events(event)

    def terminate(self):
        pygame.quit()
        sys.exit()


class SinglePlayerMenu:
    def __init__(self, manager, buttons: Buttons):
        self.manager = manager
        self.buttons = buttons

        buttons.hide()
        self.new_game_button = buttons.new_game_button.visible = True
        self.high_scores_button = buttons.high_scores_button.visible = True
        self.sp_btm_button = buttons.sp_btm_button.visible = True

        self.interface = self

        self.process_events()

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.new_game_button:
                    self.interface = "single_player_process"
                if event.ui_element == self.high_scores_button:
                    self.interface = 'highscores_menu'
                if event.ui_element == self.sp_btm_button:
                    self.interface = 'main_menu'
            self.manager.process_events(event)
