import pygame
import pygame_gui

from pygame_gui.ui_manager import UIManager
from pygame.surface import Surface

from game import GameDataContainer, GameFieldRenderer
from constants import *
from pygame.event import Event

from .gui_elements import NextFigureElement, ScoreBoxElement, LevelBoxElement, RowsBoxElement


class SinglePlayerMenu:

    next_fig_elem_x = 426
    next_fig_elem_y = 135
    score_elem_x = 426
    score_elem_y = 325
    level_elem_x = 426
    level_elem_y = 460
    rows_elem_x = 426
    rows_elem_y = 595

    def __init__(self, manager: UIManager, game_data: GameDataContainer, sp_surface: Surface, music):

        self.renderer = GameFieldRenderer()
        self.sp_surface = sp_surface
        self.game_data = game_data
        self.music = music

        self.pause_state = False
        self.is_game_over = False

        self.next_figure = NextFigureElement(self.next_fig_elem_x, self.next_fig_elem_y, self.sp_surface, game_data)
        self.score = ScoreBoxElement(self.score_elem_x, self.score_elem_y, self.sp_surface, game_data)
        self.level = LevelBoxElement(self.level_elem_x, self.level_elem_y, self.sp_surface, game_data)
        self.rows = RowsBoxElement(self.rows_elem_x, self.rows_elem_y, self.sp_surface, game_data)

        self.gui_content_surface = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT), pygame.SRCALPHA)

        self.sp_ui_menu_panel = pygame_gui.elements.ui_panel.UIPanel(
            relative_rect=pygame.Rect((175, 200), (250, 400)),
            manager=manager,
            visible=False
        )

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

    def button_pressed(self, event: Event):
        if event.ui_element == self.sp_btm_button:
            self.is_game_over = True
            return

        if event.ui_element == self.sp_mute_music_button:
            if self.music.get_volume() == 0.5:
                self.music.set_volume(0)
            else:
                self.music.set_volume(0.5)

    def update(self, game_data: GameDataContainer):

        self.next_figure.update(game_data)
        self.score.update(game_data)
        self.level.update(game_data)
        self.rows.update(game_data)

    def render (self):

        self.gui_content_surface.fill((0, 0, 0, 0))

        if self.next_figure.is_changed:
            self.gui_content_surface.blit(self.next_figure.render(), (self.next_figure.pos_x_bg, self.next_figure.pos_y_bg))

        if self.score.is_changed:
            self.gui_content_surface.blit(self.score.render(), (self.score.pos_x_bg, self.score.pos_y_bg))

        if self.level.is_changed:
            self.gui_content_surface.blit(self.level.render(), (self.level.pos_x_bg, self.level.pos_y_bg))

        if self.rows.is_changed:
            self.gui_content_surface.blit(self.rows.render(), (self.rows.pos_x_bg, self.rows.pos_y_bg))

        return self.gui_content_surface


