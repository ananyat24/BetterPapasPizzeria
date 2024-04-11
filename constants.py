# store all constants used across multiple files here
import socket

class Constants():
    
    def __init__(self):
        self.screen_height = 765
        self.screen_width = 1350
        self.HOST_IP = socket.gethostbyname('localhost') #replace 'localhost' with socket.gethostname() for other laptops
        self.HOST_PORT = 12345
        self.ENCODER = 'utf-8'
        