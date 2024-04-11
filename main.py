import pygame
from constants import Constants
from network import Network

# create the screen
pygame.init()
pygame.font.init() 
c = Constants()
screen = pygame.display.set_mode((c.screen_width, c.screen_height))
homescreen_image = pygame.image.load("background images/Homescreen.png")

# intialize all the variables
gameloop = True


my_font = pygame.font.SysFont('Comic Sans MS', 30)
n = Network()
n.connect()

data = {"type":"into", "data": {"key": None, "color": None}}

# gameloop
while gameloop:
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                data["data"]["key"] = "left"
                data = n.send(data)
            if event.key == pygame.K_RIGHT:
                data["data"]["key"] = "right"
                data = n.send(data)
    if data["data"]["color"]:
        if data["data"]["color"] == "red":
            screen.fill((255,0,0))
        else:
            screen.fill((0, 255,0))
    else:
        screen.blit(homescreen_image, (0, 0))
    pygame.display.update()
    # n.send("hi")

    # print(n.get_role())

    # text_surface = my_font.render(n.get_role(), False, (0, 0, 0))
    # screen.blit(text_surface, (0,0))

pygame.quit()
