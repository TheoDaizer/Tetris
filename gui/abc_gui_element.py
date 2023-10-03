from abc import ABC

from pygame import Surface
from game import GameDataContainer
from gui.gui_constants import font_source

class GuiElement(ABC):
    font_source = font_source
    label_frame_image = "resources/elem_frame_small.png"
    bar_image = "resources/score_bar2.png"
    label_inner_surface_offset = (4, 5)
    label_text_offset = (5, 0)
    def __init__(self, x: int, y: int, background: Surface):
        self.pos_x_frame = x
        self.pos_y_frame = y
        self.background_main = background
        self.is_changed = True
        # self.width = width
        # self.height = height

    #     self.background: Surface = self._prepare_background(x, y, background)
    #
    # def _prepare_background(self, x: int, y: int, background: Surface) -> Surface:
    #     background = background.subsurface(Rect(x, y, self.width, self.height))
    #
    #     # alpha_white = Surface((self.width, self.height)).convert_alpha()
    #     # alpha_white.fill((255, 255, 255, 75))
    #
    #     # background.blit(alpha_white, (0, 0))
    #     return background

    def update(self, game_data: GameDataContainer):
        pass

    def render(self):
        pass

