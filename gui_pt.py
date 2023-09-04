import sys

import pygame
import pygame_gui

from constants import *
from renderer import Renderer
import game
from settings import *
from network import Network, NetworkContainer

if __name__ == '__main__':

    def terminate():
        pygame.quit()
        sys.exit()



class MainMenu:
    def __init__(self):
        self.width = window_width
        self.heigh = window_height

    def process_events (self):


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == single_player_button:
                    self.interface = "single_player_menu"

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == multiplayer_button:
                    self.interface = 'multi_player_menu'

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == settings_button:
                    self.interface = 'settings_menu'

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == exit_button:
                    terminate()

            manager.process_events(event)


    def initialise_menu(self):
        self.interface = "main_menu"
        # here we also define visible UI elements
        single_player_button.visible = True
        multiplayer_button.visible = True
        settings_button.visible = True
        exit_button.visible = True

        self.process_events()

        return str(self.interface)


class SinglePlayerMenu:
    def __init__(self):
        self.interface = "single_player_menu"
        self.width = window_width
        self.heigh = window_height

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()



            manager.process_events(event)



    def initialise_menu(self):
        self.interface = "single_player_menu"
        # here we also define visible UI elements
        single_player_button.visible = False
        multiplayer_button.visible = False
        settings_button.visible = False
        exit_button.visible = False

        self.process_events()

        return str(self.interface)

class SurfaceInterface:
    def __init__(self):
        self.interface = 'main_menu'

    @staticmethod
    def main_menu():
        return main_menu.initialise_menu()

    @staticmethod
    def single_player_menu():
        return single_player.initialise_menu()

    def run(self):
        while True:
            dt = clock.tick(FPS)

            self.interface = getattr(self, self.interface)()

            manager.update(dt)

            window_surface.blit(background, (0, 0))
            manager.draw_ui(window_surface)

            pygame.display.update()

    def buttons_initialisation(self):

        button_size_x = window_width / 3
        button_size_y = window_height / 8

        button_pos_x = window_width / 2 - button_size_x / 2
        button_pos_y = window_height / 2 - button_size_y / 2
        button_pos_y1 = button_pos_y - window_height / 4
        button_pos_y2 = button_pos_y - window_height / 8
        button_pos_y3 = button_pos_y
        button_pos_y4 = button_pos_y + window_height / 8
        button_pos_y5 = button_pos_y + window_height / 4

        confirm_start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y), (button_size_x, button_size_y)),
            text='Press Space to Start',
            manager=manager,
            visible=False
            )

        single_player_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y1), (button_size_x, button_size_y)),
            text='Single Player',
            manager=manager,
            visible=False
            )

        multiplayer_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y2), (button_size_x, button_size_y)),
            text='Multiplayer',
            manager=manager,
            visible=False
            )

        settings_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y3), (button_size_x, button_size_y)),
            text='Settings',
            manager=manager,
            visible=False
            )

        exit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y4), (button_size_x, button_size_y)),
            text='Exit Tetris',
            manager=manager,
            visible=False
            )

if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption('PvP Tetris')
    clock = pygame.time.Clock()

    window_surface = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

    background = pygame.Surface((window_width, window_height))
    background.fill(pygame.Color('#000000'))

    main_menu_background = pygame.Surface((window_width, window_height))
    main_menu_background.fill(pygame.Color('#003000'))

    manager = pygame_gui.UIManager((window_width, window_height))
    main_menu = MainMenu()
    single_player = SinglePlayerMenu()
    tetris_game = game.Game()



    interface = SurfaceInterface()
    interface.buttons_initialisation()
    interface.run()
