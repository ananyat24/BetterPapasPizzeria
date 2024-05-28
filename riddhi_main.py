import pygame
from chef_files.slicing_pizza import SlicingPizza
from constants import Constants
from Player import *

# create the screen
pygame.init()
c = Constants()
screen = pygame.display.set_mode((c.screen_width, c.screen_height))
    
# intialize all the variables
#adds gameloop variable and direction variable to keep track of player movement
gameloop = True
direction = None
direction_for_collision = None
framecounter = 0
firstchange = False

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

        #test customer sprite
        sprite1 = Player("medha", "joyspritesheet1", 100, 100)
        sprite1.player_rectangle.topleft = (750, 700)

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                    direction_for_collision = "right"

                if event.key == pygame.K_LEFT:
                    direction = "left"
                    direction_for_collision = "left"

                if event.key == pygame.K_DOWN:
                    direction = "down"
                    direction_for_collision = "down"

                if event.key == pygame.K_UP:
                    direction = "up"
                    direction_for_collision = "up"

        #stops movement if key is released - sets direction to None
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                sprite1.current_frame = 10
                direction = None
            elif event.key == pygame.K_UP:
                sprite1.current_frame = 11
                direction = None
            elif event.key == pygame.K_DOWN:
                sprite1.current_frame = 9
                direction = None

        if event.type == pygame.QUIT:
                    gameLoop=False
                    pygame.quit()
                    sys.exit()
                
        sprite1.handlemove(direction, framecounter, firstchange)
        
    pygame.display.update()


pygame.quit()