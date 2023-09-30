import pygame
from pygame import Rect
import pygame_gui

from pygame_gui.ui_manager import UIManager
from pygame.surface import Surface

from game import GameDataContainer, GameFieldRenderer
from gui.abc_gui_element import GuiElement
from .ui_constants import *
from constants import *
from pygame.event import Event
from game.point import Point


class NextFigureElement (GuiElement):
    next_figure_coordinates = ((438, 171), (455, 191), (421, 191), (455, 191), (451, 191), (421, 191), (438, 191))

    def __init__(self, width: int, height: int, x: int, y: int, background: Surface, game_data: GameDataContainer):

        self.renderer = GameFieldRenderer()
        self.game_data = game_data
        self.width = width
        self.height = height
        self.pos_x = x
        self.pos_y = y
        self.background_main = background

        self.sp_next_figure_item_surface = pygame.Surface(
            (self.width, self.height))
        self.sp_next_figure_item_surface = self.sp_next_figure_item_surface.convert_alpha()
        self.sp_next_figure_item_surface.fill((0, 0, 0, 0))

        self.sp_next_figure_inner_surface = pygame.Surface(
            (element_inner_width_1, element_inner_height_1))
        self.sp_next_figure_inner_surface = self.sp_next_figure_inner_surface.convert_alpha()
        self.sp_next_figure_inner_surface.fill((255, 255, 255, 75))
        # self.sp_next_figure_inner_surface.fill((0, 0, 0, 0))

        self.sp_next_figure_outer_surface = pygame.Surface(
            (element_outer_width_1, element_outer_height_1))
        self.sp_next_figure_outer_surface = self.sp_next_figure_outer_surface.convert_alpha()
        self.sp_next_figure_outer_surface.fill((0, 0, 0, 0))
        self.sp_next_figure_outer_surface.blit(self.sp_next_figure_inner_surface, (5, 6))
        self.sp_next_figure_outer_surface.blit(pygame.image.load("resources/elem_frame.png"), (0, 0))

        # self.background2 = pygame.Surface ((WINDOWWIDTH, WINDOWHEIGHT))
        # self.background2.blit(background, (0, 0))
        # self.background2.blit (self.sp_next_figure_outer_surface, (x - 9, y - 10))
        self.background_main.blit(self.sp_next_figure_outer_surface, (x - 9, y - 10))

        self.background = background.subsurface(Rect(x, y, self.width, self.height))

        self.sp_next_figure_test_surface = pygame.Surface(
            (self.width, self.height))
        self.sp_next_figure_test_surface = self.sp_next_figure_test_surface.convert_alpha()
        self.sp_next_figure_test_surface.fill((0, 0, 0, 0))
        self.sp_next_figure_test_surface.blit(self.background, (0, 0))

    # def _prepare_background(self, x: int, y: int, background: Surface) -> Surface:
    #     self.background = background.subsurface(Rect(x, y, self.width, self.height))
    #     return self.background

    def update(self, game_data):
        self.game_data = game_data
        self.next_shape = self.game_data.next_shape_variant
        self.coordinates = self.next_figure_coordinates[self.game_data.next_shape_variant]
        print(self.next_shape)
        print(self.coordinates)


    def render (self):
        self.sp_next_figure_item_surface.fill((0, 0, 0, 0))
        self.renderer.render_figure(self.sp_next_figure_item_surface, Point(1, 0),
                                    self.next_shape, 0)

        self.background_main.blit(self.sp_next_figure_test_surface, (self.pos_x, self.pos_y))

        self.background_main.blit(self.sp_next_figure_item_surface, self.coordinates)

        # self.background_main.blit(self.sp_next_figure_outer_surface, (self.pos_x, self.pos_y))




