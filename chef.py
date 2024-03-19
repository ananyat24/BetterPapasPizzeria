import pygame

class Chef:
    
    def __init__(self, screen:pygame.display, background:pygame.image):
        self.screen = screen
        
        self.pizza_image = None # image for whole pizza
        self.pizza_image_location = () # location for pizza in the form (x_pos, y_pos)
        
        self.lines = [] # lines for cut pizza
        
        self.background_image = background
        
        self.topping_boxes = [] # list of tuples in the form (image, location) for all topping containers
    
    
    # show the current pizza (needed for erasing cutting line)
    def display_current_pizza(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.pizza_image, (self.pizza_image_location[0], self.pizza_image_location[1]))
        for line in self.lines:
            pygame.draw.line(line[0], line[1], line[2], line[3], line[4])
        for tb in self.topping_boxes:
            self.screen.blit(tb[0], tb[1])
            
            
    # add new images to the screen
    def add_pizza_image(self, image, location:tuple): # locations is a list of tuples in the form (x_pos, y_pos)
        self.pizza_image = image
        self.pizza_image_location = location
            