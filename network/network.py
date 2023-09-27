import socket
import pickle

from constants import IPV4

from game import GameDataContainer


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = IPV4
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect = self.connect()

    def get_seed(self) -> float:
        return self.connect

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(1024))

        # TODO эескпт без типа ошибки - шляпа
        except:
            pass

    def send(self, data: GameDataContainer) -> GameDataContainer:
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)
