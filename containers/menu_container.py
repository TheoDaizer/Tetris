import pygame
import pygame_gui

from pygame.surface import Surface
from pygame.event import Event

from gui import Buttons, GameMenu
from constants import WINDOWWIDTH, WINDOWHEIGHT
from containers import Container


class MenuContainer(Container):
    def __init__(self, window_surface):
        super().__init__(window_surface)

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

    def event_handler(self, event: Event):
        self.manager.process_events(event)
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            self.menu.process_events(event)

    def update(self, time_delta: float):
        self.manager.update(time_delta)

        if self.menu.is_changed:
            self.fill_background()
            # self.menu_surface.fill("black")
            self.menu.is_changed = False

    def render(self):
        self.manager.draw_ui(self.menu_surface)
        self.window_surface.blit(self.menu_surface, (0, 0))
