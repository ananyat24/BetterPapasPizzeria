import pygame
from chef_files.chef import Chef
from constants import Constants

class SatisfactionScore(Chef):
    
    def __init__(self):
        self.background_image = None
        self.pizza_image_location = (int(self.c.screen_width/2), 120)
        
        
    def bg_to_complete_pizza(self):
        self.background_image = self.change_background("background images/kitchen backgrounds/Kitchen - Complete Pizza BG.png")
        self.pizza_fly_in()
    
    
    # have the pizza fly in before the cutting process starts
    def pizza_fly_in(self):
        self.c.pizza_image_location = self.pizza_image_location
        final_x_coor = self.c.pizza_image_location[0]
        for x_coor in range(0, final_x_coor, 20):
            self.screen.blit(self.c.background_image, (0, 0))
            self.screen.blit(self.c.pizza_image, (x_coor, self.c.pizza_image_location[1]))
            pygame.display.update()
        self.screen.blit(self.c.background_image, (0, 0))
        self.screen.blit(self.c.pizza_image, (final_x_coor, self.c.pizza_image_location[1]))
        self.display_current_pizza()
    
    