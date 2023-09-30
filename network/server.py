import socket
import pickle
from _thread import start_new_thread
from datetime import datetime

from typing import Optional

from constants import IPV4, PORT, PACKAGE_SIZE
from game import game


def run_server(server: str = IPV4, port: int = PORT, players: int = 2):
    TetrisServer(server, port, players).run()


class TetrisServer:
    def __init__(self, server: str, port: int, players: int = 2):
        self.seed = datetime.now().timestamp()
        self.stand_by: bool = True

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((server, port))
        self.socket.listen(players)
        self.slots = [True] * players
        self.free_slots = players
        self.containers: list[Optional[game.GameDataContainer]] = [None] * players
        print('Waiting for connection, Server Started')

    def run(self):
        while self.stand_by:
            conn, addr = self.socket.accept()
            player_id = None
            for i in range(len(self.slots)):
                if self.slots[i]:
                    player_id = i
                    self.slots[player_id] = False
                    self.free_slots -= 1
                    break

            if player_id is not None:
                start_new_thread(self.threaded_client, (conn, player_id))
                print("Connected to:", addr)
                print(f'Connections: {self.free_slots}')

    def threaded_client(self, conn, player_id: int):
        conn.sendall(pickle.dumps(self.seed))
        reply_index = (1, 0)[player_id]
        while True:
            game_data: GameDataContainer = pickle.loads(conn.recv(PACKAGE_SIZE))

            if not game_data:
                print("Disconnected")
                break
            else:
                if game_data.field is None and self.containers[player_id] is not None:
                    game_data.field = self.containers[player_id].field
                self.containers[player_id] = game_data

                reply = self.containers[reply_index]
                # print('Received: ', data)
                # print('Sending: ', reply)

            conn.sendall(pickle.dumps(reply))

        conn.close()
        self.slots[player_id] = True
        self.free_slots += 1
        print('Lost connection')
        print(f'Connections: {self.free_slots}')


if __name__ == '__main__':
    run_server()
