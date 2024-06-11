import pygame
from chef_files.chef import Chef
from constants import Constants
import math

class SatisfactionScore(Chef):
    
    def __init__(self, screen, c):
        self.background_image = None
        self.c = c
        self.pizza_image_location = (430, 120)
        
        self.num_cuts = 0
        
        super().__init__(screen, self.c)
        
        
    def bg_to_complete_pizza(self):
        self.c.curr_screen_name = "satisfaction"
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
        
    
    def display_satisfaction_score(self):
        satisfaction_score = 100
        
        diff1 = abs(self.c.angles[0] - 50)
        
        if self.num_cuts == 0:
            satisfaction_score -= 0.25 * diff1    
        if self.num_cuts == 2:
            diff2 = abs(self.c.angles[1])
            satisfaction_score -= 0.25 * diff1
            satisfaction_score -= 10 * diff2
        else:
            satisfaction_score -= 0.25 * diff1
            diff2 = abs(self.c.angles[1])
            satisfaction_score -= 10 * diff2
            diff3 = abs(self.c.angles[1] - (1 / math.sqrt(3)))
            satisfaction_score -= 10 * diff3
        
        total_num_toppings = len(self.c.toppings)
        exact_num_toppings = self.c.VALUES_JSON["M1"] + self.c.VALUES_JSON["M2"] + self.c.VALUES_JSON["M3"] + self.c.VALUES_JSON["M4"] + self.c.VALUES_JSON["M5"] + self.c.VALUES_JSON["M6"] + self.c.VALUES_JSON["M7"]
        
        satisfaction_score -= 10 * abs(exact_num_toppings - total_num_toppings) + 5
        satisfaction_score = int(satisfaction_score)
        
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Satisfaction Score: " + str(satisfaction_score), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (730, 600)
        self.screen.blit(text, text_rect)
    