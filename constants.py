# store all constants used across multiple files here
import socket

# also store variables that are changed throughout code but needed in multiple files here

import os
import json
import socket
# also store variables that are changed throughout code but needed in multiple files here

import os
import json

class Constants():
    def __init__(self):
        self.screen_height = 765
        self.screen_width = 1350
        self.HOST_IP = socket.gethostbyname('localhost') #replace 'localhost' with socket.gethostname() for other laptops
        self.HOST_PORT = 12345
        self.ENCODER = 'utf-8'
        self.background_image = None

        self.playerNumber = 1
        
        self.angles = []
        
        self.pizza_image = None # image for whole pizza
        self.pizza_image_location = () # location for pizza in the form (x_pos, y_pos)
        self.lines = [] # lines for cut pizza
        self.topping_boxes = [] # list of tuples in the form (image, location) for all topping containers
        self.toppings = [] # list of all toppings on the pizza
        
        # background images for each chef screen
        self.chef_cutting_bg = None
        self.chef_topping_bg = None
        self.chef_oven_bg = None
        
        self.curr_screen_name = None
        
        # store the differences in pizza locations for each chef screen
        self.toppings_to_cutting = (430 - 295, 120 - 120)
        self.toppings_to_oven = (330 - 295, 140 - 120)
        self.cutting_to_toppings = (295 - 430, 120 - 120)
        self.cutting_to_oven = (330 - 430, 140 - 120)
        
        # storing order ticket information
        self.VALUES_JSON = {}
        self.VALUES = {}
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "values.json")) as f:
            self.VALUES_JSON = json.load(f)

    def ticketLoad(self):
        self.VALUES = self.VALUES_JSON.copy()

        return self.VALUES


    def ticketSave(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "values.json"), "w") as f:
            json.dump(self.VALUES_JSON, f)

    def ticketSave(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "values.json"), "w") as f:
            json.dump(self.VALUES_JSON, f)
