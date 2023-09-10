import sys

import pygame
import pygame_gui
import runpy

from constants import *
from game import Game
from settings import *
from renderer import Renderer
from network import Network, NetworkContainer





def terminate():
    pygame.quit()
    sys.exit()



class MainMenu:
    # def __init__(self):
        # self.width = window_width
        # self.heigh = window_height

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
        new_game_button.visible = False
        high_scores_button.visible = False
        sp_btm_button.visible = False
        start_server_button.visible = False
        start_multiplayer_button.visible = False
        ip_entry_box.visible = False
        ip_text_box.visible = False
        mp_btm_button.visible = False
        highscore_table.visible = False
        hs_btm_button.visible = False
        settings_resolution.visible = False
        set_btm_button.visible = False

        self.process_events()

        return str(self.interface)


class SinglePlayerMenu:
    # def __init__(self):
        # self.width = window_width
        # self.heigh = window_height

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == new_game_button:
                    self.interface = "single_player_process"

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == high_scores_button:
                    self.interface = 'highscores_menu'

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == sp_btm_button:
                    self.interface = 'main_menu'

            manager.process_events(event)



    def initialise_menu(self):
        self.interface = "single_player_menu"
        # here we also define visible UI elements
        single_player_button.visible = False
        multiplayer_button.visible = False
        settings_button.visible = False
        exit_button.visible = False
        new_game_button.visible = True
        high_scores_button.visible = True
        sp_btm_button.visible = True
        start_server_button.visible = False
        start_multiplayer_button.visible = False
        ip_entry_box.visible = False
        ip_text_box.visible = False
        mp_btm_button.visible = False
        highscore_table.visible = False
        hs_btm_button.visible = False
        settings_resolution.visible = False
        # settings_resolution_dropdown.visible = False
        set_btm_button.visible = False

        self.process_events()

        return str(self.interface)

class SinglePlayerProcess:
    # def __init__(self):
        # self.width = window_width
        # self.heigh = window_height

    def process_events(self):

        if tetris_game.game_over:
            # pygame.quit()
            # sys.exit()
            self.interface = "main_menu"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                tetris_game.keyboard_input(event)

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
            #         sp_game_running = False



            manager.process_events(event)




    def initialise_menu(self):
        self.interface = "single_player_process"
        # here we also define visible UI elements
        single_player_button.visible = False
        multiplayer_button.visible = False
        settings_button.visible = False
        exit_button.visible = False
        new_game_button.visible = False
        high_scores_button.visible = False
        sp_btm_button.visible = False
        start_server_button.visible = False
        start_multiplayer_button.visible = False
        ip_entry_box.visible = False
        ip_text_box.visible = False
        mp_btm_button.visible = False
        highscore_table.visible = False
        hs_btm_button.visible = False
        settings_resolution.visible = False
        # settings_resolution_dropdown.visible = False
        set_btm_button.visible = False

        self.process_events()

        return str(self.interface)

class HighscoresMenu:
    # def __init__(self):
        # self.width = window_width
        # self.heigh = window_height

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hs_btm_button:
                    self.interface = 'main_menu'

            manager.process_events(event)



    def initialise_menu(self):
        self.interface = "highscores_menu"
        # here we also define visible UI elements
        single_player_button.visible = False
        multiplayer_button.visible = False
        settings_button.visible = False
        exit_button.visible = False
        new_game_button.visible = False
        high_scores_button.visible = False
        sp_btm_button.visible = False
        start_server_button.visible = False
        start_multiplayer_button.visible = False
        ip_entry_box.visible = False
        ip_text_box.visible = False
        mp_btm_button.visible = False
        highscore_table.visible = True
        hs_btm_button.visible = True
        settings_resolution.visible = False
        # settings_resolution_dropdown.visible = False
        set_btm_button.visible = False

        self.process_events()

        return str(self.interface)

class MultiPlayerMenu:
    # def __init__(self):
        # self.width = window_width
        # self.heigh = window_height

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_server_button:
                    # start_server_state = True
                    self.interface = "multi_player_menu"

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_multiplayer_button:
                    self.interface = 'multiplayer_game'

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == mp_btm_button:
                    self.interface = 'main_menu'

            manager.process_events(event)



    def initialise_menu(self):
        self.interface = "multi_player_menu"
        # here we also define visible UI elements
        single_player_button.visible = False
        multiplayer_button.visible = False
        settings_button.visible = False
        exit_button.visible = False
        new_game_button.visible = False
        high_scores_button.visible = False
        sp_btm_button.visible = False
        start_server_button.visible = True
        start_multiplayer_button.visible = True
        ip_entry_box.visible = True
        ip_text_box.visible = True
        mp_btm_button.visible = True
        highscore_table.visible = False
        hs_btm_button.visible = False
        settings_resolution.visible = False
        set_btm_button.visible = False

        self.process_events()

        return str(self.interface)

class SettingsMenu:
    # def __init__(self):
        # self.width = window_width
        # self.heigh = window_height

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()



            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == set_btm_button:
                    self.interface = 'main_menu'

            manager.process_events(event)



    def initialise_menu(self):
        self.interface = "settings_menu"
        # here we also define visible UI elements
        single_player_button.visible = False
        multiplayer_button.visible = False
        settings_button.visible = False
        exit_button.visible = False
        new_game_button.visible = False
        high_scores_button.visible = False
        sp_btm_button.visible = False
        start_server_button.visible = False
        start_multiplayer_button.visible = False
        ip_entry_box.visible = False
        ip_text_box.visible = False
        mp_btm_button.visible = False
        highscore_table.visible = False
        hs_btm_button.visible = False
        settings_resolution.visible = True
        set_btm_button.visible = True

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

    @staticmethod
    def multi_player_menu():
        return multi_player.initialise_menu()

    @staticmethod
    def settings_menu():
        return settings_menu.initialise_menu()

    @staticmethod
    def highscores_menu():
        return highscores_menu.initialise_menu()

    @staticmethod
    def single_player_process():
        return single_player_process.initialise_menu()

    def run(self):
        while True:
            dt = clock.tick(FPS)

            self.interface = getattr(self, self.interface)()

            manager.update(dt)

            window_surface.blit(background, (0, 0))


            if self.interface == "single_player_process":
                tetris_game.update(dt)
                player = NetworkContainer(tetris_game)
                player_2 = None
                game_renderer.render(player, player_2)

            # window_surface.blit(gui_surface, (0, 0))
            manager.draw_ui(window_surface)


            pygame.display.update()





if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption('PvP Tetris')
    clock = pygame.time.Clock()

    window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.RESIZABLE)

    background = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
    background.fill(pygame.Color('#000000'))

    game_field_surface = pygame.Surface((WINDOWWIDTH * 2 // 3, WINDOWHEIGHT))
    game_interface_surface = pygame.Surface((WINDOWWIDTH // 3, WINDOWHEIGHT))


    # game_manager = pygame_gui.UIManager((window_width, window_height))
    # game_manager = pygame_gui.core.interfaces.container_interface.IContainerLikeInterface.get_container(game_manager)


    manager = pygame_gui.UIManager((WINDOWWIDTH, WINDOWHEIGHT))
    main_menu = MainMenu()
    single_player = SinglePlayerMenu()
    single_player_process = SinglePlayerProcess()
    multi_player = MultiPlayerMenu()
    highscores_menu = HighscoresMenu()
    settings_menu = SettingsMenu()
    tetris_game = Game()

    # network = network()
    game_renderer = Renderer(window_surface)


    button_size_x = WINDOWWIDTH / 3
    button_size_y = WINDOWHEIGHT / 8

    #posotion in the middle of game window
    button_pos_x = WINDOWWIDTH / 2 - button_size_x / 2
    button_pos_y = WINDOWHEIGHT / 2 - button_size_y / 2

    #relative X positions
    button_pos_x1 = button_pos_x - button_size_x / 2
    button_pos_x2 = button_pos_x + button_size_x / 2


    #relative Y positions
    button_pos_y1 = button_pos_y - WINDOWHEIGHT / 4
    button_pos_y2 = button_pos_y - WINDOWHEIGHT / 8
    button_pos_y3 = button_pos_y
    button_pos_y4 = button_pos_y + WINDOWHEIGHT / 8
    button_pos_y5 = button_pos_y + WINDOWHEIGHT / 4

    #main menu buttons
    single_player_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_pos_x, button_pos_y1), (button_size_x, button_size_y)),
        text='Single Player',
        manager=manager,
        # container=game_manager,
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

    #single player buttons
    new_game_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_pos_x, button_pos_y2), (button_size_x, button_size_y)),
        text='Start New Game',
        manager=manager,
        visible=False
    )

    high_scores_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_pos_x, button_pos_y3), (button_size_x, button_size_y)),
        text='Highscores',
        manager=manager,
        visible=False
    )

    sp_btm_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_pos_x, button_pos_y4), (button_size_x, button_size_y)),
        text='Back to Menu',
        manager=manager,
        visible=False
    )

    #multi player buttons
    start_server_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_pos_x, button_pos_y2), (button_size_x, button_size_y)),
        text='Start Server',
        manager=manager,
        visible=False
    )

    start_multiplayer_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_pos_x, button_pos_y1), (button_size_x, button_size_y)),
        text='Start Multiplayer Game',
        manager=manager,
        visible=False
    )

    ip_entry_box = pygame_gui.elements.UITextEntryBox(
        relative_rect=pygame.Rect((button_pos_x2, button_pos_y3), (button_size_x, button_size_y)),
        manager=manager,
        visible=False
    )
    ip_entry_box.set_text("e.g. 192.182.1.1")

    ip_text_box = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((button_pos_x1, button_pos_y3), (button_size_x, button_size_y)),
        html_text='Enter Server IP Address',
        manager=manager,
        visible=False
    )

    mp_btm_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_pos_x, button_pos_y4), (button_size_x, button_size_y)),
        text='Back to Menu',
        manager=manager,
        visible=False
    )

    #highscores
    highscore_table = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((button_pos_x, button_pos_y1), (button_size_x, button_size_y)),
        html_text='Highscores',
        manager=manager,
        visible=False
    )

    hs_btm_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_pos_x, button_pos_y5), (button_size_x, button_size_y)),
        text='Back to Menu',
        manager=manager,
        visible=False
    )

    #settings buttons
    settings_resolution = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((button_pos_x, button_pos_y3), (button_size_x, button_size_y)),
        html_text='Select Resulotion',
        manager=manager,
        visible=False
    )

    # settings_resolution_dropdown = pygame_gui.elements.ui_selection_list(
    #     relative_rect=pygame.Rect((button_pos_x, button_pos_y4), (button_size_x, button_size_y)),
    #     item_list = list(tuple("800 x 600", 1), tuple ("1200 x 800", 2)),
    #     manager=manager,
    #     visible=False
    # )

    set_btm_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_pos_x, button_pos_y5), (button_size_x, button_size_y)),
        text='Back to Menu',
        manager=manager,
        visible=False
    )



    interface = SurfaceInterface()

    interface.run()
