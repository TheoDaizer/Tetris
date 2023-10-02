from abc import ABC

from pygame import Surface, Rect


class GuiElement(ABC):
    def __init__(self, x: int, y: int, background: Surface):
        self.x = x
        self.y = y
        self.background_main = background
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

    def update(self):
        pass

    def render(self):
        pass

