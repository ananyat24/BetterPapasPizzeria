import socket

class Network:
    def __init__ (self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname('localhost')
        self.port = 12347
        self.encoder = "utf-8"

    def connect(self):
        try:
            self.client.connect((self.server, self.port))
            return self.client.recv(1024).decode(self.encoder)
        except:
            pass

    def send(self, data):
        try:
            self.client.send(data.encode(self.encoder))
            return self.client.recv(1024).decode(self.encoder)
        except socket.error as e:
            print(e)
            
