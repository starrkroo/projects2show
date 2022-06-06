#!/usr/bin/env python3
import socket
from select import select
from os import listdir

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # config
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# sock.bind((socket.gethostname(), 5000))
# print('{}:{}'.format(socket.gethostname(), 5000))
# sock.listen()

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # config
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind((socket.gethostname(), 5004))
    print('{} {}'.format(socket.gethostname(), 5004))
    sock.listen()
    to_monitor = []

    def accept_connection(server_socket):
        data, __ = server_socket.accept()
        to_monitor.append(data)

    def send_message(client_socket):
        can = True
        while can:
            request = client_socket.recv(4096)
            try:
                item = request.decode()
            except:
                print('returns')
                return 'fucked'
            if len(request):
                can = False
            print(item)
        #item = request.decode()

    def event_loop():
        while True:
            try:
                ready_to_read, _, _, = select(to_monitor, [], [])
            except ValueError:
                break

            for item in ready_to_read:
                if item is sock:
                    accept_connection(item)
                else:
                    if send_message(item) == 'fucked':  print('yes'); break

            break

    if __name__ == '__main__':
        to_monitor.append(sock)
        event_loop()

    continue

