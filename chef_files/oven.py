import pygame
from chef_files.chef import Chef
from constants import Constants

class Oven(Chef):
    
    def __init__(self, screen:pygame.display, c:Constants):
        
        self.cooking_time = 0  # stores how long the player cooks the pizza for (used for calculating satsifaction at end)
        self.background_image = None
        
        super().__init__(screen, self.c)
        
    # switch the background to the oven
    def bg_to_oven(self):
        self.background_image = self.change_background("background images/kitchen backgrounds/Kitchen - Oven BG.png")
        self.pizza_fly_in()
        
    # place the pizza on the oven
    def pizza_fly_in(self):
        pass
    