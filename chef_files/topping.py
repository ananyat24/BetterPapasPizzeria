import pygame

class Topping():
    
    def __init__(self, image_filepath:str, location:tuple, width:int, height:int, screen:pygame.display):
        self.one_topping_image = pygame.image.load(image_filepath)
        
        self.location = location # tuple in the form (x_coordinate, y_coordinate)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.location, (self.width, self.height))
        
        self.screen = screen
    
    
    # drag the topping from the container to the pizza
    def topping_follow_cursor(self):
        pass
        