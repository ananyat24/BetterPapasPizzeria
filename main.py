import pygame
from constants import Constants
from network import Network
from order_options import orderOptions
from chef_main import Chef
import os
from intro import run

# create the screen
pygame.init()
pygame.font.init()
pygame.font.init() 
c = Constants()
screen = pygame.display.set_mode((c.screen_width, c.screen_height))
homescreen_image = pygame.image.load("background images/Homescreen.png")
role_selection_us = pygame.image.load("background images/role_selection_bg.png") # background image for when no characters have been selected
role_selection_ch = pygame.image.load("background images/role_selection_bg_chef.png") # background image for when waiter has been selected
role_selection_wa = pygame.image.load("background images/role_selection_bg_waiter.png") # background image for when chef has been selected
waiter = orderOptions()
chef = Chef()


intro_begin_btn = pygame.Rect(475, 425, 410, 80)
intro_settings_btn = pygame.Rect(475, 550, 410, 80)
intro_tutorial_btn = pygame.Rect(475, 670, 410, 80)
intro_instructions_btn = pygame.Rect(475, 255, 200, 200)
instr_continue_btn = pygame.Rect(695, 1280, 300, 300)

selection_chef_btn = pygame.Rect(1010, 650, 260, 100)
selection_waiter_btn = pygame.Rect(105, 650, 260, 100)
selection_continue_btn = pygame.Rect(510, 340, 360, 130)




# intialize all the variables
gameloop = True



my_font = pygame.font.SysFont('Comic Sans MS', 30)
n = Network()
n.connect()

data = {"stage":"intro", "key": None, "role": None, "remaining_roles": ["waiter", "chef"], "to_send_to_chef": None, "to_send_to_waiter": None}
cur_screen = "unselected"

# gameloop
while gameloop:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

        # if data["stage"] == "instructions":
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if instr_continue_btn.collidepoint(pygame.mouse.get_pos()):
        #             data["stage"] = "intro"
        #     pygame.display.update()

        if data["stage"] == "intro":
            
            screen.blit(homescreen_image, (0,0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if intro_tutorial_btn.collidepoint(pygame.mouse.get_pos()):
                    data["stage"] = "instructions"
                    run()
                    data["stage"] = "intro"
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if intro_begin_btn.collidepoint(pygame.mouse.get_pos()):
                    data["stage"] = "selection"
            pygame.display.update()


        elif data["stage"] == "selection":
            

            if cur_screen == "unselected":
                screen.blit(role_selection_us, (0,0))

            elif cur_screen == "waiter_selected":
                    screen.blit(role_selection_wa, (0,0))
                   
            else:
                    screen.blit(role_selection_ch, (0,0))
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selection_chef_btn.collidepoint(pygame.mouse.get_pos()):
                    
                    data["key"] = "right"
                    data = n.send(data)
                    if data["role"] == "chef":
                         cur_screen = "chef_selected"

                    print(data)
                

                if selection_waiter_btn.collidepoint(pygame.mouse.get_pos()):
                    data["key"] = "left"
                    data = n.send(data)
                    if data["role"] == "waiter":
                         cur_screen = "waiter_selected"
                    

                    print(data)
                    
                if selection_continue_btn.collidepoint(pygame.mouse.get_pos()):
                    data["key"] = "continue"
                    print("Continue selected")
                    print(data["role"])
                    data = n.send(data)
                    print(data["stage"])

            pygame.display.update()

        elif data["stage"] == "waiter1":
                waiter.run(n, data)

        elif data["stage"] == "chef1":
                chef.run(n, data)
        else:
            screen.blit(homescreen_image, (0, 0))
            pygame.display.update()


pygame.quit()
