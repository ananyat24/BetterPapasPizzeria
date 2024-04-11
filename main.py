import pygame
from constants import Constants
from network import Network
from order_options import orderOptions
from chef_main import Chef

# create the screen
pygame.init()
pygame.font.init() 
pygame.font.init() 
c = Constants()
screen = pygame.display.set_mode((c.screen_width, c.screen_height))
homescreen_image = pygame.image.load("background images/Homescreen.png")
waiter = orderOptions()
chef = Chef()

# intialize all the variables
gameloop = True


my_font = pygame.font.SysFont('Comic Sans MS', 30)
n = Network()
n.connect()

data = {"stage":"intro", "data": {"key": None, "color": None, "role": None}}

# gameloop
while gameloop:
    




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    if data["stage"] == "intro":
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                data["data"]["key"] = "left"
                data = n.send(data)
            if event.key == pygame.K_RIGHT:
                data["data"]["key"] = "right"
                data = n.send(data)
        pygame.display.update()

    if data["stage"] == "waiter1":
            waiter.run()

    if data["stage"] == "chef1":
            chef.run()
    else:
        screen.blit(homescreen_image, (0, 0))
        pygame.display.update()
    # n.send("hi")

    # print(n.get_role())

    # text_surface = my_font.render(n.get_role(), False, (0, 0, 0))
    # screen.blit(text_surface, (0,0))


pygame.quit()
