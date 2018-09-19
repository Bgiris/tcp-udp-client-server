import socket
import time
import datetime
import threading


def time_stamp():
    print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))


def handle_client(client_socket):
    client_socket.send("You are connected\n".encode())
    message = client_socket.recv(1024)
    print("Client says: %s" % message.decode())
    client_socket.close()


bind_ip = 'localhost'
bind_port = 3535

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))

time_stamp()
print("Server has started", bind_ip, bind_port)

server.listen(5)
''' socket.listen(backlog)
Listen for connections made to the socket.
The backlog argument specifies the maximum number of queued connections 
and should be at least 1; the maximum value is system-dependent (usually 5).
(SO) - https://stackoverflow.com/a/2444483
'''

while True:
    client, (client_ip, client_port) = server.accept()

    time_stamp()
    print("Client connected: %s:%d" % (client_ip, client_port))

    clientHandler = threading.Thread(target=handle_client, args=(client,))
    clientHandler.start()
