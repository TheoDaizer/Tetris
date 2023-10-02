import pygame
import pygame_gui

from pygame_gui.ui_manager import UIManager
from pygame.surface import Surface

from game import GameDataContainer, GameFieldRenderer
from constants import *
from pygame.event import Event
from game.point import Point

from .gui_elements_sp_mp import NextFigureElement, ScoreBoxElement, LevelBoxElement, RowsBoxElement

from .abc_gui_element import GuiElement


class SinglePlayerMenu:
    next_figure_coordinates = ((7, 0), (24, 20), (-10, 20), (24, 20), (20, 20), (-10, 20), (7, 20))

    def __init__(self, manager: UIManager, game_data: GameDataContainer, sp_surface: Surface, music):

        self.renderer = GameFieldRenderer()
        self.sp_surface = sp_surface
        self.game_data = game_data
        self.music = music

        self.pause_state = False
        self.is_game_over = False

        self.test_window = NextFigureElement(426, 135, self.sp_surface, game_data)
        self.test_window2 = ScoreBoxElement(426, 325, self.sp_surface, game_data)
        self.test_window3 = LevelBoxElement(426, 460, self.sp_surface, game_data)
        self.test_window4 = RowsBoxElement(426, 595, self.sp_surface, game_data)

        self.font = pygame.font.Font("resources/MightyKingdom.ttf", 32)
        self.sp_ui_menu_panel = pygame_gui.elements.ui_panel.UIPanel(
            relative_rect=pygame.Rect((175, 200), (250, 400)),
            manager=manager,
            visible=False
        )

        self.element_surface_inner_width_big = 142
        self.element_surface_inner_height_big = 102
        self.element_surface_outer_width_big = 150
        self.element_surface_outer_height_big = 110

        self.element_surface_inner_width_small = 102
        self.element_surface_inner_height_small = 50
        self.element_surface_outer_width_small = 110
        self.element_surface_outer_height_small = 60

        self.element_surface_inner_width_small2 = 116
        self.element_surface_inner_height_small2 = 40
        self.element_surface_outer_width_small2 = 150
        self.element_surface_outer_height_small2 = 60

        self.element_frame_image = "resources/elem_frame.png"

        self.element_position_x = 435
        self.element_position_y = 175

        #elements of ESC menu
        self.sp_btm_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((25, 275), (200, 100)),
            text='Back to Menu',
            container=self.sp_ui_menu_panel,
            manager=manager,
            visible=False
        )

        self.sp_mute_music_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((25, 25), (200, 100)),
            text='On/Off Music',
            container=self.sp_ui_menu_panel,
            manager=manager,
            visible=False
        )

    def key_esc_down(self):
        self.sp_ui_menu_panel.visible = not self.sp_ui_menu_panel.visible
        self.sp_btm_button.visible = not self.sp_btm_button.visible
        self.sp_mute_music_button.visible = not self.sp_mute_music_button.visible
        self.pause_state = not self.pause_state
            # self.music.stop()

            # self.sp_surface.blit(pygame.image.load(background), (0, 0))
            # self.music.play(-1)

    def button_pressed(self, event: Event):
        if event.ui_element == self.sp_btm_button:
            self.is_game_over = True
            return

        if event.ui_element == self.sp_mute_music_button:
            if self.music.get_volume() == 0.5:
                # self.freeze_sound.set_volume(0)
                # self.burn_sound.set_volume(0)
                # self.game_over.set_volume(0)
                self.music.set_volume(0)
            else:
                # self.music.freeze_sound.set_volume(0.5)
                # self.music.burn_sound.set_volume(0.5)
                # self.music.game_over.set_volume(0.1)
                self.music.set_volume(0.5)

    def update(self, game_data: GameDataContainer):

        self.test_window.update(game_data)
        self.test_window2.update(game_data)
        self.test_window3.update(game_data)
        self.test_window4.update(game_data)

        if self.game_data.field is not None:
            self.test_window.render()
            self.test_window2.render()
            self.test_window3.render()
            self.test_window4.render()


    # def render (self):


