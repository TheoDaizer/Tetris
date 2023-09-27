import socket
from _thread import start_new_thread
import pickle
from typing import Optional

from constants import IPV4
from datetime import datetime

from game.game import GameDataContainer

server = IPV4
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print('Waiting for connection, Server Started')

containers: list[Optional[GameDataContainer]] = [None, None]
free_slot = [True, True]
seed = datetime.now().timestamp()


def threaded_client(conn, player_id: int):

    conn.sendall(pickle.dumps(seed))
    reply_index = (1, 0)[player_id]
    while True:
        try:
            game_data: GameDataContainer = pickle.loads(conn.recv(4096))

            if not game_data:
                print("Disconnected")
                break
            else:
                if game_data.field is None and containers[player_id] is not None:
                    game_data.field = containers[player_id].field
                containers[player_id] = game_data

                reply = containers[reply_index]
                # print('Received: ', data)
                # print('Sending: ', reply)

            conn.sendall(pickle.dumps(reply))

        # TODO эескпт без типа ошибки - шляпа
        except:
            break

    conn.close()
    global free_slot
    free_slot[player_id] = True
    print('Lost connection')
    print(f'Connections: {free_slot.count(False)}')


while True:
    conn, addr = s.accept()

    for i in range(2):
        if free_slot[i]:
            player_id = i
            free_slot[player_id] = False
            break

    start_new_thread(threaded_client, (conn, player_id))
    print("Connected to:", addr)
    print(f'Connections: {free_slot.count(False)}')

