#!/usr/bin/env python3



def server():
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server_socket.bind(('localhost', 5000))
  server_socket.listen()

  while True:
    client_socket, addr = server_socket.accept() # read
    print("Connection from ", addr)
    cliend(client_socket)

 
def client():
  while True:
    request = client_socket.recv(4096) # read

    if not request:
      break
    else:
      response = 'Hello world\n'.encode() # - coding string into bytes
      client_socket.send(response)  # write

  client_socket.close()


server()
