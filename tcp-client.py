import socket

server_ip = 'localhost'
server_port = 3535

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((server_ip, server_port))
my_socket.send("Am i connected?".encode())

message = my_socket.recv(1000)
print(message.decode())

my_socket.close()
