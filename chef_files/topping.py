import pygame

class Topping():

    def __init__(self, image_filepath:str, location:tuple, screen:pygame.display, c):
        one_topping_img = pygame.image.load(image_filepath)
        self.one_topping_image = pygame.transform.scale(one_topping_img, (30, 30))
        
        self.location = location # tuple in the form (x_coordinate, y_coordinate) for top left corner of topping box
        self.width = 150 # same for each topping box
        self.height = 150 # same for each topping boxs
        self.rect = pygame.Rect(self.location, (self.width, self.height))
        
        self.screen = screen
        self.c = c
    
    
    # drag the topping from the container to the pizza
    def topping_follow_cursor(self, current_toppings:list, order_ticket):
        # clear screen first
        self.screen.blit(self.c.background_image, (0, 0))
        self.screen.blit(self.c.pizza_image, (self.c.pizza_image_location[0], self.c.pizza_image_location[1]))
        order_ticket.run()
        
        for t in current_toppings:
            self.screen.blit(t[0], t[1])
        
        # display new topping that's being dragged
        x_pos, y_pos = pygame.mouse.get_pos()
        self.screen.blit(self.one_topping_image, (x_pos, y_pos))

        