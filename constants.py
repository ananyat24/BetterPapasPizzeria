# store all constants used across multiple files here
import socket

# also store variables that are changed throughout code but needed in multiple files here

import os
import json
import socket
# also store variables that are changed throughout code but needed in multiple files here

import os
import json
<<<<<<< HEAD
import socket
=======
>>>>>>> af33859 (send ticket values to library to share with another player. fix #27)

class Constants():
    def __init__(self):
        self.screen_height = 765
        self.screen_width = 1350
        self.HOST_IP = socket.gethostbyname('localhost') #replace 'localhost' with socket.gethostname() for other laptops
        self.HOST_PORT = 12345
        self.ENCODER = 'utf-8'
<<<<<<< HEAD
        self.background_image = None

        self.playerNumber = 1

        self.HOST_IP = socket.gethostbyname('localhost') #replace 'localhost' with socket.gethostname() for other laptops
        self.HOST_PORT = 12345
        self.ENCODER = 'utf-8'
        
        self.pizza_image = None # image for whole pizza
        self.pizza_image_location = () # location for pizza in the form (x_pos, y_pos)
        self.lines = [] # lines for cut pizza
        self.topping_boxes = [] # list of tuples in the form (image, location) for all topping containers
<<<<<<< HEAD
=======

>>>>>>> af33859 (send ticket values to library to share with another player. fix #27)
        self.VALUES_JSON = {}
        self.VALUES = {}
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "values.json")) as f:
            self.VALUES_JSON = json.load(f)

    def ticketLoad(self):
        self.VALUES = self.VALUES_JSON.copy()

<<<<<<< HEAD
        return self.VALUES


    def ticketSave(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "values.json"), "w") as f:
            json.dump(self.VALUES_JSON, f)
=======
        
>>>>>>> ec6bec4 (Succesfully implemented socket and threading test)
=======
    def ticketSave(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "values.json"), "w") as f:
            json.dump(self.VALUES_JSON, f)
>>>>>>> af33859 (send ticket values to library to share with another player. fix #27)
