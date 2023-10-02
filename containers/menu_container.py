import pygame
import pygame_gui

from pygame.surface import Surface
from pygame.event import Event

from gui import MainMenu
from constants import WINDOWWIDTH, WINDOWHEIGHT, BACKGROUND
from containers import Container


class MenuContainer(Container):
    def __init__(self, window_surface):
        super().__init__(window_surface)

        self.menu_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.fill_background()

        self.manager = pygame_gui.UIManager((WINDOWWIDTH, WINDOWHEIGHT))

        self.menu = MainMenu(self.manager)

    @property
    def status(self):
        return self.menu.new_container

    def fill_background(self):
        self.menu_surface.blit(pygame.image.load(BACKGROUND), (0, 0))

    def event_handler(self, event: Event):
        self.manager.process_events(event)
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            new_menu = self.menu.process_events(event)

            if new_menu is not self.menu:
                self.fill_background()
                self.menu = new_menu

    def update(self, time_delta: float):
        self.manager.update(time_delta)

    def render(self):
        self.manager.draw_ui(self.menu_surface)
        self.window_surface.blit(self.menu_surface, (0, 0))
