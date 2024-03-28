import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_IP = socket.gethostbyname('localhost')
HOST_PORT = 12347
ENCODER = 'utf-8'
BYTE_SIZE = 1024

server_socket.bind((HOST_IP, HOST_PORT))

client_number = 0
all_clients = []

def handle_client(client_socket, client_number):
    while True:
        client_socket.send(f'Hello client #{client_number}, your message has been recieved!'.encode(ENCODER))
        
        message = client_socket.recv(BYTE_SIZE).decode(ENCODER)

        if message == "quit":
            client_socket.send("quit".encode(ENCODER))
            print("\nEnding the chat...goodbye!")
            break
        
        # client_socket.send(f'Hello client #{client_number}, your message has been recieved!'.encode(ENCODER))
        for i in all_clients:
            i.get("socket").send(f'\n Client #{client_number}: {message}\n'.encode(ENCODER))


        # if client_number == 0:
        #     for i in all_clients:
        #         if i.get("number") == 0:
        #             continue
        #         else:
        #             i.get("socket").send(f'Client #{client_number}: {message}'.encode(ENCODER))
        # elif client_number == 1:
        #     for i in all_clients:
        #         if i.get("number") == 1:
        #             continue
        #         else:
        #             i.get("socket").send(f'Client #{client_number}: {message}'.encode(ENCODER))
    client_socket.close()

server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()
    all_clients.append({"socket": client_socket, "number": client_number})
    thread = threading.Thread(target = handle_client, args = (client_socket, client_number))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    client_number += 1