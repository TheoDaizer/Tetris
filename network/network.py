import socket
import pickle
from game import Game, GameDataContainer
from constants import IPV4


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = IPV4
        self.port = 5555
        self.addr = (self.server, self.port)
        self.game = self.connect()

    def get_game(self) -> Game:
        return self.game

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(1024 * 8))

        # TODO эескпт без типа ошибки - шляпа
        except:
            pass

    def send(self, data: GameDataContainer) -> GameDataContainer:
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(1024))
        except socket.error as e:
            print(e)
