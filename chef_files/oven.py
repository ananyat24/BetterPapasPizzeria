import pygame
from chef_files.chef import Chef
from constants import Constants
import datetime
import math

class Oven(Chef):
    
    def __init__(self, screen:pygame.display, c:Constants):
        
        self.cooking_time = 0  # stores how long the player cooks the pizza for (used for calculating satsifaction at end)
        self.background_image = None
        
        self.c = c
        
        self.pizza_image_location = (330, 140)
        
        # create the images for the clock
        hand_img = pygame.image.load("pictures/timerHand.png")
        self.hand_image = pygame.transform.scale(hand_img, (10, 37))
        clock_img = pygame.image.load("pictures/OLD ticketSliceBG.png")
        self.clock_image = pygame.transform.scale(clock_img, (130, 110))
        
        self.clock_stopped = False
        
        super().__init__(screen, self.c)
        
        
    # switch the background to the oven
    def bg_to_oven(self):
        self.background_image = self.change_background("background images/kitchen backgrounds/Kitchen - Oven BG.png")
        self.pizza_fly_in()
        
        # display timer to screen
        self.screen.blit(self.clock_image, (int(self.c.screen_width/2) - 200, 550))
        #self.screen.blit(self.hand_image, (int(self.c.screen_width/2) - 140, 565))
        
        self.start_timer()
        
        
    # place the pizza on the oven
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
        
        
    def polar_to_cartesian(self, r, theta):
        x = int(r * math.cos(math.pi * theta / 180))
        y = int(r * math.sin(math.pi * theta / 180))
        adjusted_x = int(self.c.screen_width/2) - 200 + 65 + x
        adjusted_y = int(550 + 55 - y)
        print("x" + str(adjusted_x))
        print("y" + adjusted_y)
        return (adjusted_x, adjusted_y)
        
        
    def start_timer(self):
        current_time = datetime.datetime.now()
        
        self.oven_clock_button = pygame.Rect((130, 110, int(self.c.screen_width/2) - 200, 550))
        
        while not self.clock_stopped:
            second = current_time.second
            r = 55
            adjusted_theta = 90 - (second * 60)
            #self.screen.blit(self.hand_image, self.polar_to_cartesian(r, adjusted_theta))
            pygame.draw.line(self.screen, (0, 0, 0), (int(self.c.screen_width/2) - 200 + 65, 605), self.polar_to_cartesian(r, adjusted_theta), 7)
            pygame.display.update()
                
            if self.oven_clock_button.collidepoint(pygame.mouse.get_pos()):
                self.clock_stopped = True
            
            pygame.time.wait(500)
        
        #pygame.time.wait(1000)
    