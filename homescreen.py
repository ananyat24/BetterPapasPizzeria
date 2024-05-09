import pygame
import os
from constants import Constants
import sys
import order_options
from chef_files import chef

class homescreen:
    def __init__(self):
        pygame.init()

        self.c = Constants()
        self.WIDTH = self.c.screen_width
        self.HEIGHT = self.c.screen_height

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption("starting the game")
        

    def setup(self):
        self.bg = pygame.image.load(os.path.join("background images", "Homescreen.png"))
        self.bg = pygame.transform.scale(self.bg, (self.WIDTH, self.HEIGHT))
        self.screen.blit(self.bg, (0, 0))

        self.button1 = pygame.Rect(350, 325, 300, 80)
        self.button2 = pygame.Rect(350, 420, 300, 80)
        self.button3 = pygame.Rect(350, 515, 300, 80)

    def run(self):
        self.setup()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                # add smth to resize screen
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button1.collidepoint(pygame.mouse.get_pos()):
                        if self.c.playerNumber == 1:
                            o = order_options.orderOptions()
                            o.run()

                        if self.c.playerNumber == 2:
                            c = chef.Chef
                            c.run()



            pygame.display.flip()

if __name__ == "__main__":
    h = homescreen()
    h.run()
