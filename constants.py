# store all constants used across multiple files here
# also store variables that are changed throughout code but needed in multiple files here

import os
import json

class Constants():
    def __init__(self):
        self.screen_height = 600
        self.screen_width = 1000
        self.background_image = None

        self.playerNumber = 1
        
        self.pizza_image = None # image for whole pizza
        self.pizza_image_location = () # location for pizza in the form (x_pos, y_pos)
        self.lines = [] # lines for cut pizza
        self.topping_boxes = [] # list of tuples in the form (image, location) for all topping containers

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
