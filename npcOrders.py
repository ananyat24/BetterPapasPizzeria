import pygame
import os
from constants import Constants
import sys
import random

class npcOrders:
    def __init__(self):
        pygame.init()

        # change to constants in class
        self.c = Constants()
        self.WIDTH = self.c.screen_width
        self.HEIGHT = self.c.screen_height

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption("npc order taking")

    def setup(self):
        self.bg = pygame.image.load(os.path.join("background images", "waiter backgrounds", "Waiter - Cashier BG.png"))
        self.bg = pygame.transform.scale(self.bg, (self.WIDTH, self.HEIGHT))
        self.screen.blit(self.bg, (0, 0))

    def orderChoices(self):
        orders = ['6 artichokes and 4 mushrooms on half pizza. Cut in 6 slices. 30 minutes',
                  '8 olives on full pizza. Cut in 8 slices. 45 minutes',
                  '5 spinach and 7 tomatoes on half pizza. Cut in 4 slices. 15 minutes',
                  '10 pepperoni and 3 onions on full pizza. Cut in 8 slices. 60 minutes',
                  '7 artichokes, 5 mushrooms, and 4 spinach on full pizza. Cut in 6 slices. 30 minutes',
                  '9 pineapple and 6 olives on full pizza. Cut in 8 slices. 45 minutes',
                  '4 tomatoes and 8 spinach on half pizza. Cut in 2 slices. 15 minutes',
                  '7 olives, 3 pepperoni, and 5 mushrooms on full pizza. Cut in 4 slices. 60 minutes',
                  '10 onions and 5 artichokes on half pizza. Cut in 6 slices. 30 minutes',
                  '6 spinach and 9 mushrooms on full pizza. Cut in 8 slices. 45 minutes',
                  '8 pepperoni and 5 pineapple on half pizza. Cut in 4 slices. 60 minutes',
                  '7 olives, 2 onions, and 5 tomatoes on full pizza. Cut in 6 slices. 45 minutes',
                  '9 artichokes on full pizza. Cut in 8 slices. 30 minutes',
                  '4 pineapple, 5 mushrooms, and 3 spinach each on different quarters of pizza. Cut in 4 slices. 60 minutes',
                  '6 onions, 7 tomatoes, and 8 olives on full pizza. Cut in 8 slices. 45 minutes',
                  '5 spinach and 3 artichokes on half pizza. Cut in 2 slices. 15 minutes',
                  '8 mushrooms and 4 onions on full pizza. Cut in 6 slices. 60 minutes',
                  '7 tomatoes and 5 pepperoni on half pizza. Cut in 8 slices. 45 minutes',
                  '6 pineapple, 3 spinach, and 4 artichokes on full pizza. Cut in 4 slices. 30 minutes',
                  '9 mushrooms and 2 onions on half pizza. Cut in 6 slices. 60 minutes',
                  '5 artichokes and 6 mushrooms on full pizza. Cut in 8 slices. 45 minutes',
                  '7 olives and 3 tomatoes on half pizza. Cut in 4 slices. 15 minutes',
                  '8 pepperoni and 5 onions on full pizza. Cut in 6 slices. 30 minutes',
                  '4 spinach and 7 pineapple on half pizza. Cut in 2 slices. 60 minutes',
                  '6 tomatoes, 5 mushrooms, and 4 olives on full pizza. Cut in 8 slices. 45 minutes',
                  '10 artichokes and 3 spinach on full pizza. Cut in 6 slices. 30 minutes',
                  '5 pineapple and 7 olives on half pizza. Cut in 4 slices. 15 minutes',
                  '6 onions and 8 tomatoes on full pizza. Cut in 8 slices. 60 minutes',
                  '7 mushrooms and 4 pepperoni on half pizza. Cut in 6 slices. 45 minutes',
                  '9 spinach and 2 artichokes on full pizza. Cut in 4 slices. 30 minutes',
                  '5 onions and 6 pineapple on full pizza. Cut in 6 slices. 60 minutes',
                  '8 mushrooms and 3 tomatoes on half pizza. Cut in 4 slices. 15 minutes',
                  '7 artichokes and 5 pepperoni on full pizza. Cut in 8 slices. 45 minutes',
                  '4 spinach and 6 olives on half pizza. Cut in 2 slices. 30 minutes',
                  '9 onions and 5 pineapple on full pizza. Cut in 8 slices. 60 minutes',
                  '6 tomatoes and 8 artichokes on full pizza. Cut in 6 slices. 45 minutes',
                  '5 mushrooms and 7 spinach on half pizza. Cut in 4 slices. 15 minutes',
                  '10 olives and 3 onions on full pizza. Cut in 8 slices. 30 minutes',
                  '4 artichokes and 8 pineapple on full pizza. Cut in 6 slices. 60 minutes',
                  '6 pepperoni and 5 mushrooms on half pizza. Cut in 2 slices. 45 minutes',
                  '7 spinach and 3 tomatoes on full pizza. Cut in 8 slices. 30 minutes',
                  '5 onions and 8 olives on half pizza. Cut in 4 slices. 60 minutes',
                  '6 artichokes and 7 pineapple on full pizza. Cut in 8 slices. 45 minutes',
                  '4 spinach and 5 pepperoni on half pizza. Cut in 6 slices. 30 minutes',
                  '9 mushrooms and 8 tomatoes on full pizza. Cut in 8 slices. 45 minutes',
                  '7 olives and 6 onions on half pizza. Cut in 4 slices. 60 minutes',
                  '5 artichokes and 4 spinach on full pizza. Cut in 8 slices. 15 minutes',
                  '6 pineapple and 8 pepperoni on half pizza. Cut in 6 slices. 45 minutes',
                  '7 tomatoes and 5 mushrooms on full pizza. Cut in 4 slices. 30 minutes',
                  '10 olives and 6 onions on half pizza. Cut in 2 slices. 60 minutes',
                  '4 spinach and 8 artichokes on full pizza. Cut in 8 slices. 45 minutes',
                  '5 pineapple and 7 olives on half pizza. Cut in 4 slices. 15 minutes',
                  '9 mushrooms and 6 tomatoes on full pizza. Cut in 8 slices. 30 minutes',
                  '7 onions and 4 pepperoni on half pizza. Cut in 6 slices. 60 minutes',
                  '8 artichokes and 5 spinach on full pizza. Cut in 8 slices. 45 minutes',
                  '6 olives and 7 pineapple on half pizza. Cut in 2 slices. 15 minutes',
                  '5 mushrooms and 8 tomatoes on full pizza. Cut in 6 slices. 30 minutes',
                  '4 onions and 9 pepperoni on half pizza. Cut in 4 slices. 60 minutes',
                  '7 artichokes and 6 spinach on full pizza. Cut in 8 slices. 45 minutes',
                  '5 olives and 4 mushrooms on half pizza. Cut in 2 slices. 15 minutes',
                  '8 pineapple and 7 onions on full pizza. Cut in 6 slices. 30 minutes',
                  '6 tomatoes and 5 pepperoni on half pizza. Cut in 6 slices. 60 minutes',
                  '7 mushrooms and 4 spinach on full pizza. Cut in 8 slices. 45 minutes',
                  '5 artichokes and 6 olives on half pizza. Cut in 4 slices. 30 minutes',
                  '8 onions and 9 pineapple on full pizza. Cut in 6 slices. 60 minutes',
                  '7 tomatoes and 5 spinach on half pizza. Cut in 4 slices. 45 minutes',
                  '6 pepperoni and 4 mushrooms on full pizza. Cut in 8 slices. 15 minutes',
                  '10 olives and 3 onions on half pizza. Cut in 6 slices. 30 minutes',
                  '5 artichokes and 6 pineapple on full pizza. Cut in 8 slices. 60 minutes',
                  '8 mushrooms and 7 spinach on half pizza. Cut in 4 slices. 45 minutes',
                  '6 olives and 5 tomatoes on full pizza. Cut in 6 slices. 30 minutes',
                  '7 onions and 4 artichokes on half pizza. Cut in 2 slices. 15 minutes',
                  '9 pepperoni and 8 pineapple on full pizza. Cut in 8 slices. 60 minutes',
                  '5 spinach and 6 mushrooms on half pizza. Cut in 6 slices. 45 minutes',
                  '8 tomatoes and 7 olives on full pizza. Cut in 4 slices. 30 minutes']
    
        randOrder = random.randint(0, 74)
        order = orders[randOrder]
        print(order)

         # add random order, character (if time LATER, add multiple players w an array to keep track of who had what order)

    def textDisplay(self):
        quit # print selected order

    def charDisplay(self):
        quit # print sprite sliding upon call

    def accuracyCalc(self):
        quit # compare request to order ticket

    # random order, order options, text display, character display, add to array for tables, requested order score

    def run(self):
        self.setup()
        self.orderChoices()

        while True:
            reload = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                # add something for resizing the screen
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.SMTH.collidepoint(pygame.mouse.get_pos()):
                        quit

if __name__ == "__main__":
    n = npcOrders()
    n.run()