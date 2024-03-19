import pygame

class Topping():
    
    def __init__(self, image:pygame.image, location:tuple, screen:pygame.display):
        self.image = image
        self.location = location
        self.screen = screen
        self.screen.blit(self.image, self.location)     
    
    # get the image and location for the topping
    def get_image_location(self):
        return (self.image, self.location)
        