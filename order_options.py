import pygame
import os
from constants import Constants
import sys

class orderOptions:
    def __init__(self):
        pygame.init()

        # change to constants in class
        self.c = Constants()
        self.WIDTH = self.c.screen_width
        self.HEIGHT = self.c.screen_height

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption("order taking")

        self.TA1count = 0
        self.TA2count = 0
        self.TA3count = 0
        self.TA4count = 0
        self.TA5count = 0
        self.TA6count = 0
        self.TA7count = 0
        self.TA8count = 0

    def setup(self):
        self.bg = pygame.image.load(os.path.join("background images", "waiter backgrounds", "Waiter - Cashier BG.png"))
        self.bg = pygame.transform.scale(self.bg, (self.WIDTH, self.HEIGHT))
        self.screen.blit(self.bg, (0, 0))

        self.toppingArea1 = pygame.Rect(780, 160, 42, 42)
        self.toppingArea2 = pygame.Rect(780, 200, 42, 42)
        self.toppingArea3 = pygame.Rect(780, 240, 42, 42)
        self.toppingArea4 = pygame.Rect(780, 280, 42, 42)
        self.toppingArea5 = pygame.Rect(780, 320, 42, 42)
        self.toppingArea6 = pygame.Rect(780, 360, 42, 42)
        self.toppingArea7 = pygame.Rect(780, 400, 42, 42)

        # pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.toppingArea7), 10)

    def toppingArea(self, x, y, click, color):
        self.TA = pygame.image.load(os.path.join("pictures", "toppingAreaImage.png"))
        self.TA = pygame.transform.scale(self.TA, (35, 35))

        if color == 1: # pink
            self.TAbg = pygame.image.load(os.path.join("pictures", "blankToppingAreaPink.png"))
        
        else: # white
            self.TAbg = pygame.image.load(os.path.join("pictures", "blankToppingAreaWhite.png"))

        if (click == 1):
            self.screen.blit(self.TAbg, (x+2, y+3))
            self.screen.blit(self.TA, (x+16, y+16))

        if (click == 2):
            self.TA = pygame.transform.flip(self.TA, True, False)
            self.screen.blit(self.TAbg, (x+2, y+3))
            self.screen.blit(self.TA, (x-2, y+16))

        if (click == 3):
            self.TA = pygame.transform.flip(self.TA, True, True)
            self.screen.blit(self.TAbg, (x+2, y+3))
            self.screen.blit(self.TA, (x-2, y-4))

        if (click == 4):
            self.TA = pygame.transform.flip(self.TA, False, True)
            self.screen.blit(self.TAbg, (x+2, y+3))
            self.screen.blit(self.TA, (x+16, y-4))
        
        if (click == 5):
            self.screen.blit(self.TAbg, (x+2, y+3))
            self.screen.blit(self.TA, (x+16, y+16))
            self.TA = pygame.transform.flip(self.TA, False, True)
            self.screen.blit(self.TA, (x+16, y-4))

        if (click == 6):
            self.screen.blit(self.TAbg, (x+2, y+3))
            self.TA = pygame.transform.flip(self.TA, True, False)
            self.screen.blit(self.TA, (x-2, y+16))
            self.TA = pygame.transform.flip(self.TA, False, True)
            self.screen.blit(self.TA, (x-2, y-4))

        if (click == 0):
            self.screen.blit(self.TAbg, (x+2, y+3))
            self.screen.blit(self.TA, (x+16, y+16))
            self.TA = pygame.transform.flip(self.TA, False, True)
            self.screen.blit(self.TA, (x+16, y-4))
            self.TA = pygame.transform.flip(self.TA, True, True)
            self.screen.blit(self.TA, (x-2, y+16))
            self.TA = pygame.transform.flip(self.TA, False, True)
            self.screen.blit(self.TA, (x-2, y-4))

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
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.toppingArea1.collidepoint(pygame.mouse.get_pos()):
                        self.TA1count += 1
                        self.toppingArea(self.toppingArea1[0], self.toppingArea1[1], self.TA1count % 7, 1)
                    
                    if self.toppingArea2.collidepoint(pygame.mouse.get_pos()):
                        self.TA2count += 1
                        self.toppingArea(self.toppingArea2[0], self.toppingArea2[1], self.TA2count % 7, 2)

                    if self.toppingArea3.collidepoint(pygame.mouse.get_pos()):
                        self.TA3count += 1
                        self.toppingArea(self.toppingArea3[0], self.toppingArea3[1], self.TA3count % 7, 1)

                    if self.toppingArea4.collidepoint(pygame.mouse.get_pos()):
                        self.TA4count += 1
                        self.toppingArea(self.toppingArea4[0], self.toppingArea4[1], self.TA4count % 7, 2)

                    if self.toppingArea5.collidepoint(pygame.mouse.get_pos()):
                        self.TA5count += 1
                        self.toppingArea(self.toppingArea5[0], self.toppingArea5[1], self.TA5count % 7, 1)

                    if self.toppingArea6.collidepoint(pygame.mouse.get_pos()):
                        self.TA6count += 1
                        self.toppingArea(self.toppingArea6[0], self.toppingArea6[1], self.TA6count % 7, 2)

                    if self.toppingArea7.collidepoint(pygame.mouse.get_pos()):
                        self.TA7count += 1
                        self.toppingArea(self.toppingArea7[0], self.toppingArea7[1], self.TA7count % 7, 1)

            pygame.display.flip()


if __name__ == "__main__":
    c = orderOptions()
    c.run()

