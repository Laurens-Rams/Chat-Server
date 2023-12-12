import socket
from random import random, randint

socket_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8080

socket_one.bind(("0.0.0.0", port))
socket_one.listen(1)

while True:
    connected_socket, addr = socket_one.accept()
    print("Connection from: " + str(addr))

    received_data = connected_socket.recv(4096)
    print(received_data.decode())

    random_number = randint(0, 1000000)

    connected_socket.send(f"HTTP/1.1 200 OK\n\n<html><b>Hi from the best web server ever! Num {random_number}</b></html>\n\n".encode())
    connected_socket.close()

    if "stop" in received_data.decode():
        break

socket_one.close()




