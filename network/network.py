import socket
import pickle

from constants import IPV4, PORT, PACKAGE_SIZE

from game import GameDataContainer


class Network:
    def __init__(self, server: str = IPV4, port: int = PORT):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.connect = self.connect()

    def get_seed(self) -> float:
        return self.connect

    def connect(self):
        try:
            self.client.connect((self.server, self.port))
            return pickle.loads(self.client.recv(PACKAGE_SIZE))

        # TODO эескпт без типа ошибки - шляпа
        except:
            pass

    def send(self, data: GameDataContainer) -> GameDataContainer:
        self.client.send(pickle.dumps(data))
        return pickle.loads(self.client.recv(PACKAGE_SIZE))
