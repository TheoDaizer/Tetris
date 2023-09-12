from abc import ABC, abstractmethod
from pygame.surface import Surface
from pygame.event import Event


class Container(ABC):

    def __init__(self, window_surface: Surface):
        self.window_surface = window_surface

    @abstractmethod
    def event_handler(self, event: Event):
        pass

    @abstractmethod
    def update(self, time_delta: float):
        pass

    @abstractmethod
    def render(self):
        pass
