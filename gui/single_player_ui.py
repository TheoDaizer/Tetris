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

        self.font = pygame.font.Font(pygame.font.get_default_font(), 18)

        # self.sp_ui_panel = pygame_gui.elements.ui_panel.UIPanel(
        #     relative_rect=pygame.Rect((400, 0), (200, 800)),
        #     manager=manager,
        # )

        self.sp_ui_menu_panel = pygame_gui.elements.ui_panel.UIPanel(
            relative_rect=pygame.Rect((100, 200), (250, 400)),
            manager=manager,
            visible=False
        )

        self.element_surface_inner_width = 142
        self.element_surface_inner_height = 102

        self.element_surface_outer_width = 150
        self.element_surface_outer_height = 110

        self.element_frame_image = "resources/elem_frame.png"

        self.element_position_x = 425
        self.element_position_y = 175


        self.sp_next_figure_item_surface = pygame.Surface((self.element_surface_inner_width, self.element_surface_inner_height)) #pos (4, 4)

        # self.sp_next_figure_item = self.renderer.render_figure(self.sp_next_figure_item_surface, Point(1,0), self.game.figure.next_shape_variant, self.game.figure.default_orientation)

        self.sp_next_figure_inner_surface = pygame.Surface((self.element_surface_inner_width, self.element_surface_inner_height))
        self.sp_next_figure_outer_surface = pygame.Surface((self.element_surface_outer_width, self.element_surface_outer_height))
        self.sp_next_figure_outer_surface = self.sp_next_figure_outer_surface.convert_alpha()
        self.sp_next_figure_outer_surface.fill((0, 0, 0, 0))
        self.sp_next_figure_outer_surface.blit(pygame.image.load(self.element_frame_image), (0, 0))

        self.sp_score_surface = pygame.Surface((self.element_surface_outer_width, self.element_surface_outer_height))
        self.sp_score_surface = self.sp_score_surface.convert_alpha()
        self.sp_score_surface.fill((0, 0, 0, 0))
        self.sp_score_text_surface = pygame.Surface((self.element_surface_inner_width, self.element_surface_inner_height))
        self.sp_score_surface.blit(pygame.image.load(self.element_frame_image), (0,0))

        self.sp_level_surface = pygame.Surface((self.element_surface_outer_width, self.element_surface_outer_height))
        self.sp_level_surface = self.sp_level_surface.convert_alpha()
        self.sp_level_surface.fill((0, 0, 0, 0))
        self.sp_level_text_surface = pygame.Surface((self.element_surface_inner_width, self.element_surface_inner_height))
        self.sp_level_surface.blit(pygame.image.load(self.element_frame_image), (0, 0))

        self.sp_burned_rows_surface = pygame.Surface((self.element_surface_outer_width, self.element_surface_outer_height))
        self.sp_burned_rows_surface = self.sp_burned_rows_surface.convert_alpha()
        self.sp_burned_rows_surface.fill((0, 0, 0, 0))
        self.sp_burned_rows_text_surface = pygame.Surface((self.element_surface_inner_width, self.element_surface_inner_height))
        self.sp_burned_rows_surface.blit(pygame.image.load(self.element_frame_image), (0, 0))


        # #elements of game UI
        # self.sp_next_figure_box = pygame_gui.elements.ui_image.UIImage (
        #     relative_rect=pygame.Rect((25, 25), (150, 100)),
        #     image_surface=self.sp_next_figure_surface,
        #     container=self.sp_ui_panel,
        #     manager=manager,
        #     visible=True
        # )
        #
        # self.sp_score_box = pygame_gui.elements.UITextBox(
        #     relative_rect=pygame.Rect((25, 125), (150, 100)),
        #     html_text="<p>Current Score: <br>" + str(self.game.score) + "</p>",
        #     container=self.sp_ui_panel,
        #     manager=manager,
        #     visible=True
        # )
        #
        # self.sp_level_box = pygame_gui.elements.UITextBox(
        #     relative_rect=pygame.Rect((25, 225), (150, 100)),
        #     html_text="<p>Current Level: <br>" + str(self.game.level) + "</p>",
        #     container=self.sp_ui_panel,
        #     manager=manager,
        #     visible=True
        # )
        #
        # self.sp_burned_total_box = pygame_gui.elements.UITextBox(
        #     relative_rect=pygame.Rect((25, 325), (150, 100)),
        #     html_text="<p>Rows burned: <br>" + str(self.game.burned_rows_total) + "</p>",
        #     container=self.sp_ui_panel,
        #     manager=manager,
        #     visible=True
        # )

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
        #score
        self.sp_score_text = self.font.render('Current Score: \n \n' + str(self.game.score), antialias=True,
                                              color=(255, 255, 255))
        self.sp_score_text_surface.fill(pygame.Color('#000000'))
        self.sp_score_text_surface.blit(self.sp_score_text, (10, 10))
        self.sp_score_surface.blit(self.sp_score_text_surface, (4, 4))

        #level
        self.sp_level_text = self.font.render('Current Level: \n \n' + str(self.game.level), antialias=True,
                                              color=(255, 255, 255))
        self.sp_level_text_surface.fill(pygame.Color('#000000'))
        self.sp_level_text_surface.blit(self.sp_level_text, (10, 10))
        self.sp_level_surface.blit(self.sp_level_text_surface, (4, 4))

        #burned rows
        self.sp_burned_rows_text = self.font.render('Burned rows: \n \n' + str(self.game.burned_rows_total), antialias=True,
                                              color=(255, 255, 255))
        self.sp_burned_rows_text_surface.fill(pygame.Color('#000000'))
        self.sp_burned_rows_text_surface.blit(self.sp_burned_rows_text, (10, 10))
        self.sp_burned_rows_surface.blit(self.sp_burned_rows_text_surface, (4, 4))

        #next figure
        self.sp_next_figure_item_surface.fill(pygame.Color('#000000'))
        self.sp_next_figure_inner_surface.fill(pygame.Color('#000000'))
        self.sp_next_figure_item = self.renderer.render_figure(self.sp_next_figure_item_surface, Point(1, 0),
                                                               self.game.figure.next_shape_variant,
                                                               self.game.figure.default_orientation)
        print(self.game.figure.next_shape_variant)
        if self.game.figure.next_shape_variant == 0:
            self.sp_next_figure_inner_surface.blit(self.sp_next_figure_item_surface, (7, 0))
        elif self.game.figure.next_shape_variant == 1:
            self.sp_next_figure_inner_surface.blit(self.sp_next_figure_item_surface, (24, 20))
        elif self.game.figure.next_shape_variant == 2:
            self.sp_next_figure_inner_surface.blit(self.sp_next_figure_item_surface, (-10, 20))
        elif self.game.figure.next_shape_variant == 3:
            self.sp_next_figure_inner_surface.blit(self.sp_next_figure_item_surface, (24, 20))
        elif self.game.figure.next_shape_variant == 4:
            self.sp_next_figure_inner_surface.blit(self.sp_next_figure_item_surface, (20, 20))
        elif self.game.figure.next_shape_variant == 5:
            self.sp_next_figure_inner_surface.blit(self.sp_next_figure_item_surface, (-10, 20))
        elif self.game.figure.next_shape_variant == 6:
            self.sp_next_figure_inner_surface.blit(self.sp_next_figure_item_surface, (7, 20))


        self.sp_next_figure_outer_surface.blit(self.sp_next_figure_inner_surface, (4, 4))
        self.sp_next_figure_outer_surface.blit(pygame.image.load(self.element_frame_image), (0, 0))

        #build elements into main window
        self.sp_surface.blit(self.sp_next_figure_outer_surface, (self.element_position_x, self.element_position_y))
        self.sp_surface.blit(self.sp_score_surface, (self.element_position_x, self.element_position_y + 120))
        self.sp_surface.blit(self.sp_level_surface, (self.element_position_x, self.element_position_y + 240))
        self.sp_surface.blit(self.sp_burned_rows_surface, (self.element_position_x, self.element_position_y + 360))






    # def render (self, surface: Surface):
    #     self.surface = surface
