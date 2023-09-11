import socket
from _thread import start_new_thread
import pickle

from game import Game
from constants import IPV4

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


def threaded_client(conn, player):
    conn.sendall(pickle.dumps(Game()))

    while True:
        try:
            data = pickle.loads(conn.recv(1024))
            containers[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 0:
                    reply = containers[1]
                else:
                    reply = containers[0]
                print('Received: ', data)
                print('Sending: ', reply)

            conn.sendall(pickle.dumps(reply))
        # TODO эескпт без типа ошибки - шляпа
        except:
            break

    print('Lost connection')
    conn.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
