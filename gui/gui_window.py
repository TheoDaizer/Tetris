from abc import ABC

from pygame import Surface, Rect


class GuiWindow():
    def __init__(self, width: int, height: int, x: int, y: int, background: Surface):
        self.width = width
        self.height = height

        self.background: Surface = self._prepare_background(x, y, background)

    def _prepare_background(self, x: int, y: int, background: Surface) -> Surface:
        background = background.subsurface(Rect(x, y, self.width, self.height))

        alpha_white = Surface((self.width, self.height)).convert_alpha()
        alpha_white.fill((255, 255, 255, 75))

        background.blit(alpha_white, (0, 0))
        return background


