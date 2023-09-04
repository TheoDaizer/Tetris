import sys

import pygame
import pygame_gui

from constants import *
from render import render
import game
from settings import *

if __name__ == '__main__':

    def terminate():
        pygame.quit()
        sys.exit()


    def waitForPlayerToPressKey():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Нажатие ESC осуществляет выход.
                        terminate()
                    return

    def starting_screen():

        while True:

            confirm_start_button.visible = True

            dt_frame = clock.tick(FPS)  # time from previous frame in milliseconds. argument provides fps limitation
            dt_input = dt_frame / 1000.0  # time from previous input recognition in milliseconds, divisor for refresh rate

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 'single_plyer'

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == confirm_start_button:
                        return 'single_plyer'
                    # if event.ui_element == options:
                    #     return 'options'

                manager.process_events(event)

            manager.update(dt_input)

            window_surface.blit(background, (0, 0))
            manager.draw_ui(window_surface)

            pygame.display.update()

    def single_plyer():

        tetris_game = game.Game()
        running = True
        clock.tick()  # time restart
        while True:
            dt = clock.tick(FPS)  # time from previous frame in milliseconds. argument provides fps limitation

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "starting_screen"

            tetris_game.update(dt_frame)

            window_surface.fill("black")  # "clearing screen" by filling it with one color
            render(tetris_game, window_surface)
            pygame.display.flip()  # updating screen


class MainMenu:
    def __init__(self):
        self.interface = "main_menu"
        self.width = window_width
        self.heigh = window_height

    def interface (self):
        self.interface = getattr(self, self.interface)

    def refresh_menu (self):

        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == single_player_button:
                    return 'single_plyer_menu'

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == multiplayer_button:
                    return 'multi_player_menu'

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == settings_button:
                    return 'settings_menu'

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == exit_button:
                    return 'exit'

            manager.process_events(event)

        manager.update(dt)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()

    def initialise_loop(self):
        Running = True
        while Running:
            # here we also define visible UI elements
            single_player_button.visible = True
            multiplayer_button.visible = True
            settings_button.visible = True
            exit_button.visible = True

            self.refresh_menu()

class SettingsMenu:
    def __init__(self):
        self.interface = "settings_menu"
        self.width = window_width
        self.heigh = window_height

    def interface (self):
        self.interface = getattr(self, self.interface)

    def refresh_menu ():

        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == confirm_start_button:
                    return 'single_plyer'

            manager.process_events(event)

        manager.update(dt)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()

    def initialise_loop(self):
        Running = True
        while Running:
            # here we also define visible UI elements

            self.refresh_menu()


class SurfaceInterface:
    def __init__(self):
        self.interface = 'main_menu'

    @staticmethod
    def main_menu():
        return main_menu.initialise_loop()

    @staticmethod
    def single_plyer():
        return single_plyer()

    def run(self):
        while True:
            self.interface = getattr(self, self.interface)()

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

    button_size_x = window_width/3
    button_size_y = window_height/8
    button_pos_x = window_width/2 - button_size_x/2
    button_pos_y = window_height/2 - button_size_y/2
    button_pos_y1 = button_pos_y + window_height/4
    button_pos_y2 = button_pos_y + window_height/8
    button_pos_y3 = button_pos_y - window_height/8
    button_pos_y4 = button_pos_y - window_height/4


    confirm_start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((button_pos_x, button_pos_y), (button_size_x, button_size_y)),
                                                        text='Press Space to Start',
                                                        manager=manager,
                                                        visible=False
                                                        )

    single_player_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((button_pos_x, button_pos_y1), (button_size_x, button_size_y)),
                                                        text='Single Player',
                                                        manager=manager,
                                                        visible=False
                                                        )

    multiplayer_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((button_pos_x, button_pos_y2), (button_size_x, button_size_y)),
                                                        text='Multiplayer',
                                                        manager=manager,
                                                        visible=False
                                                        )

    settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((button_pos_x, button_pos_y3), (button_size_x, button_size_y)),
                                                   text='Settings',
                                                   manager=manager,
                                                   visible=False
                                                   )

    exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((button_pos_x, button_pos_y4), (button_size_x, button_size_y)),
                                                      text='Exit Tetris',
                                                      manager=manager,
                                                      visible=False
                                                      )


    interface = SurfaceInterface()
    interface.run()
