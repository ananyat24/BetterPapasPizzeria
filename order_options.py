import pygame
import os
from constants import Constants
import sys
import network
import npcOrders
import time

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

        self.IA1count = 0
        self.IA2count = 0
        self.IA3count = 0
        self.IA4count = 0
        self.IA5count = 0
        self.IA6count = 0
        self.IA7count = 0
        self.IA8count = 0

        self.sliceCount = 0
        self.timerCount = 0

        self.toppingArea1 = pygame.Rect(1054, 155, 65, 55)
        self.toppingArea2 = pygame.Rect(1054, 206, 65, 55)
        self.toppingArea3 = pygame.Rect(1054, 257, 65, 55)
        self.toppingArea4 = pygame.Rect(1054, 308, 65, 55)
        self.toppingArea5 = pygame.Rect(1054, 359, 65, 55)
        self.toppingArea6 = pygame.Rect(1054, 410, 65, 55)
        self.toppingArea7 = pygame.Rect(1054, 461, 65, 55)

        self.ingredientArea1 = pygame.Rect(1130, 160, 120, 50)
        self.ingredientArea2 = pygame.Rect(1130, 211, 120, 50)
        self.ingredientArea3 = pygame.Rect(1130, 262, 120, 50)
        self.ingredientArea4 = pygame.Rect(1130, 313, 120, 50)
        self.ingredientArea5 = pygame.Rect(1130, 364, 120, 50)
        self.ingredientArea6 = pygame.Rect(1130, 415, 120, 50)
        self.ingredientArea7 = pygame.Rect(1130, 466, 120, 50)

        self.multiplierArea1 = pygame.Rect(1270, 160, 55, 50)
        self.multiplierArea2 = pygame.Rect(1270, 211, 55, 50)
        self.multiplierArea3 = pygame.Rect(1270, 262, 55, 50)
        self.multiplierArea4 = pygame.Rect(1270, 313, 55, 50)
        self.multiplierArea5 = pygame.Rect(1270, 364, 55, 50)
        self.multiplierArea6 = pygame.Rect(1270, 415, 55, 50)
        self.multiplierArea7 = pygame.Rect(1270, 466, 55, 50)

        self.sliceArea = pygame.Rect(1230, 525, 85, 83)
        self.completeButton = pygame.Rect(1050, 610, 280, 55)
        self.timerArea = pygame.Rect(1075, 525, 82, 73)

        self.startTimer = None
        self.duration = 15

        # pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.completeButton), 10)

    def setup(self):
        self.bg = pygame.image.load(os.path.join("background images", "waiter backgrounds", "Waiter - Cashier BG.png"))
        self.bg = pygame.transform.scale(self.bg, (self.WIDTH, self.HEIGHT))
        self.screen.blit(self.bg, (0, 0))

    def update(self):
        c = Constants()
        
        c.VALUES_JSON = {
                       "S1": self.TA1count, "T1": self.IA1count, "M1": self.MA1count,
                       "S2": self.TA2count, "T2": self.IA2count, "M2": self.MA2count,
                       "S3": self.TA3count, "T3": self.IA3count, "M3": self.MA3count,
                       "S4": self.TA4count, "T4": self.IA4count, "M4": self.MA4count,
                       "S5": self.TA5count, "T5": self.IA5count, "M5": self.MA5count,
                       "S6": self.TA6count, "T6": self.IA6count, "M6": self.MA6count,
                       "S7": self.TA7count, "T7": self.IA7count, "M7": self.MA7count,
                       "CUTS": self.sliceCount, "TIME": self.timerCount
                       }
        
        c.ticketLoad()
        c.ticketSave()

    def toppingArea(self, x, y, click, color):
        self.TA = pygame.image.load(os.path.join("pictures", "toppingAreaImage.png"))
        self.TA = pygame.transform.scale(self.TA, (43, 43))

        if color == 1: # pink
            self.TAbg = pygame.image.load(os.path.join("pictures", "blankToppingAreaPink.png"))
        
        else: # white
            self.TAbg = pygame.image.load(os.path.join("pictures", "blankToppingAreaWhite.png"))

        self.TAbg = pygame.transform.scale(self.TAbg, (60, 47))

        if (click == 1):
            self.screen.blit(self.TAbg, (x+2, y+7))
            self.screen.blit(self.TA, (x+20, y+19))

        elif (click == 2):
            self.TA = pygame.transform.flip(self.TA, True, False)
            self.screen.blit(self.TAbg, (x+2, y+7))
            self.screen.blit(self.TA, (x-2, y+19))

        elif (click == 3):
            self.TA = pygame.transform.flip(self.TA, True, True)
            self.screen.blit(self.TAbg, (x+2, y+7))
            self.screen.blit(self.TA, (x-2, y-3))

        elif (click == 4):
            self.TA = pygame.transform.flip(self.TA, False, True)
            self.screen.blit(self.TAbg, (x+2, y+7))
            self.screen.blit(self.TA, (x+20, y-3))
        
        elif (click == 5):
            self.screen.blit(self.TAbg, (x+2, y+7))
            self.screen.blit(self.TA, (x+20, y+19))
            self.TA = pygame.transform.flip(self.TA, False, True)
            self.screen.blit(self.TA, (x+20, y-3))

        elif (click == 6):
            self.screen.blit(self.TAbg, (x+2, y+7))
            self.TA = pygame.transform.flip(self.TA, True, False)
            self.screen.blit(self.TA, (x-2, y+19))
            self.TA = pygame.transform.flip(self.TA, False, True)
            self.screen.blit(self.TA, (x-2, y-3))

        elif (click == 0):
            self.screen.blit(self.TAbg, (x+2, y+7))
            self.screen.blit(self.TA, (x+20, y+19))
            self.TA = pygame.transform.flip(self.TA, False, True)
            self.screen.blit(self.TA, (x+20, y-3))
            self.TA = pygame.transform.flip(self.TA, True, True)
            self.screen.blit(self.TA, (x-2, y+19))
            self.TA = pygame.transform.flip(self.TA, False, True)
            self.screen.blit(self.TA, (x-2, y-3))

        self.update()

    def ingredientArea(self, x, y, click, color):
        self.artichoke = pygame.image.load(os.path.join("pictures", "single_ingredients", "artichoke.png"))
        self.artichoke = pygame.transform.scale(self.artichoke, (50, 50))

        self.mushroom = pygame.image.load(os.path.join("pictures", "single_ingredients", "mushroom.png"))
        self.mushroom = pygame.transform.scale(self.mushroom, (50, 50))

        self.olive = pygame.image.load(os.path.join("pictures", "single_ingredients", "olive.png"))
        self.olive = pygame.transform.scale(self.olive, (50, 50))

        self.onions = pygame.image.load(os.path.join("pictures", "single_ingredients", "onions.png"))
        self.onions = pygame.transform.scale(self.onions, (50, 50))

        self.pepperoni = pygame.image.load(os.path.join("pictures", "single_ingredients", "pepperoni.png"))
        self.pepperoni = pygame.transform.scale(self.pepperoni, (50, 50))

        self.pineapple = pygame.image.load(os.path.join("pictures", "single_ingredients", "pineapple.png"))
        self.pineapple = pygame.transform.scale(self.pineapple, (50, 50))

        self.spinach = pygame.image.load(os.path.join("pictures", "single_ingredients", "spinach.png"))
        self.spinach = pygame.transform.scale(self.spinach, (50, 50))

        self.tomato = pygame.image.load(os.path.join("pictures", "single_ingredients", "tomato.png"))
        self.tomato = pygame.transform.scale(self.tomato, (50, 50))

        if color == 1: # pink
            self.bgColor = (253, 210, 206)
        
        else: # white
            self.bgColor = (255, 255, 255)

        if (click == 1):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y+2, 50, 47))
            self.screen.blit(self.artichoke, (x, y))

        elif (click == 2):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y+2, 50, 47))
            self.screen.blit(self.mushroom, (x, y))

        elif (click == 3):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y+2, 50, 47))
            self.screen.blit(self.olive, (x, y))

        elif (click == 4):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y+2, 50, 47))
            self.screen.blit(self.onions, (x, y))

        elif (click == 5):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y+2, 50, 47))
            self.screen.blit(self.pepperoni, (x, y))

        elif (click == 6):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y+2, 50, 47))
            self.screen.blit(self.pineapple, (x, y))

        elif (click == 7):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y+2, 50, 47))
            self.screen.blit(self.spinach, (x, y))

        elif (click == 0):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y+2, 50, 42))
            self.screen.blit(self.tomato, (x, y))

        self.update()

    def multiplierArea(self, x, y, click, color):
        self.M1X = pygame.image.load(os.path.join("pictures", "1x_image.png"))
        self.M1X = pygame.transform.scale(self.M1X, (55, 50))

        self.M2X = pygame.image.load(os.path.join("pictures", "2x_image.png"))
        self.M2X = pygame.transform.scale(self.M2X, (55, 50))

        self.M3X = pygame.image.load(os.path.join("pictures", "3x_image.png"))
        self.M3X = pygame.transform.scale(self.M3X, (55, 50))

        self.M4X = pygame.image.load(os.path.join("pictures", "4x_image.png"))
        self.M4X = pygame.transform.scale(self.M4X, (55, 50))

        if color == 1: # pink
            self.bgColor = (253, 210, 206)
        
        else: # white
            self.bgColor = (255, 255, 255)

        if (click == 1):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y,55, 50))
            self.screen.blit(self.M1X, (x, y))

        elif (click == 2):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y, 55, 50))
            self.screen.blit(self.M2X, (x, y))

        elif (click == 3):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y, 55, 50))
            self.screen.blit(self.M3X, (x, y))

        elif (click == 0):
            pygame.draw.rect(self.screen, self.bgColor, pygame.Rect(x, y, 55, 50))
            self.screen.blit(self.M4X, (x, y))

        self.update()

    def sliceSelect (self, click):
        self.sliceBG = pygame.image.load(os.path.join("pictures", "ticketSliceBG.jpg"))
        self.sliceBG = pygame.transform.scale(self.sliceBG, (82, 80))
        self.sliceColor = (97, 71, 24)

        x = self.sliceArea.x - 3.5
        y = self.sliceArea.y - 6.5

        if (click == 1):
            self.screen.blit(self.sliceBG, (x, y))
            pygame.draw.rect(self.screen, self.sliceColor, pygame.Rect(x+43, y+9, 2, 70))

        elif (click == 2):
            pygame.draw.rect(self.screen, self.sliceColor, pygame.Rect(x+8, y+45, 70, 2))

        elif (click == 3):
            self.screen.blit(self.sliceBG, (x, y))
            pygame.draw.line(self.screen, self.sliceColor, (x+17, y+21), (x+70, y+66), 3)
            pygame.draw.line(self.screen, self.sliceColor, (x+70, y+21), (x+20, y+70), 3)
            pygame.draw.rect(self.screen, self.sliceColor, pygame.Rect(x+43, y+9, 2, 70))

        elif (click == 0):
            pygame.draw.rect(self.screen, self.sliceColor, pygame.Rect(x+43, y+9, 2, 70))
            pygame.draw.rect(self.screen, self.sliceColor, pygame.Rect(x+8, y+45, 70, 2))

        self.update()

    def timerSelect (self, click):
        self.timeBG = pygame.image.load(os.path.join("pictures", "ticketSliceBG.jpg"))
        self.timeBG = pygame.transform.scale(self.timeBG, (82, 80))
        self.timeHand = pygame.image.load(os.path.join("pictures", "timerHand.png"))
        self.timeHand = pygame.transform.scale(self.timeHand, (8, 35))

        x = self.timerArea.x - 3.5
        y = self.timerArea.y - 6.5

        if (click == 1):
            self.screen.blit(self.timeBG, (x+5, y))
            self.screen.blit(self.timeHand, (x+44, y+13))

        elif (click == 2):
            self.screen.blit(self.timeBG, (x+5, y))
            self.timeHand = pygame.transform.rotate(self.timeHand, 270)
            self.screen.blit(self.timeHand, (x+45, y+40))

        elif (click == 3):
            self.screen.blit(self.timeBG, (x+5, y))
            self.timeHand = pygame.transform.rotate(self.timeHand, 180)
            self.screen.blit(self.timeHand, (x+46, y+40))

        elif (click == 0):
            self.screen.blit(self.timeBG, (x+5, y))
            self.timeHand = pygame.transform.rotate(self.timeHand, 90)
            self.screen.blit(self.timeHand, (x+20, y+40))
        self.update()

    def onComplete (self):
        c = Constants()
        c.ticketLoad
        c.ticketSave
        return c.VALUES_JSON
            
    def miniTimer(self):
        if self.startTimer is None:
            return
        
        self.passed = time.time() - self.startTimer
        self.left = self.duration - self.passed
        
        if self.left < 0:
            pygame.draw.rect(self.screen, (212, 238,241), pygame.Rect(0, 0, 1030, 300))
            return

        font = pygame.font.SysFont("comicsans", int(30))
        timerPrint = font.render(str(int(self.left)) + "  ", True, (0,0,0), (212,238,241))
        self.screen.blit(timerPrint, (960, 30))

    def run(self, n, data):
        n = npcOrders.npcOrders()

        self.setup()
        n.orderChoices()
        self.startTimer = time.time()

        while True:
            reload = False
            self.miniTimer()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        
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

                    elif self.ingredientArea1.collidepoint(pygame.mouse.get_pos()):
                        self.IA1count +=1
                        self.ingredientArea(self.ingredientArea1[0], self.ingredientArea1[1], self.IA1count % 8, 1)

                    elif self.ingredientArea2.collidepoint(pygame.mouse.get_pos()):
                        self.IA2count +=1
                        self.ingredientArea(self.ingredientArea2[0], self.ingredientArea2[1], self.IA2count % 8, 2)

                    elif self.ingredientArea3.collidepoint(pygame.mouse.get_pos()):
                        self.IA3count +=1
                        self.ingredientArea(self.ingredientArea3[0], self.ingredientArea3[1], self.IA3count % 8, 1)

                    elif self.ingredientArea4.collidepoint(pygame.mouse.get_pos()):
                        self.IA4count +=1
                        self.ingredientArea(self.ingredientArea4[0], self.ingredientArea4[1], self.IA4count % 8, 2)

                    elif self.ingredientArea5.collidepoint(pygame.mouse.get_pos()):
                        self.IA5count +=1
                        self.ingredientArea(self.ingredientArea5[0], self.ingredientArea5[1], self.IA5count % 8, 1)

                    elif self.ingredientArea6.collidepoint(pygame.mouse.get_pos()):
                        self.IA6count +=1
                        self.ingredientArea(self.ingredientArea6[0], self.ingredientArea6[1], self.IA6count % 8, 2)

                    elif self.ingredientArea7.collidepoint(pygame.mouse.get_pos()):
                        self.IA7count +=1
                        self.ingredientArea(self.ingredientArea7[0], self.ingredientArea7[1], self.IA7count % 8, 1)

                    elif self.sliceArea.collidepoint(pygame.mouse.get_pos()):
                        self.sliceCount +=1
                        self.sliceSelect(self.sliceCount % 4)

                    elif self.timerArea.collidepoint(pygame.mouse.get_pos()):
                        self.timerCount +=1
                        self.timerSelect(self.timerCount % 4)

                    elif self.completeButton.collidepoint(pygame.mouse.get_pos()):
                        json_to_send = self.onComplete() # send ticket to chef
                        data = {"stage": "in_level", "role": "waiter", "to_send_to_chef" : {"receipt": json_to_send, "receipt score" : None}, "to_send_to_waiter": None}
                        # print(data)
                        d = network.Network()
                        data = d.send(data)

                        o = npcOrders.npcOrders()
                        self.setup()
                        o.orderChoices()
                        self.startTimer = time.time()

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
                        self.IA1count = 0
                        self.IA2count = 0
                        self.IA3count = 0
                        self.IA4count = 0
                        self.IA5count = 0
                        self.IA6count = 0
                        self.IA7count = 0
                        self.IA8count = 0
                        self.sliceCount = 0
                        self.timerCount = 0

                        self.update()
                
            pygame.display.flip()

            if reload: break
        c = Constants()
        c.VALUES_JSON = {
                        "S1": self.TA1count, "T1": self.IA1count, "M1": self.MA1count,
                        "S2": self.TA2count, "T2": self.IA2count, "M2": self.MA2count,
                        "S3": self.TA3count, "T3": self.IA3count, "M3": self.MA3count,
                        "S4": self.TA4count, "T4": self.IA4count, "M4": self.MA4count,
                        "S5": self.TA5count, "T5": self.IA5count, "M5": self.MA5count,
                        "S6": self.TA6count, "T6": self.IA6count, "M6": self.MA6count,
                        "S7": self.TA7count, "T7": self.IA7count, "M7": self.MA7count,
                        "CUTS": self.sliceCount, "TIME": self.timerCount
                        }
    
        c.ticketLoad()
        c.ticketSave()

if __name__ == "__main__":
    c = orderOptions()
    c.run()