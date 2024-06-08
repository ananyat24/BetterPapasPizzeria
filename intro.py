import pygame
import time
import os
import sys
from constants import Constants


YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)

class TextScroll:
    
    def __init__(self, area, font, fg_color, bk_color, text, ms_per_line = 500):
        super().__init__()
        self.rect = area.copy()
        self.fg_color = fg_color
        self.bk_color = bk_color
        self.size = area.size
        self.surface = pygame.Surface(self.size, flags = pygame.SRCALPHA)
        self.surface.fill(bk_color)
        self.font = font
        self.lines = text.split('\n')
        self.ms_per_line = ms_per_line
        self.y = 0
        self.delta_y =  self.font.size("M")[1]
        self.next_time = None
        self.dirty = False

    def update_line(self, line):
        if self.y + self.delta_y > self.size[1]:
            self.surface.blit(self.surface, (0, -self.delta_y))
            self.y += -self.delta_y
            pygame.draw.rect(self.surface, self.bk_color, 
                             (0, self.y, self.size(0), self.size[1]-self.y))
            
        text = self.font.render(line, True, self.fg_color)
        self.surface.blit(text, (0,self.y))

        self.y += self.delta_y

    def update(self):
        
        curr_time = time.time()
        if (self.next_time is None or self.next_time < curr_time) and self.lines:
            self.next_time = curr_time + self.ms_per_line/1000
            line = self.lines.pop(0)
            self.update_line(line)
            self.dirty = True
            self.update()

    def draw(self, screen):
        if self.dirty:
            screen.blit(self.surface, self.rect)
            self.dirty = False


INTRO = """Welcome to Papa's Pizzeria Multiplayer!!
In this game, there will be two players working together to run the pizzeria
and make Papa and the customers satisfied!
The two roles are Chef, and Waiter. Only one player can be in a role at a time. 
The Waiter will take orders manually, by clicking on the order form to update numbers 
of certain ingredients, time to bake, and slices cut.
The Chef will then take the order form and place toppings, bake, and cut the pizza accordingly. 
The pizza is then handed to the customer.

The goal of this game is to get high satisfaction scores from our customers, by working efficiently 
and collaboratively.

After all, at Papa Louie's Pizzeria, Your Satisfaction is Our Priority!

Let's get to work!"""
    
def run():
    c = Constants()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "1560, 100"
    pygame.init()
    screen = pygame.display.set_mode((c.screen_width, c.screen_height))
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Comic Sans MS", 30)
    message = TextScroll(pygame.Rect(50, 50, c.screen_width - 100, c.screen_height - 100), font, YELLOW, BLACK, INTRO, ms_per_line=1500)

    time_passed = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
                sys.exit(0)
        else:
            # screen.fill(pygame.color.Color('black'))
            message.update()
            message.draw(screen)
            pygame.display.flip()
            clock.tick(60)
    
    # button = pygame.image.load(os.path.join("pictures", "instructions_continue.png"))
    # screen.blit(button, (c.screen_width- 70, c.screen_height - 70))








    
