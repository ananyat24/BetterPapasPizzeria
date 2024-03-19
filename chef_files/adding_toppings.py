import pygame
from chef_files.chef import Chef
from constants import Constants
from chef_files.topping import Topping

class AddingToppings(Chef):
    
    def __init__(self, screen:pygame.display):
        self.c = Constants() # get the constants        
        
        toppings_board_img = pygame.image.load("ADD HERE")
        toppings_board_image = pygame.transform.scale(toppings_board_img, (self.c.screen_width, self.c.screen_height))
        
        super().__init__(screen, toppings_board_image)
        
        # create each topping as a separate object
        olives = Topping() # ADD ALL THE PARAMETERS HERE
        self.topping_boxes.append(olives.get_image_location())
    
    # add a topping