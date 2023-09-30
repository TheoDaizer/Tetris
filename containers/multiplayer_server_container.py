from pygame import Surface

from _thread import start_new_thread
from network.server import run_server

from .multiplayer_client_container import ClientContainer


class ServerContainer(ClientContainer):
    def __init__(self, window_surface: Surface):
        start_new_thread(run_server, tuple())
        super().__init__(window_surface)
