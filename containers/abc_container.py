from abc import ABC, abstractmethod
from pygame.surface import Surface


class Container(ABC):
    @abstractmethod
    def update(self, time_delta: float):
        pass

    @abstractmethod
    def render(self) -> Surface:
        pass
