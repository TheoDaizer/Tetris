import socket
import pickle
from typing import Optional
from game import Game
from constants import IPV4


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = IPV4
        self.port = 5555
        self.addr = (self.server, self.port)
        self.game = self.connect()

    def get_game(self):
        return self.game

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(4096))

        # TODO эескпт без типа ошибки - шляпа
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(1024))
        except socket.error as e:
            print(e)


class NetworkContainer:
    def __init__(self, game: Game):
        self.figure = game.figure.shape_position
        self.figure_shadow = game.figure.shadow_shape_position
        self.figure_color = game.figure.color
        self.field = None
        if game.field_updated:
            self.field_updated = False
            self.field = game.field.nodes
