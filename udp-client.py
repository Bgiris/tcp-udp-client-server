import socket

server_ip = 'localhost'
server_port = 5050

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.sendto("Am i connected?".encode(), (server_ip, server_port))

message = my_socket.recv(1000)
print(message.decode())

my_socket.close()
