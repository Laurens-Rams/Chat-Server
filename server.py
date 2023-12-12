import socket

def send_message(sckt, message):
    sckt.send(message.encode())

def receive_message(sckt):
    return sckt.recv(4096).decode()

socket_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 33123
socket_one.bind(("0.0.0.0", port))
socket_one.listen(1)

print("Waiting for a connection...")

while True:
    connected_socket, addr = socket_one.accept()
    print(f"Client {addr[0]} connected")

    server_name = input("Enter your name (server): ")

    client_name = receive_message(connected_socket)
    send_message(connected_socket, server_name)

    while True:
        client_message = receive_message(connected_socket)
        print(f"{client_name}: {client_message}")

        # Check if the client wants to exit the chat
        if client_message.lower() == "exit":
            print("Server finished")
            connected_socket.close()
            break

        server_message = input("Input message: ")
        send_message(connected_socket, server_message)

        if server_message.lower() == "exit":
            connected_socket.close()
            break

socket_one.close()
