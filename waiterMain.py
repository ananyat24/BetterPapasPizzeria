# decided not to use this...

import pygame
import os
from constants import Constants
import sys

class waiterRun:
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

    # switching between screens, functionality of page per function

    def run(self):
        self.setup()

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
                        
                # elif event.type == pygame.MOUSEBUTTONDOWN:
                #     if self.SMTH.collidepoint(pygame.mouse.get_pos()):
                #         quit

                pygame.display.flip()

if __name__ == "__main__":
    w = waiterRun()
    w.run()