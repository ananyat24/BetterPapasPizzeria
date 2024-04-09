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

        self.MA1count = 0
        self.MA2count = 0
        self.MA3count = 0
        self.MA4count = 0
        self.MA5count = 0
        self.MA6count = 0
        self.MA7count = 0
        self.MA8count = 0

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

        self.multiplierArea1 = pygame.Rect(940, 165, 42, 42)
        self.multiplierArea2 = pygame.Rect(940, 205, 42, 42)
        self.multiplierArea3 = pygame.Rect(940, 245, 42, 42)
        self.multiplierArea4 = pygame.Rect(940, 285, 42, 42)
        self.multiplierArea5 = pygame.Rect(940, 325, 42, 42)
        self.multiplierArea6 = pygame.Rect(940, 365, 42, 42)
        self.multiplierArea7 = pygame.Rect(940, 405, 42, 42)

        # pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.multiplierArea7), 10)

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

    def multiplierArea(self, x, y, click, color):
        self.M1X = pygame.image.load(os.path.join("pictures", "1x_image.png"))
        self.M1X = pygame.transform.scale(self.M1X, (40, 40))

        self.M2X = pygame.image.load(os.path.join("pictures", "2x_image.png"))
        self.M2X = pygame.transform.scale(self.M2X, (40, 40))

        self.M3X = pygame.image.load(os.path.join("pictures", "3x_image.png"))
        self.M3X = pygame.transform.scale(self.M3X, (40, 40))

        self.M4X = pygame.image.load(os.path.join("pictures", "4x_image.png"))
        self.M4X = pygame.transform.scale(self.M4X, (40, 40))

        if color == 1: # pink
            self.bgColor = (253, 210, 206)
        
        else: # white
            self.bgColor = (255, 255, 255)

        if (click == 1):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y, 35, 35))
            self.screen.blit(self.M1X, (x, y))

        if (click == 2):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y, 35, 35))
            self.screen.blit(self.M2X, (x, y))

        if (click == 3):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y, 35, 35))
            self.screen.blit(self.M3X, (x, y))

        if (click == 0):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y, 35, 35))
            self.screen.blit(self.M4X, (x, y))

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
                    
                    elif self.toppingArea2.collidepoint(pygame.mouse.get_pos()):
                        self.TA2count += 1
                        self.toppingArea(self.toppingArea2[0], self.toppingArea2[1], self.TA2count % 7, 2)

                    elif self.toppingArea3.collidepoint(pygame.mouse.get_pos()):
                        self.TA3count += 1
                        self.toppingArea(self.toppingArea3[0], self.toppingArea3[1], self.TA3count % 7, 1)

                    elif self.toppingArea4.collidepoint(pygame.mouse.get_pos()):
                        self.TA4count += 1
                        self.toppingArea(self.toppingArea4[0], self.toppingArea4[1], self.TA4count % 7, 2)

                    elif self.toppingArea5.collidepoint(pygame.mouse.get_pos()):
                        self.TA5count += 1
                        self.toppingArea(self.toppingArea5[0], self.toppingArea5[1], self.TA5count % 7, 1)

                    elif self.toppingArea6.collidepoint(pygame.mouse.get_pos()):
                        self.TA6count += 1
                        self.toppingArea(self.toppingArea6[0], self.toppingArea6[1], self.TA6count % 7, 2)

                    elif self.toppingArea7.collidepoint(pygame.mouse.get_pos()):
                        self.TA7count += 1
                        self.toppingArea(self.toppingArea7[0], self.toppingArea7[1], self.TA7count % 7, 1)

                    elif self.multiplierArea1.collidepoint(pygame.mouse.get_pos()):
                        self.MA1count +=1
                        self.multiplierArea(self.multiplierArea1[0], self.multiplierArea1[1], self.MA1count % 4, 1)

                    elif self.multiplierArea2.collidepoint(pygame.mouse.get_pos()):
                        self.MA2count +=1
                        self.multiplierArea(self.multiplierArea2[0], self.multiplierArea2[1], self.MA2count % 4, 2)

                    elif self.multiplierArea3.collidepoint(pygame.mouse.get_pos()):
                        self.MA3count +=1
                        self.multiplierArea(self.multiplierArea3[0], self.multiplierArea3[1], self.MA3count % 4, 1)

                    elif self.multiplierArea4.collidepoint(pygame.mouse.get_pos()):
                        self.MA4count +=1
                        self.multiplierArea(self.multiplierArea4[0], self.multiplierArea4[1], self.MA4count % 4, 2)

                    elif self.multiplierArea5.collidepoint(pygame.mouse.get_pos()):
                        self.MA5count +=1
                        self.multiplierArea(self.multiplierArea5[0], self.multiplierArea5[1], self.MA5count % 4, 1)

                    elif self.multiplierArea6.collidepoint(pygame.mouse.get_pos()):
                        self.MA6count +=1
                        self.multiplierArea(self.multiplierArea6[0], self.multiplierArea6[1], self.MA6count % 4, 2)

                    elif self.multiplierArea7.collidepoint(pygame.mouse.get_pos()):
                        self.MA7count +=1
                        self.multiplierArea(self.multiplierArea7[0], self.multiplierArea7[1], self.MA7count % 4, 1)

            pygame.display.flip()


if __name__ == "__main__":
    c = orderOptions()
    c.run()

