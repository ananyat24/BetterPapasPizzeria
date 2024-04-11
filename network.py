import socket
from constants import Constants
import json

c = Constants()

class Network():
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname('localhost')
        self.id = c.HOST_IP
        self.port = c.HOST_PORT
        self.encoder = c.ENCODER   
        self.role = None

        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def connect(self):
        try:
            self.client_socket.connect((self.server, self.port))
            # self.role = self.client_socket.recv(1024).decode(self.encoder)
            # print(self.role)
            # recieved_data =  self.client_socket.recv(1024).decode(self.encoder)
            # return json.loads(recieved_data)
        except:
            pass

    def send(self, data_to_send):
        try:
            formated_data = json.dumps(data_to_send)
            self.client_socket.send(formated_data.encode(self.encoder))
            
            recieved_data =  self.client_socket.recv(1024).decode(self.encoder)
            return json.loads(recieved_data)
        except socket.error as e:
            print(e)
    
    def get_role(self):
        return self.role
    
            
