import datetime
import socket
import time


def time_stamp():
    print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))


bind_ip = 'localhost'
bind_port = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((bind_ip, bind_port))

time_stamp()
print("Server has started", bind_ip, bind_port)

while True:
    (message, (client_ip, client_port)) = server.recvfrom(1000)

    time_stamp()
    print("Client connected: %s:%d" % (client_ip, client_port))
    print("Client says: %s" % message.decode())

    server_message = 'Welcome\n'
    server.sendto(server_message.encode(), (client_ip, client_port))

server.close()
