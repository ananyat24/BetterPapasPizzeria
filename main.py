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

data = {"stage":"intro", "key": None, "role": None, "remaining_roles": ["waiter", "chef"]}

# gameloop
while gameloop:
    




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    if data["stage"] == "intro":
        height = 50
        # if data["role"] == None:
        for role in data["remaining_roles"]:  
            #print(role)  
            txtsurf = my_font.render(role, True, (255, 255, 255))
            screen.blit(txtsurf,(30, height))
            height += 100

        # elif data["role"] == "chef":
        #     txtsurf = my_font.render("waiter", True, (255, 255, 255))
        #     screen.blit(txtsurf,(30, 50))
        #     height += 100

        # elif data["role"] == "waiter":
        #     txtsurf = my_font.render("chef", True, (255, 255, 255))
        #     screen.blit(txtsurf,(30, 150))
        #     height += 100

        pygame.display.update()
        height = 50
        # if data["role"] == None:
        for role in data["remaining_roles"]:  
            #print(role)  
            txtsurf = my_font.render(role, True, (255, 255, 255))
            screen.blit(txtsurf,(30, height))
            height += 100

        # elif data["role"] == "chef":
        #     txtsurf = my_font.render("waiter", True, (255, 255, 255))
        #     screen.blit(txtsurf,(30, 50))
        #     height += 100

        # elif data["role"] == "waiter":
        #     txtsurf = my_font.render("chef", True, (255, 255, 255))
        #     screen.blit(txtsurf,(30, 150))
        #     height += 100

        pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if data["key"] != "left":
                    data["remaining_roles"] = ["waiter", "chef"]
                    data["key"] = "left"
                    # print(data)
                    data = n.send(data)
                    # print("#2: ")
                    #print(data)
                if data["key"] != "left":
                    data["remaining_roles"] = ["waiter", "chef"]
                    data["key"] = "left"
                    # print(data)
                    data = n.send(data)
                    # print("#2: ")
                    #print(data)
            if event.key == pygame.K_RIGHT:
                if data["key"] != "right":
                    data["remaining_roles"] = ["waiter", "chef"]
                    data["key"] = "right"
                    data = n.send(data)
            if event.key == pygame.K_UP:
                data["key"] = "up"
                if data["key"] != "right":
                    data["remaining_roles"] = ["waiter", "chef"]
                    data["key"] = "right"
                    data = n.send(data)
            if event.key == pygame.K_UP:
                data["key"] = "up"
                data = n.send(data)
        


    elif data["stage"] == "waiter1":
            waiter.run()

    elif data["stage"] == "chef1":
            chef.run()
    else:
        screen.blit(homescreen_image, (0, 0))
        pygame.display.update()
    # n.send("hi")

    # print(n.get_role())

    # text_surface = my_font.render(n.get_role(), False, (0, 0, 0))
    # screen.blit(text_surface, (0,0))



pygame.quit()
