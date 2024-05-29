import pygame
from constants import Constants

class Chef:
    
    def __init__(self, screen:pygame.display, c:Constants):
        self.c = c
        self.screen = screen
    
    
    # show the current pizza (needed for erasing cutting line)

    def display_current_pizza(self, curr_toppings:list):
        # clear the screen (background + plain pizza displayed)
        self.screen.blit(self.c.background_image, (0, 0))
        self.screen.blit(self.c.pizza_image, (self.c.pizza_image_location[0], self.c.pizza_image_location[1]))
        
        # display pizza toppings
        for t in curr_toppings:
            self.screen.blit(t[0], t[1])
        
        # display the pizza cuts
        for line in self.c.lines:
            pygame.draw.line(line[0], line[1], line[2], line[3], line[4])
            
        """
        use the code below to make the topping_boxes code more concise if time

        for tb in self.c.topping_boxes:
            self.screen.blit(tb[0], tb[1])
        """
            
            
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
            