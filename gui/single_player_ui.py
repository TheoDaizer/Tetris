import pygame
import pygame_gui
import sys
from typing import Optional
from pygame_gui.ui_manager import UIManager
from pygame.surface import Surface

import game
from game import GameFieldRenderer
from constants import *
from pygame.event import Event
from game.point import Point

class SinglePlayerMenu:
    def __init__(self, manager: UIManager, game: game.Game, sp_surface: Surface):

        self.renderer = GameFieldRenderer()
        self.game = game
        self.sp_surface = sp_surface

        self.pause_state = False

        self.sp_ui_panel = pygame_gui.elements.ui_panel.UIPanel(
            relative_rect=pygame.Rect((400, 0), (200, 800)),
            manager=manager,
        )

        self.sp_ui_menu_panel = pygame_gui.elements.ui_panel.UIPanel(
            relative_rect=pygame.Rect((100, 200), (250, 400)),
            manager=manager,
            visible=False
        )

        self.sp_next_figure_surface = pygame.Surface((150, 100))
        self.sp_next_figure_item = self.renderer.render_figure(self.sp_next_figure_surface, Point(1,0), self.game.figure.next_shape_variant, self.game.figure.default_orientation)

        #elements of game UI
        self.sp_next_figure_box = pygame_gui.elements.ui_image.UIImage (
            relative_rect=pygame.Rect((25, 25), (150, 100)),
            image_surface=self.sp_next_figure_surface,
            container=self.sp_ui_panel,
            manager=manager,
            visible=True
        )

        self.sp_score_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((25, 125), (150, 100)),
            html_text="<p>Current Score: <br>" + str(self.game.score) + "</p>",
            container=self.sp_ui_panel,
            manager=manager,
            visible=True
        )

        self.sp_level_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((25, 225), (150, 100)),
            html_text="<p>Current Level: <br>" + str(self.game.level) + "</p>",
            container=self.sp_ui_panel,
            manager=manager,
            visible=True
        )

        self.sp_burned_total_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((25, 325), (150, 100)),
            html_text="<p>Rows burned: <br>" + str(self.game.burned_rows_total) + "</p>",
            container=self.sp_ui_panel,
            manager=manager,
            visible=True
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
            relative_rect=pygame.Rect((25, 75), (200, 100)),
            text='On/Off Music',
            container=self.sp_ui_menu_panel,
            manager=manager,
            visible=False
        )



    def event_handler (self, event: Event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if self.sp_ui_menu_panel.visible == False:
                    self.sp_ui_menu_panel.visible = True
                    self.sp_btm_button.visible = True
                    self.sp_mute_music_button.visible = True
                    self.pause_state = True
                    # self.music.stop()
                else:
                    self.sp_ui_menu_panel.visible = False
                    self.sp_btm_button.visible = False
                    self.pause_state = False
                    self.sp_mute_music_button.visible = False
                    self.sp_surface.blit(pygame.image.load(BACKGROUNDPATH), (0, 0))
                    # self.music.play(-1)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.sp_btm_button:
                self.game.is_game_over = True
                # self.music.stop()
                # self.game_over.play()
                return 'menu'

            # if event.ui_element == self.sp_mute_music_button:
            #     if self.music.get_volume() == 0.5:
            #         self.freeze_sound.set_volume(0)
            #         self.burn_sound.set_volume(0)
            #         self.game_over.set_volume(0)
            #         self.music.set_volume(0)
            #     else:
            #         self.freeze_sound.set_volume(0.5)
            #         self.burn_sound.set_volume(0.5)
            #         self.game_over.set_volume(0.1)
            #         self.music.set_volume(0.5)

    def update (self):
        self.sp_score_box.set_text("<p>Current Score: <br>" + str(self.game.score) + "</p>")
        self.sp_level_box.set_text("<p>Current Level: <br>" + str(self.game.level) + "</p>")
        self.sp_burned_total_box.set_text("<p>Rows burned: <br>" + str(self.game.burned_rows_total) + "</p>")

        self.sp_next_figure_surface.fill(pygame.Color('#000000'))
        self.sp_next_figure_item = self.renderer.render_figure(self.sp_next_figure_surface, Point(1, 0),
                                                               self.game.figure.next_shape_variant,
                                                               self.game.figure.default_orientation)

        self.sp_next_figure_box.set_image(self.sp_next_figure_surface)