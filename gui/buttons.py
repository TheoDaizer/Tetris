import pygame
import pygame_gui

from constants import WINDOWHEIGHT, WINDOWWIDTH


#  button size
button_size_x = WINDOWWIDTH / 3
button_size_y = WINDOWHEIGHT / 8

#  position in the middle of game window
button_pos_x = WINDOWWIDTH / 2 - button_size_x / 2
button_pos_y = WINDOWHEIGHT / 2 - button_size_y / 2

#  relative X positions
button_pos_x1 = button_pos_x - button_size_x / 2
button_pos_x2 = button_pos_x + button_size_x / 2

#  relative Y positions
button_pos_y1 = button_pos_y - WINDOWHEIGHT / 4
button_pos_y2 = button_pos_y - WINDOWHEIGHT / 8
button_pos_y3 = button_pos_y
button_pos_y4 = button_pos_y + WINDOWHEIGHT / 8
button_pos_y5 = button_pos_y + WINDOWHEIGHT / 4


class Buttons:
    def __init__(self, manager):
        # main menu buttons
        self.single_player_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y1), (button_size_x, button_size_y)),
            text='Single Player',
            manager=manager,
        )

        self.multiplayer_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y2), (button_size_x, button_size_y)),
            text='Multiplayer',
            manager=manager,
        )

        self.settings_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y3), (button_size_x, button_size_y)),
            text='Settings',
            manager=manager,
        )

        self.exit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y4), (button_size_x, button_size_y)),
            text='Exit Tetris',
            manager=manager,
        )

        # single player buttons
        self.new_game_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y2), (button_size_x, button_size_y)),
            text='Start New Game',
            manager=manager,
        )

        self.high_scores_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y3), (button_size_x, button_size_y)),
            text='Highscores',
            manager=manager,
        )

        self.sp_btm_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y4), (button_size_x, button_size_y)),
            text='Back to Menu',
            manager=manager,
        )

        #  multiplayer buttons
        self.hotseat_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y1), (button_size_x, button_size_y)),
            text='Hotseat',
            manager=manager,
        )

        self.start_server_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y2), (button_size_x, button_size_y)),
            text='Start Server',
            manager=manager,
        )

        self.join_server_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y3), (button_size_x, button_size_y)),
            text='Join Server',
            manager=manager,
        )

        self.ip_entry_box = pygame_gui.elements.UITextEntryBox(
            relative_rect=pygame.Rect((button_pos_x2, button_pos_y4), (button_size_x, button_size_y)),
            manager=manager,
        )
        self.ip_entry_box.set_text("e.g. 192.182.1.1")

        self.ip_text_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((button_pos_x1, button_pos_y4), (button_size_x, button_size_y)),
            html_text='Enter Server IP Address',
            manager=manager,
        )

        self.mp_btm_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y5), (button_size_x, button_size_y)),
            text='Back to Menu',
            manager=manager,
        )

        # highscores
        self.highscores_table = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y1), (button_size_x, button_size_y)),
            html_text='Highscores',
            manager=manager,
        )

        self.hs_btm_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y5), (button_size_x, button_size_y)),
            text='Back to Menu',
            manager=manager,
        )

        # settings buttons
        self.settings_resolution = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y3), (button_size_x, button_size_y)),
            html_text='Select Resolution',
            manager=manager,
        )

        self.set_btm_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((button_pos_x, button_pos_y5), (button_size_x, button_size_y)),
            text='Back to Menu',
            manager=manager,
        )

    def main_menu(self):
        self.hide()
        self.single_player_button.visible = True
        self.multiplayer_button.visible = True
        self.settings_button.visible = True
        self.exit_button.visible = True

    def single_player(self):
        self.hide()
        self.new_game_button.visible = True
        self.high_scores_button.visible = True
        self.sp_btm_button.visible = True

    def multiplayer(self):
        self.hide()
        self.start_server_button.visible = True
        self.join_server_button.visible = True
        self.hotseat_button.visible = True
        self.ip_entry_box.visible = True
        self.ip_text_box.visible = True
        self.mp_btm_button.visible = True

    def highscores(self):
        self.hide()
        self.highscores_table.visible = True
        self.hs_btm_button.visible = True

    def settings(self):
        self.hide()
        self.settings_resolution.visible = True
        self.set_btm_button.visible = True

    def hide(self):
        self.single_player_button.visible = False
        self.multiplayer_button.visible = False
        self.settings_button.visible = False
        self.exit_button.visible = False
        self.new_game_button.visible = False
        self.high_scores_button.visible = False
        self.sp_btm_button.visible = False
        self.start_server_button.visible = False
        self.join_server_button.visible = False
        self.hotseat_button.visible = False
        self.ip_entry_box.visible = False
        self.ip_text_box.visible = False
        self.mp_btm_button.visible = False
        self.highscores_table.visible = False
        self.hs_btm_button.visible = False
        self.settings_resolution.visible = False
        self.set_btm_button.visible = False
