import pygame
import os
from constants import Constants
import sys
import order_options
import json

class orderTicketFill:
    def __init__(self):
        pygame.init()

        # change to constants in class
        self.c = Constants()
        self.WIDTH = self.c.screen_width
        self.HEIGHT = self.c.screen_height

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption("order ticket filling (for chef)")

        self.order = order_options.orderOptions()

        c = Constants()
        self.values = c.ticketLoad()
        self.valueList = list(self.values.values())
        # print (self.values)

    # delete later
    def setup(self):
        self.bg = pygame.image.load(os.path.join("background images", "kitchen backgrounds", "Kitchen - Order BG.png"))
        self.bg = pygame.transform.scale(self.bg, (self.WIDTH, self.HEIGHT))
        self.screen.blit(self.bg, (0, 0))

    def fillArea (self):
        x = 780
        y = 160
        color = 0
        click = 0
        value = 0

        for i in self.valueList:
            if value%3 != 0 or value > 20:
                value += 1
                continue

            click = i % 7
            if value % 2 == 1:
                color = 0
            else:
                color =1

            if i != 0:
                self.order.toppingArea(x, (y + (40*(value/3))), click, color)
            
            value += 1

    def fillToppings (self):
        quit

    def fillMultiplier (self):
        quit
        
    def fillSlices (self):
        quit

    def run(self):
        self.setup()
        self.fillArea()
        self.fillToppings()
        self.fillMultiplier()
        self.fillSlices()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()

if __name__ == "__main__":
    o = orderTicketFill()
    o.run()