import pygame
import os
from constants import Constants
import sys
import order_options

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
        x = 1060
        y = 162
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
                self.order.toppingArea(x, (y + (45*(value/3)) + 2*(value-2)), click, color)
            
            value += 1

    def fillToppings (self):
        x = 1140
        y = 149
        color = 0
        click = 0
        value = 0

        for i in self.valueList:
            if value%3 != 1 or value > 20:
                value += 1
                continue

            click = i % 8
            if value % 2 == 1:
                color = 1
            else:
                color = 0

            if i != 0:
                self.order.ingredientArea(x, (y + (45*(value/3)) + 2*(value-2)), click, color)
            
            value += 1

    def fillMultiplier (self):
        x = 1265
        y = 133
        color = 0
        click = 0
        value = 0

        for i in self.valueList:
            if value%3 != 2 or value > 20:
                value += 1
                continue

            click = i % 4
            if value % 2 == 1:
                color = 0
            else:
                color = 1

            if i != 0:
                self.order.multiplierArea(x, (y + (45*(value/3)) + 2*(value-2)), click, color)
            
            value += 1
        
    def fillSlices (self):
        click = self.valueList[21]

        self.order.sliceArea.x = self.order.sliceArea.x + 4
        self.order.sliceArea.y = self.order.sliceArea.y + 3
        
        if click != 0:
            click %= 4
            self.order.sliceSelect(click)

    def fillTimer (self):
        click = self.valueList[22]

        self.order.timerArea.x = self.order.timerArea.x + 4
        self.order.timerArea.y = self.order.timerArea.y + 3
        
        if click != 0:
            click %= 4
            self.order.timerSelect(click)

    def run(self):
        self.fillArea()
        self.fillToppings()
        self.fillMultiplier()
        self.fillSlices()
        self.fillTimer()

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
    o.setup()
    o.run()