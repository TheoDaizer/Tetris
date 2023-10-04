import pygame
from pygame import Rect

from pygame.surface import Surface

from game import GameDataContainer
from game.figure import SHAPES
from game.colors import COLORS
from gui.abc_gui_element import GuiElement
import gui.gui_constants as g_const
import constants as const


class NextFigureElement (GuiElement):

    next_figure_offset = ((2, -2), (20, 15), (-15, 15), (20, 15), (18, 15), (-13, 15), (2, 15))
    block_image = pygame.image.load("resources/tetris_block.png")
    next_figure_frame_image = "resources/elem_frame.png"
    inner_surface_offset = (5, 6)

    def __init__(self, x: int, y: int, background: Surface, game_data: GameDataContainer):
        super().__init__(x, y, background)
        self.width = 132
        self.height = 91
        self.pos_x_bg = x + 8
        self.pos_y_bg = y + 10
        self.next_shape = game_data.next_shape_variant

        self.next_figure_item_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        self.next_figure_inner_surface = pygame.Surface(
            (g_const.element_inner_width_1, g_const.element_inner_height_1), pygame.SRCALPHA)
        self.next_figure_inner_surface.fill((255, 255, 255, 75))

        self.next_figure_outer_surface = pygame.Surface(
            (g_const.element_outer_width_1, g_const.element_outer_height_1), pygame.SRCALPHA)
        self.next_figure_outer_surface.blit(self.next_figure_inner_surface, self.inner_surface_offset)
        self.next_figure_outer_surface.blit(pygame.image.load(self.next_figure_frame_image), (0, 0))

        background.blit(self.next_figure_outer_surface, self.pos_frame)
        self.background = background.subsurface(Rect(self.pos_x_bg, self.pos_y_bg, self.width, self.height))

        self.next_figure_background_surface = pygame.Surface((self.width, self.height))
        self.next_figure_background_surface.blit(self.background, (0, 0))
        self.next_figure_surface = pygame.Surface((self.width, self.height))

    def update(self, game_data: GameDataContainer):

        if game_data.next_shape_variant != self.next_shape:
            self.next_shape = game_data.next_shape_variant
            self.is_changed = True

    def render(self):

        if self.is_changed:
            self.next_figure_item_surface.fill((0, 0, 0, 0))
            self.next_figure_surface.blit(self.next_figure_background_surface, (0, 0))

            for dx, dy in SHAPES[self.next_shape][0]:
                x = 1 + dx
                y = 0 + dy
                self.render_block(self.next_figure_item_surface, (x, y), self.next_shape)

            self.next_figure_surface.blit(self.next_figure_item_surface, self.next_figure_offset[self.next_shape])

            self.is_changed = False
            return self.next_figure_surface

    def render_block(self, surface, position: tuple[int, int], shape_variant: int, x_shift: bool = False):
        x, y = position
        rect = pygame.Rect(x * const.TILESIZE + x_shift, y * const.TILESIZE, const.TILESIZE, const.TILESIZE)
        pygame.draw.rect(surface, COLORS[shape_variant], rect, 0)
        surface.blit(self.block_image, (x * const.TILESIZE + x_shift, y * const.TILESIZE))


class ScoreBoxElement (GuiElement):
    width = 125
    height = 38

    d_bg = (12, 11)
    d_label = (20, g_const.element_outer_height_2 - 2)

    def __init__(self, x: int, y: int, background: Surface, game_data: GameDataContainer):
        super().__init__(x, y, background)
        self.font = pygame.font.Font(self.font_source, 36)
        self.font2 = pygame.font.Font(self.font_source, 24)
        self.score = game_data.score
        self.score_text = self.font.render(str(self.score), antialias=True, color=(0, 0, 0))
        self.text_offset = -5

        # score label
        self.score_label_inner_surface = pygame.Surface(
            (g_const.element_inner_width_2, g_const.element_inner_height_2), pygame.SRCALPHA)
        self.score_label_inner_surface.fill((255, 255, 255, 75))
        self.score_label_outer_surface = pygame.Surface(
            (g_const.element_outer_width_2, g_const.element_outer_height_2), pygame.SRCALPHA)
        self.score_label_text_surface = pygame.Surface((g_const.element_inner_width_2, g_const.element_inner_height_2),
                                                       pygame.SRCALPHA)

        self.score_label_text = self.font.render('Score', antialias=True,
                                                 color=(0, 0, 0))
        self.score_label_text_surface.blit(self.score_label_text, (0, 0))
        self.score_label_inner_surface.blit(self.score_label_text_surface, self.label_text_offset)
        self.score_label_outer_surface.blit(self.score_label_inner_surface, self.label_inner_surface_offset)
        self.score_label_outer_surface.blit(pygame.image.load(self.label_frame_image), (0, 0))

        background.blit(self.score_label_outer_surface, self.pos_label)

        # score
        self.score_outer_surface = pygame.Surface((g_const.element_outer_width_3, g_const.element_outer_height_3))
        self.score_inner_surface = pygame.Surface((self.width, self.height))
        self.score_text_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        self.score_outer_surface.blit(pygame.image.load(self.bar_image), (0, 0))

        background.blit(self.score_outer_surface, self.pos_frame)

        self.score_inner_surface.blit(self.background, (0, 0))

        self.score_surface = pygame.Surface((self.width, self.height))

    def update(self, game_data: GameDataContainer):

        if game_data.score != self.score:
            self.score = game_data.score

            if len(str(self.score)) >= 6:
                self.score_text = self.font2.render(str(self.score), antialias=True, color=(0, 0, 0))
                self.text_offset = 4
            else:
                self.score_text = self.font.render(str(self.score), antialias=True, color=(0, 0, 0))

            self.is_changed = True

    def render(self):

        if self.is_changed:
            self.score_text_surface.fill((0, 0, 0, 0))
            self.score_text_surface.blit(self.score_text, (0, self.text_offset))
            self.score_surface.blit(self.score_inner_surface, (0, 0))
            self.score_surface.blit(self.score_text_surface, (0, 0))

            self.is_changed = False
            return self.score_surface


class LevelBoxElement (GuiElement):

    def __init__(self, x: int, y: int, background: Surface, game_data: GameDataContainer):
        super().__init__(x, y, background)
        self.width = 125
        self.height = 38
        self.pos_x_bg = x + 12
        self.pos_y_bg = y + 11
        self.pos_x_label = x + 20
        self.pos_y_label = y - g_const.element_outer_height_2 - 2
        self.font = pygame.font.Font(self.font_source, 36)
        self.level = game_data.level
        self.level_text = self.font.render(str(self.level), antialias=True, color=(0, 0, 0))
        self.text_offset = - 5

        # level label
        self.level_label_inner_surface = pygame.Surface(
            (g_const.element_inner_width_2, g_const.element_inner_height_2), pygame.SRCALPHA)
        self.level_label_inner_surface.fill((255, 255, 255, 75))

        self.level_label_outer_surface = pygame.Surface(
            (g_const.element_outer_width_2, g_const.element_outer_height_2), pygame.SRCALPHA)

        self.level_label_text_surface = pygame.Surface((g_const.element_inner_width_2, g_const.element_inner_height_2),
                                                       pygame.SRCALPHA)

        self.level_label_text = self.font.render('Level', antialias=True,
                                                 color=(0, 0, 0))
        self.level_label_text_surface.blit(self.level_label_text, (0, 0))
        self.level_label_inner_surface.blit(self.level_label_text_surface, self.label_text_offset)
        self.level_label_outer_surface.blit(self.level_label_inner_surface, self.label_inner_surface_offset)
        self.level_label_outer_surface.blit(pygame.image.load(self.label_frame_image), (0, 0))

        background.blit(self.level_label_outer_surface,(self.pos_x_label, self.pos_y_label))

        # level
        self.level_outer_surface = pygame.Surface((g_const.element_outer_width_3, g_const.element_outer_height_3))
        self.level_inner_surface = pygame.Surface((self.width, self.height))
        self.level_text_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        self.level_outer_surface.blit(pygame.image.load(self.bar_image), (0, 0))

        background.blit(self.level_outer_surface, self.pos_frame)

        self.background = background.subsurface(Rect(self.pos_x_bg, self.pos_y_bg, self.width, self.height))
        self.level_inner_surface.blit(self.background, (0, 0))

        self.level_surface = pygame.Surface((self.width, self.height))

    def update(self, game_data: GameDataContainer):

        if game_data.level != self.level:
            self.level = game_data.level
            self.level_text = self.font.render(str(self.level), antialias=True, color=(0, 0, 0))

            self.is_changed = True

    def render(self):

        if self.is_changed:
            self.level_text_surface.fill((0, 0, 0, 0))
            self.level_text_surface.blit(self.level_text, (0, self.text_offset))

            self.level_surface.blit(self.level_inner_surface, (0, 0))
            self.level_surface.blit(self.level_text_surface, (0, 0))

            self.is_changed = False
            return self.level_surface


class RowsBoxElement (GuiElement):

    def __init__(self, x: int, y: int, background: Surface, game_data: GameDataContainer):

        super().__init__(x, y, background)
        self.width = 125
        self.height = 38
        self.pos_x_bg = x + 12
        self.pos_y_bg = y + 11
        self.pos_x_label = x + 20
        self.pos_y_label = y - g_const.element_outer_height_2 - 2
        self.font = pygame.font.Font(self.font_source, 36)
        self.rows = game_data.burned_rows_total
        self.rows_text = self.font.render(str(self.rows), antialias=True, color=(0, 0, 0))
        self.text_offset = -5

        # level label
        self.rows_label_inner_surface = pygame.Surface((g_const.element_inner_width_2,
                                                        g_const.element_inner_height_2), pygame.SRCALPHA
                                                       )
        self.rows_label_inner_surface.fill((255, 255, 255, 75))

        self.rows_label_outer_surface = pygame.Surface((g_const.element_outer_width_2,
                                                        g_const.element_outer_height_2), pygame.SRCALPHA
                                                       )

        self.rows_label_text_surface = pygame.Surface((g_const.element_inner_width_2, g_const.element_inner_height_2),
                                                      pygame.SRCALPHA
                                                      )

        self.rows_label_text = self.font.render('Rows', antialias=True, color=(0, 0, 0))
        self.rows_label_text_surface.blit(self.rows_label_text, (0, 0))
        self.rows_label_inner_surface.blit(self.rows_label_text_surface, self.label_text_offset)
        self.rows_label_outer_surface.blit(self.rows_label_inner_surface, self.label_inner_surface_offset)
        self.rows_label_outer_surface.blit(pygame.image.load(self.label_frame_image), (0, 0))

        background.blit(self.rows_label_outer_surface,(self.pos_x_label, self.pos_y_label))

        # rows
        self.rows_outer_surface = pygame.Surface((g_const.element_outer_width_3, g_const.element_outer_height_3))
        self.rows_inner_surface = pygame.Surface((self.width, self.height))
        self.rows_text_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        self.rows_outer_surface.blit(pygame.image.load(self.bar_image), (0, 0))

        background.blit(self.rows_outer_surface, self.pos_frame)

        self.background = background.subsurface(Rect(self.pos_x_bg, self.pos_y_bg, self.width, self.height))
        self.rows_inner_surface.blit(self.background, (0, 0))

        self.rows_surface = pygame.Surface((self.width, self.height))

    def update(self, game_data: GameDataContainer):

        if game_data.burned_rows_total != self.rows:
            self.rows = game_data.burned_rows_total
            self.rows_text = self.font.render(str(self.rows), antialias=True, color=(0, 0, 0))

            self.is_changed = True

    def render(self):

        if self.is_changed:
            self.rows_text_surface.fill((0, 0, 0, 0))
            self.rows_text_surface.blit(self.rows_text, (0, self.text_offset))

            self.rows_surface.blit(self.rows_inner_surface, (0, 0))
            self.rows_surface.blit(self.rows_text_surface, (0, 0))

            self.is_changed = False
            return self.rows_surface
