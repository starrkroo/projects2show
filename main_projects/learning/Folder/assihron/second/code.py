#!/usr/bin/env python3


# SINHORONNIY CODE

import socket 

# domain:5000
# server and body

# 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen() # ---> 1


def accept_connection(server_socket): # ---> 3
  while True:
    #print("Before .accept()")
    client_socket, addr = server_socket.accept() 
    print("Connection from ", addr)
    send_message(client_socket) # ---> 4

def send_message(client_socket): # ---> 5
  while True:
    #print('Before .recv()')
    request = client_socket.recv(4096)
    print(request)

    if not request:
      break
    else:
      response = 'Hello world\n'.encode() # - coding string into bytes
      client_socket.send(response)  

  client_socket.close()

if __name__ == '__main__':
  accept_connection(server_socket) # ---> 2
