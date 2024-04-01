import pygame
import os
import constants
import sys

class orderOptions:
    def __init__(self):
        pygame.init()

        # change to constants in class
        self.WIDTH = 1350
        self.HEIGHT = 765

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
        self.screen.blit(self.bg, (0, 0))

        self.toppingArea1 = pygame.Rect(1075, 210, 42, 42)
        self.toppingArea2 = pygame.Rect(1075, 260, 42, 42)
        self.toppingArea3 = pygame.Rect(1075, 310, 42, 42)
        self.toppingArea4 = pygame.Rect(1075, 360, 42, 42)
        self.toppingArea5 = pygame.Rect(1075, 410, 42, 42)
        self.toppingArea6 = pygame.Rect(1075, 460, 42, 42)
        self.toppingArea7 = pygame.Rect(1075, 510, 42, 42)
        self.toppingArea8 = pygame.Rect(1075, 560, 42, 42)

        # self.screen.blit(self.screen, self.toppingArea7)

    def toppingArea(self, x, y, click):
        self.TA = pygame.image.load(os.path.join("pictures", "toppingAreaImage.png"))
        # self.screen.blit(self.TA, (1000, 600))
        print(click)

        if (click == 1):
            self.screen.blit(self.TA, (x+16, y+16))
            print(x+21, y)

        if (click == 2):
            self.screen.blit(self.TA, (x-16, y+16))

        if (click == 3):
            self.screen.blit(self.TA, (x+21, y))

        if (click == 4):
            self.screen.blit(self.TA, (x+21, y))
        
        if (click == 5):
            self.screen.blit(self.TA, (x+21, y))

        if (click == 6):
            self.screen.blit(self.TA, (x+21, y))

        if (click == 0):
            self.screen.blit(self.TA, (x+21, y))

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
                        self.toppingArea(self.toppingArea1[0], self.toppingArea1[1], self.TA1count % 7)
                    
                    if self.toppingArea2.collidepoint(pygame.mouse.get_pos()):
                        self.TA2count += 1
                        self.toppingArea(self.toppingArea2[0], self.toppingArea2[1], self.TA2count % 7)

                    if self.toppingArea3.collidepoint(pygame.mouse.get_pos()):
                        self.TA3count += 1
                        self.toppingArea(self.toppingArea3[0], self.toppingArea3[1], self.TA3count % 7)

                    if self.toppingArea4.collidepoint(pygame.mouse.get_pos()):
                        self.TA4count += 1
                        self.toppingArea(self.toppingArea4[0], self.toppingArea4[1], self.TA4count % 7)

                    if self.toppingArea5.collidepoint(pygame.mouse.get_pos()):
                        self.TA5count += 1
                        self.toppingArea(self.toppingArea5[0], self.toppingArea5[1], self.TA5count % 7)

                    if self.toppingArea6.collidepoint(pygame.mouse.get_pos()):
                        self.TA6count += 1
                        self.toppingArea(self.toppingArea6[0], self.toppingArea6[1], self.TA6count % 7)

                    if self.toppingArea7.collidepoint(pygame.mouse.get_pos()):
                        self.TA7count += 1
                        self.toppingArea(self.toppingArea7[0], self.toppingArea7[1], self.TA7count % 7)

                    if self.toppingArea8.collidepoint(pygame.mouse.get_pos()):
                        self.TA8count += 1
                        self.toppingArea(self.toppingArea8[0], self.toppingArea8[1], self.TA8count % 7)

            pygame.display.flip()


if __name__ == "__main__":
    c = orderOptions()
    c.run()

