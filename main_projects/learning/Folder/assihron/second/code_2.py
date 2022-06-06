#!/usr/bin/env python3


# ASINHORONNIY CODE

import socket 
from select import select # monitoring of changings socket
# .fileno() - number of the file


# domain:5000
# server and body

to_monitor = []
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


def accept_connection(server_socket): # getts connection info
  client_socket, addr = server_socket.accept() 
  print("Connection from ", addr)
  to_monitor.append(client_socket)
 
def send_message(client_socket): # sending message
  request = client_socket.recv(4096)
  #print(request)

  if request: # if server got message
    response = 'Hello world\n'.encode()
    client_socket.send(response)  
  else: # if no message then 
    client_socket.close()


def event_loop():
  
  while True:
    # (getting tuple with object) 
    ready_to_read, _, _ = select(to_monitor, [], [] ) # read, write, errors
    # reading free servers for sending message  
    
    for sock in ready_to_read: # READY_TO_READ
      if sock is server_socket: # if server_socket is server then: 
        accept_connection(sock)
      else:
        send_message(sock)
    


if __name__ == '__main__':
  to_monitor.append(server_socket)
  print(to_monitor)
  event_loop()
