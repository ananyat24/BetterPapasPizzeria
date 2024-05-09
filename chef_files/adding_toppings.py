import pygame
from chef_files.chef import Chef
from constants import Constants
from chef_files.topping import Topping

class AddingToppings(Chef):
    
    def __init__(self, screen:pygame.display, c:Constants):
        self.c = c
        self.pizza_image_location = (295, 65)
        self.background_image = None

        
        # contains a list of all toppings
        self.topping_boxes = []
        
        super().__init__(screen, self.c)
        
        # create each topping as a separate object
        artichoke = Topping("pictures/single_ingredients/artichoke.png", (715, 150), screen, self.c)
        self.topping_boxes.append(artichoke)
        
        mushroom = Topping("pictures/single_ingredients/mushroom.png", (650, 405), screen, self.c)
        self.topping_boxes.append(mushroom)
        
        olive = Topping("pictures/single_ingredients/olive.png", (715, 290), screen, self.c)
        self.topping_boxes.append(olive)
        
        onions = Topping("pictures/single_ingredients/onions.png", (170, 285), screen, self.c)
        self.topping_boxes.append(onions)
        
        pepperoni = Topping("pictures/single_ingredients/pepperoni.png", (170, 150), screen, self.c)
        self.topping_boxes.append(pepperoni)
        
        pineapple = Topping("pictures/single_ingredients/pineapple.png", (230, 400), screen, self.c)
        self.topping_boxes.append(pineapple)
        
        spinach = Topping("pictures/single_ingredients/spinach.png", (650, 40), screen, self.c)
        self.topping_boxes.append(spinach)
        
        tomato = Topping("pictures/single_ingredients/tomato.png", (240, 30), screen, self.c)
        self.topping_boxes.append(tomato)

        
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
        