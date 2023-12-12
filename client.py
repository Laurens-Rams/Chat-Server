import socket

def send_message(sckt, message):
    sckt.send(message.encode())

def receive_message(sckt):
    return sckt.recv(4096).decode()

socket_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 33123
server_address = '127.0.0.1'

socket_one.connect((server_address, port))
print("Connected to server.")

client_name = input("Enter your name (client): ")
send_message(socket_one, client_name)
server_name = receive_message(socket_one)

while True:
    client_message = input("Input message: ")
    send_message(socket_one, client_message)

    # Check if the client wants to exit the chat
    if client_message.lower() == "exit":
        print("Client finished")
        break

    server_response = receive_message(socket_one)
    print(f"{server_name}: {server_response}")

socket_one.close()
