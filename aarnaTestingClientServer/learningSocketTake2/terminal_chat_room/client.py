import socket, threading

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind((DEST_IP, DEST_PORT))

def send_message():
    pass

def recieve_message():
    pass