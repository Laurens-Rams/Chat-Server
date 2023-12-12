import socket

socket_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 80
server_address = '93.184.216.34'

socket_one.connect((server_address, port))
request = "GET / HTTP/1.1\nHost: example.com\n\n"

socket_one.send(request.encode())

buffer_size = 4096
result = socket_one.recv(buffer_size)

print(result.decode())