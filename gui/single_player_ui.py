import pygame
import pygame_gui

from pygame_gui.ui_manager import UIManager
from pygame.surface import Surface

from game import GameDataContainer, GameFieldRenderer
from constants import *
from pygame.event import Event
from game.point import Point

from .ui_elements_sp_mp import NextFigureElement

from .abc_gui_element import GuiElement


class SinglePlayerMenu:
    next_figure_coordinates = ((7, 0), (24, 20), (-10, 20), (24, 20), (20, 20), (-10, 20), (7, 20))

    def __init__(self, manager: UIManager, game_data: GameDataContainer, sp_surface: Surface):

        self.renderer = GameFieldRenderer()
        self.sp_surface = sp_surface
        self.game_data = game_data

        self.pause_state = False
        self.is_game_over = False

        self.test_window = NextFigureElement(132, 91, 435, 175, self.sp_surface, game_data)

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

        # self.sp_next_figure_item_surface = pygame.Surface((self.element_surface_inner_width_big, self.element_surface_inner_height_big)) #pos (4, 4)
        # self.sp_next_figure_item_surface = self.sp_next_figure_item_surface.convert_alpha()
        # self.sp_next_figure_item_surface.fill((0, 0, 0, 0))
        #
        # self.sp_next_figure_item = self.renderer.render_figure(self.sp_next_figure_item_surface, Point(1, 0),
        #                                                        game_data.next_shape_variant, 0)
        #
        # self.sp_next_figure_inner_surface = pygame.Surface((self.element_surface_inner_width_big, self.element_surface_inner_height_big))
        # self.sp_next_figure_inner_surface = self.sp_next_figure_inner_surface.convert_alpha()
        # self.sp_next_figure_inner_surface.fill((255, 255, 255, 75))
        # self.sp_next_figure_outer_surface = pygame.Surface((self.element_surface_outer_width_big, self.element_surface_outer_height_big))
        # self.sp_next_figure_outer_surface = self.sp_next_figure_outer_surface.convert_alpha()
        # self.sp_next_figure_outer_surface.fill((0, 0, 0, 0))
        # self.sp_next_figure_outer_surface.blit(pygame.image.load(self.element_frame_image), (0, 0))

        # self.sp_level_inner_surface = pygame.Surface(
        #     (self.element_surface_inner_width_big, self.element_surface_inner_height_big))
        # self.sp_level_inner_surface = self.sp_level_inner_surface.convert_alpha()
        # self.sp_level_inner_surface.fill((255, 255, 255, 75))
        # self.sp_level_outer_surface = pygame.Surface((self.element_surface_outer_width_big, self.element_surface_outer_height_big))
        # self.sp_level_outer_surface = self.sp_level_outer_surface.convert_alpha()
        # self.sp_level_outer_surface.fill((0, 0, 0, 0))
        # self.sp_level_text_surface = pygame.Surface((self.element_surface_inner_width_big, self.element_surface_inner_height_big))
        # self.sp_level_text_surface = self.sp_level_outer_surface.convert_alpha()
        # self.sp_level_text_surface.fill((0, 0, 0, 0))
        # self.sp_level_outer_surface.blit(pygame.image.load(self.element_frame_image), (0, 0))
        #
        # self.sp_burned_rows_inner_surface = pygame.Surface(
        #     (self.element_surface_inner_width_big, self.element_surface_inner_height_big))
        # self.sp_burned_rows_inner_surface = self.sp_burned_rows_inner_surface.convert_alpha()
        # self.sp_burned_rows_inner_surface.fill((255, 255, 255, 75))
        # self.sp_burned_rows_outer_surface = pygame.Surface((self.element_surface_outer_width_big, self.element_surface_outer_height_big))
        # self.sp_burned_rows_outer_surface = self.sp_burned_rows_outer_surface.convert_alpha()
        # self.sp_burned_rows_outer_surface.fill((0, 0, 0, 0))
        # self.sp_burned_rows_text_surface = pygame.Surface((self.element_surface_inner_width_big, self.element_surface_inner_height_big))
        # self.sp_burned_rows_outer_surface.blit(pygame.image.load(self.element_frame_image), (0, 0))
        #
        # #score label
        # self.sp_score_label_inner_surface = pygame.Surface(
        #     (self.element_surface_inner_width_small, self.element_surface_inner_height_small))
        # self.sp_score_label_inner_surface = self.sp_score_label_inner_surface.convert_alpha()
        # self.sp_score_label_inner_surface.fill((255, 255, 255, 75))
        # self.sp_score_label_outer_surface = pygame.Surface(
        #     (self.element_surface_outer_width_small, self.element_surface_outer_height_small))
        # self.sp_score_label_outer_surface = self.sp_score_label_outer_surface.convert_alpha()
        # self.sp_score_label_outer_surface.fill((0, 0, 0, 0))
        # self.sp_score_label_text_surface = pygame.Surface(
        #     (self.element_surface_inner_width_big, self.element_surface_inner_height_big))
        # self.sp_score_label_text_surface = self.sp_score_label_text_surface.convert_alpha()
        # self.sp_score_label_text_surface.fill((0, 0, 0, 0))
        #
        # self.sp_score_label_text = self.font.render('Score', antialias=True,
        #                                       color=(0, 0, 0))
        # self.sp_score_label_text_surface.blit(self.sp_score_label_text, (10, 5))
        # self.sp_score_label_inner_surface.blit(self.sp_score_label_text_surface, (0, 0))
        # self.sp_score_label_outer_surface.blit(self.sp_score_label_inner_surface, (4, 5))
        # self.sp_score_label_outer_surface.blit(pygame.image.load("resources/elem_frame_small.png"), (0, 0))
        #
        # self.sp_surface.blit(self.sp_score_label_outer_surface, (self.element_position_x, self.element_position_y + 120))
        #
        # #score
        # self.sp_score_inner_surface = pygame.Surface(
        #     (self.element_surface_inner_width_small2, self.element_surface_inner_height_small2))
        # self.sp_score_inner_surface = self.sp_score_inner_surface.convert_alpha()
        # self.sp_score_inner_surface.fill((0, 0, 0, 0))
        # self.sp_score_outer_surface = pygame.Surface(
        #     (self.element_surface_outer_width_small2, self.element_surface_outer_height_small2))
        # self.sp_score_outer_surface = self.sp_score_outer_surface.convert_alpha()
        # self.sp_score_outer_surface.fill((0, 0, 0, 0))
        # self.sp_score_text_surface = pygame.Surface(
        #     (self.element_surface_inner_width_small2, self.element_surface_inner_height_small2))
        # self.sp_score_text_surface = self.sp_score_text_surface.convert_alpha()
        # self.sp_score_text_surface.fill((0, 0, 0, 0))
        #
        # self.sp_score = 0
        # self.sp_score_text = self.font.render('0', antialias=True,
        #                                       color=(0, 0, 0))
        # self.sp_score_text_surface.blit(self.sp_score_text, (0, 0))
        # self.sp_score_inner_surface.blit(self.sp_score_text_surface, (0, 0))
        # self.sp_score_outer_surface.blit(pygame.image.load("resources/score_bar2.png"), (0, 0))
        # self.sp_score_outer_surface.blit(self.sp_score_inner_surface, (17, 12))
        #
        # self.sp_surface.blit(self.sp_score_outer_surface,
        #                      (self.element_position_x, self.element_position_y + 220))

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

    def update(self, game_data: GameDataContainer):
        #score
        # if game_data.score > self.sp_score:
            # self.sp_surface.blit(pygame.image.load(background), (0, 0))
            # self.sp_surface.blit(self.sp_score_label_outer_surface,
            #                      (self.element_position_x, self.element_position_y + 120))
            # self.sp_score_text_surface.fill((0, 0, 0, 0))
            # self.sp_score_inner_surface.fill((0, 0, 0, 0))
            # self.sp_score_outer_surface.fill((0, 0, 0, 0))
            # self.sp_score = game_data.score
            # self.sp_score_text = self.font.render(f'{self.sp_score}', antialias=True, color=(0, 0, 0))
            # self.sp_score_text_surface.blit(self.sp_score_text, (0, 0))
            # self.sp_score_inner_surface.blit(self.sp_score_text_surface, (0, 0))
            # self.sp_score_outer_surface.blit(pygame.image.load("resources/score_bar2.png"), (0, 0))
            # self.sp_score_outer_surface.blit(self.sp_score_inner_surface, (17, 12))
            #
            # self.sp_score_outer_surface.blit(self.test_window.background, (0, 0))

        print(game_data.next_shape_variant)
        print("from new below")
        self.test_window.update(game_data)

        #next figure
        if game_data.field is not None:
            # # level
            # self.sp_level_text = self.font.render('Current Level: \n \n' + str(game_data.level), antialias=True,
            #                                       color=(0, 0, 0))
            # # self.sp_level_text_surface.fill(pygame.Color('#000000'))
            # self.sp_level_text_surface.blit(self.sp_level_text, (5, 5))
            # self.sp_level_outer_surface.blit(self.sp_level_text_surface, (4, 4))
            # self.sp_level_outer_surface.blit(pygame.image.load(self.element_frame_image), (0, 0))
            #
            # # burned rows
            # self.sp_burned_rows_text = self.font.render('Burned rows: \n \n' + str(game_data.burned_rows_total),
            #                                             antialias=True,
            #                                             color=(255, 255, 255))
            # self.sp_burned_rows_text_surface.fill(pygame.Color('#000000'))
            # self.sp_burned_rows_text_surface.blit(self.sp_burned_rows_text, (5, 5))
            # self.sp_burned_rows_outer_surface.blit(self.sp_burned_rows_text_surface, (4, 4))
            # self.sp_burned_rows_outer_surface.blit(pygame.image.load(self.element_frame_image), (0, 0))


            self.test_window.render()
            # #self.sp_surface.blit(pygame.image.load(BACKGROUNDPATH), (0, 0))
            # self.sp_surface.blit(self.sp_score_label_outer_surface,
            #                      (self.element_position_x, self.element_position_y + 120))
            #
            # self.sp_next_figure_outer_surface.fill((0, 0, 0, 0))
            # self.sp_next_figure_inner_surface.fill((255, 255, 255, 75))
            # self.sp_next_figure_item_surface.fill((0, 0, 0, 0))
            # self.sp_next_figure_item = self.renderer.render_figure(self.sp_next_figure_item_surface, Point(1, 0),
            #                                                        game_data.next_shape_variant,0)
            #
            # coordinates = self.next_figure_coordinates[game_data.next_shape_variant]
            # self.sp_next_figure_inner_surface.blit(self.sp_next_figure_item_surface, coordinates)
            # self.sp_next_figure_outer_surface.blit(self.sp_next_figure_inner_surface, (4, 4))
            # self.sp_next_figure_outer_surface.blit(pygame.image.load(self.element_frame_image), (0, 0))

            # self.sp_surface.blit(self.sp_next_figure_outer_surface, (self.element_position_x, self.element_position_y))

            #build elements into main window
            # self.sp_surface.blit(self.sp_next_figure_outer_surface, (self.element_position_x, self.element_position_y))
            # self.sp_surface.blit(self.sp_score_outer_surface, (self.element_position_x, self.element_position_y + 220))
            # self.sp_surface.blit(self.sp_level_outer_surface, (self.element_position_x, self.element_position_y + 340))
            # self.sp_surface.blit(self.sp_burned_rows_outer_surface, (self.element_position_x, self.element_position_y + 460))


    # def render (self, surface: Surface):
    #     self.surface = surface
