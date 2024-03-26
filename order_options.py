import pygame
import pyautogui
import os
import sys

class orderOptions:
    def __init__(self):
        pygame.init()

        self.WIDTH = 1350
        self.HEIGHT = 765

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption("order taking")

    def setup(self):
        self.bg = pygame.image.load(os.path.join("background images", "waiter backgrounds", "Waiter - Cashier BG.png"))
        self.screen.blit(self.bg, (0, 0))

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

                # add something for resizing the screen

            pygame.display.flip()


if __name__ == "__main__":
    c = orderOptions()
    c.run()

