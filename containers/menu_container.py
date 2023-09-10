import pygame_gui
from pygame.surface import Surface

from gui import Buttons, MainMenu
from constants import WINDOWWIDTH, WINDOWHEIGHT
from containers import Container


class MenuContainer(Container):
    def __init__(self):
        self.menu_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))

        self.manager = pygame_gui.UIManager((WINDOWWIDTH, WINDOWHEIGHT))
        self.buttons = Buttons(self.manager)

        self.active_interface = MainMenu(self.manager, self.buttons)

    def update(self, time_delta: float):
        self.active_interface.process_events()
        self.active_interface = self.active_interface.interface

        self.manager.update(time_delta)

        self.menu_surface.fill("black")
        self.manager.draw_ui(self.menu_surface)

    def render(self) -> Surface:
        return self.menu_surface
