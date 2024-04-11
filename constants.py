# store all constants used across multiple files here
# also store variables that are changed throughout code but needed in multiple files here

class Constants():
    
    def __init__(self):
        self.screen_height = 600
        self.screen_width = 1000
        self.background_image = None
        
        self.pizza_image = None # image for whole pizza
        self.pizza_image_location = () # location for pizza in the form (x_pos, y_pos)
        self.lines = [] # lines for cut pizza
        self.topping_boxes = [] # list of tuples in the form (image, location) for all topping containers
        