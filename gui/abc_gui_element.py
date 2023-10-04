from abc import ABC, abstractmethod

from pygame import Surface, Rect
from game import GameDataContainer
from gui.gui_constants import font_source


class GuiElement(ABC):
    font_source = font_source
    label_frame_image = "resources/elem_frame_small.png"
    bar_image = "resources/score_bar2.png"
    label_inner_surface_offset = (4, 5)
    label_text_offset = (5, 0)

    # Individual for child class
    width = 125
    height = 38

    d_bg: tuple[int, int] = (0, 0)
    d_label: tuple[int, int] = (0, 0)

    def __init__(self, x: int, y: int, background: Surface):
        self.pos_frame = (x, y)
        self.pos_bg = (x + self.d_bg[0], x + self.d_bg[1])
        self.pos_label = (x + self.d_label[0], x + self.d_label[1])

        self.background = self._create_background(background)
        self.is_changed = True

    def _create_background(self, background: Surface) -> Surface:
        return background.subsurface(
            Rect(*self.pos_bg, self.width, self.height)
        )

    @abstractmethod
    def update(self, game_data: GameDataContainer):
        pass

    @abstractmethod
    def render(self):
        pass

