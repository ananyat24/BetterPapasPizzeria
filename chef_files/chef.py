import pygame
from constants import Constants

class Chef:
    
    def __init__(self, screen:pygame.display, c:Constants):
        self.c = c
        self.screen = screen
    
    
    # show the current pizza (needed for erasing cutting line)

    def display_current_pizza(self):
        
        # get needed variables from Constants class
        print(len(self.c.lines))
        curr_screen_name = self.c.curr_screen_name
        curr_toppings = self.c.toppings
        
        # clear the screen (background + plain pizza displayed)
        self.screen.blit(self.c.background_image, (0, 0))
        self.screen.blit(self.c.pizza_image, (self.c.pizza_image_location[0], self.c.pizza_image_location[1]))
        
        # check what the current screen is and adjust object positions accordingly
        if curr_screen_name == "toppings":
            x_change_topping = 0
            y_change_topping = 0
            x_change_lines = self.c.cutting_to_toppings[0]
            y_change_lines = self.c.cutting_to_toppings[1]
        elif curr_screen_name == "oven":
            x_change_topping = self.c.toppings_to_oven[0]
            y_change_topping = self.c.toppings_to_oven[1]
            x_change_lines = self.c.cutting_to_oven[0]
            y_change_lines = self.c.cutting_to_oven[1]
        else:
            x_change_topping = self.c.toppings_to_cutting[0]
            y_change_topping = self.c.toppings_to_cutting[1]
            x_change_lines = 0
            y_change_lines = 0
        
        # display pizza toppings
        for t in curr_toppings:
            new_location = (t[1][0] + x_change_topping, t[1][1] + y_change_topping)
            self.screen.blit(t[0], new_location)
        
        # display the pizza cuts
        for line in self.c.lines:
            new_line_start = (line[2][0] + x_change_lines, line[2][1] + y_change_lines)
            new_line_end = (line[3][0] + x_change_lines, line[3][1] + y_change_lines)
            pygame.draw.line(line[0], line[1], new_line_start, new_line_end, line[4])
            
            
    # add new images to the screen
    def add_pizza_image(self, image, location:tuple): # locations is a list of tuples in the form (x_pos, y_pos)
        self.c.pizza_image = image
        self.c.pizza_image_location = location
        
    
    # change the background depending on what task is being done
    def change_background(self, image_filepath:str):
        img = pygame.image.load(image_filepath)
        image = pygame.transform.scale(img, (self.c.screen_width, self.c.screen_height))
        self.c.background_image = image
        return image
            