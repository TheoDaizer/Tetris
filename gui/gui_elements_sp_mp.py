import pygame
from pygame import Rect

from pygame.surface import Surface

from game import GameDataContainer
from game.figure import SHAPES
from game.colors import COLORS
from gui.abc_gui_element import GuiElement
from .gui_constants import *
from constants import *


class NextFigureElement (GuiElement):
    next_figure_coordinates = ((438, 171), (455, 191), (421, 191), (455, 191), (451, 191), (421, 191), (438, 191))
    block_image = pygame.image.load("resources/tetris_block.png")
    426, 165,

    def __init__(self, x: int, y: int, background: Surface, game_data: GameDataContainer):

        self.game_data = game_data
        self.width = 132
        self.height = 91
        self.pos_x_frame = x
        self.pos_y_frame = y
        self.pos_x_bg = x + 9
        self.pos_y_bg = y + 10
        self.background_main = background

        self.next_figure_coordinates = ((x + 8, y + 6), (x + 29, y + 26), (x - 5, y + 26), (x + 29, y + 26), (x + 25, y + 26), (x - 5, y + 26), (x + 12, y + 26))

        self.sp_next_figure_item_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        self.sp_next_figure_inner_surface = pygame.Surface(
            (element_inner_width_1, element_inner_height_1), pygame.SRCALPHA)
        self.sp_next_figure_inner_surface.fill((255, 255, 255, 75))

        self.sp_next_figure_outer_surface = pygame.Surface(
            (element_outer_width_1, element_outer_height_1), pygame.SRCALPHA)
        self.sp_next_figure_outer_surface.blit(self.sp_next_figure_inner_surface, (5, 6))
        self.sp_next_figure_outer_surface.blit(pygame.image.load("resources/elem_frame.png"), (0, 0))

        self.background_main.blit(self.sp_next_figure_outer_surface, (self.pos_x_frame, self.pos_y_frame))
        self.background = self.background_main.subsurface(Rect(self.pos_x_bg, self.pos_y_bg, self.width, self.height))

        self.sp_next_figure_test_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.sp_next_figure_test_surface.blit(self.background, (0, 0))

    def update(self, game_data):
        self.game_data = game_data
        self.next_shape = self.game_data.next_shape_variant
        self.coordinates = self.next_figure_coordinates[self.game_data.next_shape_variant]

    def render(self):
        self.sp_next_figure_item_surface.fill((0, 0, 0, 0))

        for dx, dy in SHAPES[self.next_shape][0]:
            x = 1 + dx
            y = 0 + dy
            self.render_block(self.sp_next_figure_item_surface, (x, y), self.next_shape)

        self.background_main.blit(self.sp_next_figure_test_surface, (self.pos_x_bg, self.pos_y_bg))
        self.background_main.blit(self.sp_next_figure_item_surface, self.coordinates)

    def render_block(self, surface, position: tuple[int, int], shape_variant: int, x_shift: bool = False):
        x, y = position
        rect = pygame.Rect(x * TILESIZE + x_shift, y * TILESIZE, TILESIZE, TILESIZE)
        pygame.draw.rect(surface, COLORS[shape_variant], rect, 0)
        surface.blit(self.block_image, (x * TILESIZE + x_shift, y * TILESIZE))


class ScoreBoxElement (GuiElement):
    def __init__(self, x: int, y: int, background: Surface, game_data: GameDataContainer):

        self.game_data = game_data
        self.width = 125
        self.height = 38
        self.pos_x_frame = x
        self.pos_y_frame = y
        self.pos_x_bg = x + 12
        self.pos_y_bg = y + 11
        self.pos_x_label = x + 20
        self.pos_y_label = y - element_outer_height_2 - 2
        self.background_main = background
        self.font = pygame.font.Font("resources/MightyKingdom.ttf", 36)
        self.font2 = pygame.font.Font("resources/MightyKingdom.ttf", 24)

        #score label
        self.sp_score_label_inner_surface = pygame.Surface(
            (element_inner_width_2, element_inner_height_2), pygame.SRCALPHA)
        self.sp_score_label_inner_surface.fill((255, 255, 255, 75))
        self.sp_score_label_outer_surface = pygame.Surface(
            (element_outer_width_2, element_outer_height_2), pygame.SRCALPHA)
        self.sp_score_label_text_surface = pygame.Surface((element_inner_width_2, element_inner_height_2),
                                                          pygame.SRCALPHA)

        self.sp_score_label_text = self.font.render('Score', antialias=True,
                                                    color=(0, 0, 0))
        self.sp_score_label_text_surface.blit(self.sp_score_label_text, (0, 0))
        self.sp_score_label_inner_surface.blit(self.sp_score_label_text_surface, (5, 0))
        self.sp_score_label_outer_surface.blit(self.sp_score_label_inner_surface, (4, 5))
        self.sp_score_label_outer_surface.blit(pygame.image.load("resources/elem_frame_small.png"), (0, 0))

        self.background_main.blit(self.sp_score_label_outer_surface,
                             (self.pos_x_label, self.pos_y_label))

        #score
        self.sp_score_outer_surface = pygame.Surface(
            (element_outer_width_3, element_outer_height_3), pygame.SRCALPHA)
        self.sp_score_text_surface = pygame.Surface(
            (self.width, self.height), pygame.SRCALPHA)
        self.sp_score_outer_surface.blit(pygame.image.load("resources/score_bar2.png"), (0, 0))
        self.background_main.blit(self.sp_score_outer_surface, (self.pos_x_frame, self.pos_y_frame))

        self.background = self.background_main.subsurface(Rect(self.pos_x_bg, self.pos_y_bg, self.width, self.height))
        self.sp_score_inner_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.sp_score_inner_surface.blit(self.background, (0, 0))

    def update(self, game_data: GameDataContainer):
        self.game_data = game_data
        self.sp_score = self.game_data.score
        if len(str(self.sp_score)) <= 6:
            self.sp_score_text = self.font.render(str(self.sp_score), antialias=True,
                                              color=(0, 0, 0))
            self.text_offset = -5

        else:
            self.sp_score_text = self.font2.render(str(self.sp_score), antialias=True,
                                                  color=(0, 0, 0))
            self.text_offset = 4

    def render(self):
        self.sp_score_text_surface.fill((0, 0, 0, 0))
        self.sp_score_text_surface.blit(self.sp_score_text, (0, self.text_offset))

        self.background_main.blit(self.sp_score_inner_surface, (self.pos_x_bg, self.pos_y_bg))
        self.background_main.blit(self.sp_score_text_surface, (self.pos_x_bg, self.pos_y_bg))

class LevelBoxElement (GuiElement):
    def __init__(self, x: int, y: int, background: Surface, game_data: GameDataContainer):

        self.game_data = game_data
        self.width = 125
        self.height = 38
        self.pos_x_frame = x
        self.pos_y_frame = y
        self.pos_x_bg = x + 12
        self.pos_y_bg = y + 11
        self.pos_x_label = x + 20
        self.pos_y_label = y - element_outer_height_2 - 2
        self.background_main = background
        self.font = pygame.font.Font("resources/MightyKingdom.ttf", 36)
        # self.font2 = pygame.font.Font("resources/MightyKingdom.ttf", 24)


        #level label
        self.sp_level_label_inner_surface = pygame.Surface(
            (element_inner_width_2, element_inner_height_2), pygame.SRCALPHA)
        self.sp_level_label_inner_surface.fill((255, 255, 255, 75))

        self.sp_level_label_outer_surface = pygame.Surface(
            (element_outer_width_2, element_outer_height_2), pygame.SRCALPHA)

        self.sp_level_label_text_surface = pygame.Surface((element_inner_width_2, element_inner_height_2),
                                                          pygame.SRCALPHA)

        self.sp_level_label_text = self.font.render('Level', antialias=True,
                                                    color=(0, 0, 0))
        self.sp_level_label_text_surface.blit(self.sp_level_label_text, (0, 0))
        self.sp_level_label_inner_surface.blit(self.sp_level_label_text_surface, (5, 0))
        self.sp_level_label_outer_surface.blit(self.sp_level_label_inner_surface, (4, 5))
        self.sp_level_label_outer_surface.blit(pygame.image.load("resources/elem_frame_small.png"), (0, 0))

        self.background_main.blit(self.sp_level_label_outer_surface,
                             (self.pos_x_label, self.pos_y_label))

        #level
        self.sp_level_outer_surface = pygame.Surface(
            (element_outer_width_3, element_outer_height_3), pygame.SRCALPHA)
        self.sp_level_text_surface = pygame.Surface(
            (self.width, self.height), pygame.SRCALPHA)
        self.sp_level_outer_surface.blit(pygame.image.load("resources/score_bar2.png"), (0, 0))
        self.background_main.blit(self.sp_level_outer_surface, (self.pos_x_frame, self.pos_y_frame))

        self.background = self.background_main.subsurface(Rect(self.pos_x_bg, self.pos_y_bg, self.width, self.height))
        self.sp_level_inner_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.sp_level_inner_surface.blit(self.background, (0, 0))

    def update(self, game_data: GameDataContainer):
        self.game_data = game_data
        self.sp_level = self.game_data.level
        self.sp_level_text = self.font.render(str(self.sp_level), antialias=True,
                                              color=(0, 0, 0))
        self.text_offset = -5

    def render(self):
        self.sp_level_text_surface.fill((0, 0, 0, 0))
        self.sp_level_text_surface.blit(self.sp_level_text, (0, self.text_offset))

        self.background_main.blit(self.sp_level_inner_surface, (self.pos_x_bg, self.pos_y_bg))
        self.background_main.blit(self.sp_level_text_surface, (self.pos_x_bg, self.pos_y_bg))

class RowsBoxElement (GuiElement):
    def __init__(self, x: int, y: int, background: Surface, game_data: GameDataContainer):

        self.game_data = game_data
        self.width = 125
        self.height = 38
        self.pos_x_frame = x
        self.pos_y_frame = y
        self.pos_x_bg = x + 12
        self.pos_y_bg = y + 11
        self.pos_x_label = x + 20
        self.pos_y_label = y - element_outer_height_2 - 2
        self.background_main = background
        self.font = pygame.font.Font("resources/MightyKingdom.ttf", 36)
        # self.font2 = pygame.font.Font("resources/MightyKingdom.ttf", 24)

        #level label
        self.sp_rows_label_inner_surface = pygame.Surface(
            (element_inner_width_2, element_inner_height_2), pygame.SRCALPHA)
        self.sp_rows_label_inner_surface.fill((255, 255, 255, 75))

        self.sp_rows_label_outer_surface = pygame.Surface(
            (element_outer_width_2, element_outer_height_2), pygame.SRCALPHA)

        self.sp_rows_label_text_surface = pygame.Surface((element_inner_width_2, element_inner_height_2),
                                                          pygame.SRCALPHA)

        self.sp_rows_label_text = self.font.render('Rows', antialias=True,
                                                    color=(0, 0, 0))
        self.sp_rows_label_text_surface.blit(self.sp_rows_label_text, (0, 0))
        self.sp_rows_label_inner_surface.blit(self.sp_rows_label_text_surface, (5, 0))
        self.sp_rows_label_outer_surface.blit(self.sp_rows_label_inner_surface, (4, 5))
        self.sp_rows_label_outer_surface.blit(pygame.image.load("resources/elem_frame_small.png"), (0, 0))

        self.background_main.blit(self.sp_rows_label_outer_surface,
                             (self.pos_x_label, self.pos_y_label))

        #rows
        self.sp_rows_outer_surface = pygame.Surface(
            (element_outer_width_3, element_outer_height_3), pygame.SRCALPHA)
        self.sp_rows_text_surface = pygame.Surface(
            (self.width, self.height), pygame.SRCALPHA)
        self.sp_rows_outer_surface.blit(pygame.image.load("resources/score_bar2.png"), (0, 0))
        self.background_main.blit(self.sp_rows_outer_surface, (self.pos_x_frame, self.pos_y_frame))

        self.background = self.background_main.subsurface(Rect(self.pos_x_bg, self.pos_y_bg, self.width, self.height))
        self.sp_rows_inner_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.sp_rows_inner_surface.blit(self.background, (0, 0))

    def update(self, game_data: GameDataContainer):
        self.game_data = game_data
        self.sp_rows = self.game_data.burned_rows_total
        self.sp_rows_text = self.font.render(str(self.sp_rows), antialias=True,
                                              color=(0, 0, 0))
        self.text_offset = -5

    def render(self):
        self.sp_rows_text_surface.fill((0, 0, 0, 0))
        self.sp_rows_text_surface.blit(self.sp_rows_text, (0, self.text_offset))

        self.background_main.blit(self.sp_rows_inner_surface, (self.pos_x_bg, self.pos_y_bg))
        self.background_main.blit(self.sp_rows_text_surface, (self.pos_x_bg, self.pos_y_bg))
