import pygame
import pygame_gui
from pygame.surface import Surface

from gui import Buttons, GameMenu
from constants import WINDOWWIDTH, WINDOWHEIGHT
from containers import Container


class MenuContainer(Container):
    def __init__(self):
        self.menu_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.fill_background()

        self.manager = pygame_gui.UIManager((WINDOWWIDTH, WINDOWHEIGHT))
        self.buttons = Buttons(self.manager)

        self.menu = GameMenu(self.manager, self.buttons)

    @property
    def new_container(self):
        return self.menu.window_container

    def fill_background(self):
        self.menu_surface.blit(pygame.image.load("resources/background2.jpg"), (0, 0))

    def update(self, time_delta: float):
        self.menu.process_events()
        self.manager.update(time_delta)

        if self.menu.is_changed:
            self.fill_background()
            # self.menu_surface.fill("black")
            self.menu.is_changed = False

    def render(self, window_surface: Surface):
        self.manager.draw_ui(self.menu_surface)
        window_surface.blit(self.menu_surface, (0, 0))
