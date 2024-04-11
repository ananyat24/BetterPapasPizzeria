import pygame
from chef_files.chef import Chef
from constants import Constants
from chef_files.topping import Topping

class AddingToppings(Chef):
    
    def __init__(self, screen:pygame.display, c:Constants):
        self.c = c
        self.pizza_image_location = (295, 65)
        self.background_image = None
        super().__init__(screen, self.c)
        
        # create each topping as a separate object
        #artichoke = Topping("pictures/single_ingredients/artichoke.png", location:tuple, width:int, height:int, screen)
        #self.topping_boxes.append(artichoke.one_topping_image, artichoke.location)
        """
        ^ steps needed:
        1. create each topping as a separate object
        2. change all location, width, and height parameters to their proper values
        3. figure out how to get the topping image to follow the cursor
        4. using colliderect and mouse clicks, determine when to pick up and drop toppings
        5. add a done button that allows user to move to next stage (technically baking the pizza but cutting the pizza for now) - there might be a button on the screen already just need to add the code
        """

        
    # switch the background to the toppings board
    def bg_to_toppings_board(self):
        self.background_image = self.change_background("background images/kitchen backgrounds/Kitchen - Ingredients BG.png")
        
    
    # have the pizza fly in initially
    def pizza_fly_in(self):
        self.c.pizza_image_location = self.pizza_image_location
        final_y_coor = self.c.pizza_image_location[1]
        for y_coor in range(0, final_y_coor, 20):
            self.screen.blit(self.c.background_image, (0, 0))
            self.screen.blit(self.c.pizza_image, (self.c.pizza_image_location[0], y_coor))
            pygame.display.update()
        self.screen.blit(self.c.background_image, (0, 0))
        self.screen.blit(self.c.pizza_image, (self.c.pizza_image_location[0], final_y_coor))
        