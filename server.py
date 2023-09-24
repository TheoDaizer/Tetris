import socket
from _thread import start_new_thread
import pickle

from constants import IPV4
from datetime import datetime

server = IPV4
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print('Waiting for connection, Server Started')

containers = [None, None]
currentPlayer = 0
seed = datetime.now().timestamp()


def threaded_client(conn, player):

    conn.sendall(pickle.dumps(seed))
    reply_index = (1, 0)[player]
    while True:
        try:
            data = pickle.loads(conn.recv(4096))

            if not data:
                print("Disconnected")
                break
            else:
                containers[player] = data
                reply = containers[reply_index]
                # print('Received: ', data)
                # print('Sending: ', reply)

            conn.sendall(pickle.dumps(reply))

        # TODO эескпт без типа ошибки - шляпа
        except:
            break

    conn.close()
    global currentPlayer
    currentPlayer -= 1
    print('Lost connection')
    print(f'Connections: {currentPlayer}')


while True:
    conn, addr = s.accept()

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    print("Connected to:", addr)
    print(f'Connections: {currentPlayer}')
