from abc import ABC, abstractmethod
from typing import Optional
from pygame_gui.ui_manager import UIManager
from pygame.event import Event

from gui import Buttons


class Menu(ABC):
    def __init__(self, manager: UIManager, buttons: Optional[Buttons] = None):
        self.manager = manager
        self.buttons = Buttons(self.manager) if buttons is None else buttons

        self._new_container = None

    @property
    def new_container(self):
        return self._new_container

    @abstractmethod
    def process_events(self, event: Event):
        pass
