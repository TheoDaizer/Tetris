import pygame_gui
from pygame.surface import Surface

from gui import Buttons, GameMenu
from constants import WINDOWWIDTH, WINDOWHEIGHT
from containers import Container


class MenuContainer(Container):
    def __init__(self):
        self.menu_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))

        self.manager = pygame_gui.UIManager((WINDOWWIDTH, WINDOWHEIGHT))
        self.buttons = Buttons(self.manager)

        self.menu = GameMenu(self.manager, self.buttons)

    @property
    def new_container(self):
        return self.menu.window_container

    def update(self, time_delta: float):
        self.menu.process_events()
        self.manager.update(time_delta)

        if self.menu.is_changed:
            self.menu_surface.fill("black")
            self.menu.is_changed = False

        self.manager.draw_ui(self.menu_surface)

    def render(self) -> Surface:
        return self.menu_surface
