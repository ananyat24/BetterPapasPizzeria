import pygame
import os
from constants import Constants
import sys
import random
import time
# import Player

class npcOrders:
    def __init__(self):
        pygame.init()

        # change to constants in class
        self.c = Constants()
        self.WIDTH = self.c.screen_width
        self.HEIGHT = self.c.screen_height

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        
        # self.screen.fill((0, 0, 0))
        # pygame.display.set_caption("npc order taking")

        self.activeOrders = [] # add data w/ self.activeOrders.append([int index, "name", "sprite", {order data}, int satisfaction score])

        self.currentSprite = ""
        self.image = None

    # def customer_yapping(self, username: str, sprite_sheet:str, start_x, start_y):
    #     self.curr_customer = Player.Player(username, sprite_sheet, start_x, start_y)
    #     self.curr_customer.order = self.orderChoices()
    #     image =  pygame.image.load(os.path.join("Images", "berthaspritesheet_standing.png"))
    #     while self.curr_customer.player_rectangle.topleft[0] <= 450:
    #         self.curr_customer.updatePosition(5, 0)
    #         self.setup()
    #         self.curr_customer.moveChar(self.screen)
    #         pygame.display.flip()
    #         pygame.time.delay(50)

    def setup(self):
        self.bg = pygame.image.load(os.path.join("background images", "waiter backgrounds", "Waiter - Cashier BG.png"))
        self.bg = pygame.transform.scale(self.bg, (self.WIDTH, self.HEIGHT))
        self.screen.blit(self.bg, (0, 0))

    def orderChoices(self): # these orders were mostly AI generated
        """
        orders = ['I would like a pizza with 4 slices, bake it for 45 minutes, with artichokes on the top left (2), mushrooms on the right half (1), and olives covering the whole pizza (3).',
                'Can I get 8 slices and bake it for 30 minutes? I want pepperoni on the whole pizza (2) and spinach on the top right (1).',
                'I need a pizza with 6 slices, bake it for 60 minutes, and please add pineapple on the bottom left (3), tomato on the right half (1), and olives across the whole pizza (2).',
                'Could you do 2 slices, 15 minutes in the oven, with artichoke on the left half (1) and mushrooms on the whole pizza (2)?',
                'I want 4 slices and 45 minutes of baking, with spinach on the top left (2), tomato on the bottom right (3), and olives everywhere (1).',
                'Give me a pizza with 8 slices, 60 minutes baking time, pepperoni on the right half (2), bell peppers on the whole pizza (1), and mushrooms on the bottom left (3).',
                'I will take 6 slices, bake it for 30 minutes, with pineapple on the top right (2), tomato on the bottom right (1), spinach over the whole pizza (4), and olives on the top left (2).',
                'Just 2 slices, bake it for 15 minutes, olives all over (1), and artichoke on the left half (2).',
                'Can you make it 8 slices, bake for 60 minutes? Put pepperoni on the bottom left (3) and mushrooms on the top left (2).',
                'For me, 4 slices, 45 minutes in the oven, with pineapple all over (2), tomato on the right half (3), and spinach on the top right (1).',
                'I want 6 slices, bake it for 30 minutes, and please add mushrooms on the bottom right (2), artichokes on the left half (1), olives on the top left (4), and spinach all over (3).',
                'I would like 8 slices, bake it for 15 minutes, with pepperoni on the whole pizza (3) and olives on the top right (1).',
                'Make it 4 slices, bake for 45 minutes, with spinach on the bottom left (1) and mushrooms on the right half (2).',
                'For me, 2 slices, bake it for 60 minutes, and add tomato everywhere (2) and pineapple on the top right (1).',
                'Give me 6 slices, 15 minutes baking time, artichoke on the bottom left (2), spinach all over (1), and tomato on the right half (3).',
                'I want 8 slices, bake it for 30 minutes, with pepperoni on the whole pizza (4), mushrooms on the top left (2), and olives on the bottom right (3).',
                'I will have 2 slices, bake it for 45 minutes, with pineapple on the left half (2) and mushrooms covering the whole pizza (1).',
                'I would like 6 slices, 60 minutes in the oven, spinach on the top right (3), tomato on the bottom left (2), and olives all over (1).',
                'I need 8 slices, bake for 15 minutes, with mushrooms on the right half (2), artichokes on the top left (1), and olives on the whole pizza (4).',
                'For me, 4 slices, bake for 30 minutes, with pineapple on the bottom right (1), tomato all over (2), and spinach on the right half (3).',
                'Give me 6 slices, bake for 60 minutes, spinach on the left half (3), artichokes on the bottom left (2), and olives all over (1).',
                'I would like 8 slices, bake for 45 minutes, with pepperoni on the top right (2), bell peppers all over (1), mushrooms on the bottom right (3), and spinach on the left half (4).',
                'Can you make it 2 slices, bake for 30 minutes? Add pineapple on the right half (2) and tomato on the bottom left (1).',
                'I would like 4 slices, bake for 15 minutes, olives on the top left (3) and artichoke all over (2).',
                'I need 6 slices, bake for 60 minutes, with pepperoni on the top left (2), mushrooms on the bottom right (1), and spinach all over (4).',
                'I will take 8 slices, bake it for 45 minutes, with artichokes on the bottom left (2), tomato on the top left (1), and olives on the whole pizza (3).',
                'Give me 4 slices, bake it for 30 minutes, with pineapple on the whole pizza (2) and spinach on the top right (1).',
                'I would like 6 slices, bake for 15 minutes, artichoke on the bottom left (3), mushrooms on the right half (1), and olives everywhere (2).',
                'Can I get 2 slices, bake it for 60 minutes? Put pepperoni on the left half (2) and pineapple on the whole pizza (1).',
                'I want 8 slices, bake it for 30 minutes, with tomato on the top left (2), spinach all over (3), and olives on the bottom right (1).',
                'Give me 4 slices, bake for 45 minutes, artichokes on the top left (2), mushrooms on the right half (1), and olives on the whole pizza (3).',
                'I need 6 slices, bake for 60 minutes, pepperoni on the bottom left (3), pineapple on the right half (1), and spinach all over (2).',
                'I would like 2 slices, bake it for 15 minutes, artichokes on the left half (1) and tomato all over (2).',
                'Can you make it 8 slices, bake it for 30 minutes? Pineapple on the bottom right (2), spinach on the top left (1), and olives on the whole pizza (3).',
                'Give me 4 slices, bake for 45 minutes, mushrooms on the right half (2), tomato on the bottom left (1), and olives on the whole pizza (3).',
                'I want 6 slices, bake for 60 minutes, artichoke on the top right (3), mushrooms on the bottom left (2), and spinach all over (1).',
                'I will take 2 slices, bake it for 15 minutes, pineapple on the right half (2) and tomato on the whole pizza (1).',
                'I need 8 slices, bake for 30 minutes, olives on the top left (3) and artichoke on the whole pizza (2).',
                'For me, 4 slices, bake for 45 minutes, pepperoni on the bottom right (2) and pineapple all over (1).',
                'I would like 6 slices, bake for 60 minutes, mushrooms on the top left (2), spinach on the right half (1), and olives everywhere (4).',
                'Can you make it 8 slices, bake it for 15 minutes? Tomato on the bottom left (2), artichoke on the top right (1), and spinach all over (3).',
                'I want 4 slices, bake for 30 minutes, pineapple all over (2) and spinach on the right half (1).',
                'Give me 6 slices, bake for 45 minutes, mushrooms on the top right (2), olives on the bottom left (3), and pepperoni everywhere (1).',
                'I need 2 slices, bake it for 60 minutes, spinach on the left half (2) and tomato all over (1).',
                'I would like 8 slices, bake for 30 minutes, artichoke on the top left (3) and olives on the whole pizza (2).',
                'For me, 4 slices, bake for 15 minutes, pineapple on the bottom right (2) and mushrooms on the whole pizza (1).',
                'I want 6 slices, bake it for 60 minutes, artichokes on the top right (2), tomatoes on the bottom left (1), and olives all over (3).',
                'Can I get 8 slices, bake for 45 minutes, spinach on the top left (3) and pepperoni all over (2).',
                'I would like 2 slices, bake it for 15 minutes, with mushrooms on the right half (2) and artichoke on the whole pizza (1).',
                'I need 4 slices, bake for 30 minutes, with pineapple on the bottom left (1) and spinach all over (2).',
        """
        orders = ['I would like a pizza with 6 slices, bake it for 45 minutes, with artichokes on the top left (2), mushrooms on the right half (1), and olives covering the whole pizza (3).',
                'Can I get 6 slices and bake it for 30 minutes? I want pepperoni on the whole pizza (2) and spinach on the top right (1).',
                'I need a pizza with 6 slices, bake it for 60 minutes, and please add pineapple on the bottom left (3), tomato on the right half (1), and olives across the whole pizza (2).',
                'Could you do 6 slices, 15 minutes in the oven, with artichoke on the left half (1) and mushrooms on the whole pizza (2)?',
                'I want 6 slices and 45 minutes of baking, with spinach on the top left (2), tomato on the bottom right (3), and olives everywhere (1).',
                'Give me a pizza with 6 slices, 60 minutes baking time, pepperoni on the right half (2), bell peppers on the whole pizza (1), and mushrooms on the bottom left (3).',
                'I will take 6 slices, bake it for 30 minutes, with pineapple on the top right (2), tomato on the bottom right (1), spinach over the whole pizza (4), and olives on the top left (2).',
                'Just 6 slices, bake it for 15 minutes, olives all over (1), and artichoke on the left half (2).',
                'Can you make it 6 slices, bake for 60 minutes? Put pepperoni on the bottom left (3) and mushrooms on the top left (2).',
                'For me, 6 slices, 45 minutes in the oven, with pineapple all over (2), tomato on the right half (3), and spinach on the top right (1).',
                'I want 6 slices, bake it for 30 minutes, and please add mushrooms on the bottom right (2), artichokes on the left half (1), olives on the top left (4), and spinach all over (3).',
                'I would like 6 slices, bake it for 15 minutes, with pepperoni on the whole pizza (3) and olives on the top right (1).',
                'Make it 6 slices, bake for 45 minutes, with spinach on the bottom left (1) and mushrooms on the right half (2).',
                'For me, 6 slices, bake it for 60 minutes, and add tomato everywhere (2) and pineapple on the top right (1).',
                'Give me 6 slices, 15 minutes baking time, artichoke on the bottom left (2), spinach all over (1), and tomato on the right half (3).',
                'I want 6 slices, bake it for 30 minutes, with pepperoni on the whole pizza (4), mushrooms on the top left (2), and olives on the bottom right (3).',
                'I will have 6 slices, bake it for 45 minutes, with pineapple on the left half (2) and mushrooms covering the whole pizza (1).',
                'I would like 6 slices, 60 minutes in the oven, spinach on the top right (3), tomato on the bottom left (2), and olives all over (1).',
                'I need 6 slices, bake for 15 minutes, with mushrooms on the right half (2), artichokes on the top left (1), and olives on the whole pizza (4).',
                'For me, 6 slices, bake for 30 minutes, with pineapple on the bottom right (1), tomato all over (2), and spinach on the right half (3).',
                'Give me 6 slices, bake for 60 minutes, spinach on the left half (3), artichokes on the bottom left (2), and olives all over (1).',
                'I would like 6 slices, bake for 45 minutes, with pepperoni on the top right (2), bell peppers all over (1), mushrooms on the bottom right (3), and spinach on the left half (4).',
                'Can you make it 6 slices, bake for 30 minutes? Add pineapple on the right half (2) and tomato on the bottom left (1).',
                'I would like 6 slices, bake for 15 minutes, olives on the top left (3) and artichoke all over (2).',
                'I need 6 slices, bake for 60 minutes, with pepperoni on the top left (2), mushrooms on the bottom right (1), and spinach all over (4).',
                'I will take 6 slices, bake it for 45 minutes, with artichokes on the bottom left (2), tomato on the top left (1), and olives on the whole pizza (3).',
                'Give me 6 slices, bake it for 30 minutes, with pineapple on the whole pizza (2) and spinach on the top right (1).',
                'I would like 6 slices, bake for 15 minutes, artichoke on the bottom left (3), mushrooms on the right half (1), and olives everywhere (2).',
                'Can I get 6 slices, bake it for 60 minutes? Put pepperoni on the left half (2) and pineapple on the whole pizza (1).',
                'I want 6 slices, bake it for 30 minutes, with tomato on the top left (2), spinach all over (3), and olives on the bottom right (1).',
                'Give me 6 slices, bake for 45 minutes, artichokes on the top left (2), mushrooms on the right half (1), and olives on the whole pizza (3).',
                'I need 6 slices, bake for 60 minutes, pepperoni on the bottom left (3), pineapple on the right half (1), and spinach all over (2).',
                'I would like 6 slices, bake it for 15 minutes, artichokes on the left half (1) and tomato all over (2).',
                'Can you make it 6 slices, bake it for 30 minutes? Pineapple on the bottom right (2), spinach on the top left (1), and olives on the whole pizza (3).',
                'Give me 6 slices, bake for 45 minutes, mushrooms on the right half (2), tomato on the bottom left (1), and olives on the whole pizza (3).',
                'I want 6 slices, bake for 60 minutes, artichoke on the top right (3), mushrooms on the bottom left (2), and spinach all over (1).',
                'I will take 6 slices, bake it for 15 minutes, pineapple on the right half (2) and tomato on the whole pizza (1).',
                'I need 6 slices, bake for 30 minutes, olives on the top left (3) and artichoke on the whole pizza (2).',
                'For me, 6 slices, bake for 45 minutes, pepperoni on the bottom right (2) and pineapple all over (1).',
                'I would like 6 slices, bake for 60 minutes, mushrooms on the top left (2), spinach on the right half (1), and olives everywhere (4).',
                'Can you make it 6 slices, bake it for 15 minutes? Tomato on the bottom left (2), artichoke on the top right (1), and spinach all over (3).',
                'I want 6 slices, bake for 30 minutes, pineapple all over (2) and spinach on the right half (1).',
                'Give me 6 slices, bake for 45 minutes, mushrooms on the top right (2), olives on the bottom left (3), and pepperoni everywhere (1).',
                'I need 6 slices, bake it for 60 minutes, spinach on the left half (2) and tomato all over (1).',
                'I would like 6 slices, bake for 30 minutes, artichoke on the top left (3) and olives on the whole pizza (2).',
                'For me, 6 slices, bake for 15 minutes, pineapple on the bottom right (2) and mushrooms on the whole pizza (1).',
                'I want 6 slices, bake it for 60 minutes, artichokes on the top right (2), tomatoes on the bottom left (1), and olives all over (3).',
                'Can I get 6 slices, bake for 45 minutes, spinach on the top left (3) and pepperoni all over (2).',
                'I would like 6 slices, bake it for 15 minutes, with mushrooms on the right half (2) and artichoke on the whole pizza (1).',

]
    
        randOrder = random.randint(0, 49)
        order = orders[randOrder]
        self.charDisplay(order)
        print(order)
        return order
         # add random order, character (if time LATER, add multiple players w an array to keep track of who had what order)

    def textDisplay(self, text):
        font = pygame.font.SysFont("comicsans", int(30))
        textBreaks = self.breakLines(text, font)
        x = 80
        y = 80

        for l in textBreaks:
            c = font.render(l, True, (255, 255, 255), (0, 0 , 0))
            self.screen.blit(c, (x, y))
            y += 60

        # self.startTimer = time.time()

    def breakLines(self, text, font):
        chars = len(text)
        lines = []
        lineText = ""
        i = 0
        word = ""
        
        while i < chars:
            if text[i] == " ":
                textWidth, _ = font.size(lineText)
                wordWidth, _ = font.size(word)

                if (textWidth + wordWidth) > 900:
                    lines.append(lineText)
                    lineText = word + " "
                    word = ""

                else:
                    word += " "
                    lineText += word
                    word = ""

            else:
                word += text[i]

            if i == chars - 1:
                lineText += word

            i += 1

        lines.append(lineText)
        return lines

    def charDisplay(self, text):
        self.spriteSelect()
        self.spriteArrival()

        self.textDisplay(text)
        pygame.time.wait(15)

        # print sprite leaving screen

    def spriteSelect(self):
        sprites = ["allanspritesheet_thumbs up.png", "allanspritesheet_angry.png", "berthaspritesheet_happy.png", "berthaspritesheet_angry.png", "joyspritesheet2.png"]
        r = random.randint(0,4)
        self.currentSprite = sprites[r]
        self.image = pygame.image.load(os.path.join("Images", self.currentSprite))
        self.image = pygame.transform.scale(self.image, (1350, 225))

        n = 5
        if self.currentSprite == "joyspritesheet2.png":
            n = 7
        elif self.currentSprite == "berthaspritesheet_angry.png":
            n = 6

        w = (self.image.get_width())/n

        self.image = self.image.subsurface((w*2, 0, w, self.image.get_height())).copy()
        self.image = pygame.transform.scale(self.image, (int(1.3*self.image.get_width()), int(1.3*self.image.get_height())))

    def spriteArrival(self):
        x = 450
        y = 245
        self.screen.blit(self.image, (x, y))

    # def spriteExit(self): # implement if time
    #     quit

    def accuracyCalc(self):
        quit # compare request to order ticket

    def customerInfo(self):
        return # customer name, sprite, order array

    # random order, order options, text display, character display, add to array for tables, requested order score

    def run(self):
        self.orderChoices()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            # self.miniTimer()

                # add something for resizing the screen
                        
                # elif event.type == pygame.MOUSEBUTTONDOWN:
                #     if self.SMTH.collidepoint(pygame.mouse.get_pos()):
                #         quit

            pygame.display.flip()

if __name__ == "__main__":
    n = npcOrders()
    n.setup()
    n.run()