import pygame
from chef_files.slicing_pizza import SlicingPizza
from constants import Constants

# create the screen
pygame.init()
c = Constants()
screen = pygame.display.set_mode((c.screen_width, c.screen_height))
    
# intialize all the variables
gameloop = True
# variables for chef character
cutting_pizza = False
x_org, y_org = None, None
chef_slicing_pizza = SlicingPizza(screen, 3, c)

# display whole pizza before the cutting process
pizza_image = pygame.image.load("pictures/plain_pizza_pic.png")
chef_slicing_pizza.add_pizza_image(pizza_image, (150, 175))
chef_slicing_pizza.pizza_fly_in()

# gameloop 
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        
        # draw a line based on mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cutting_pizza = True
            if x_org == None:
                x_org, y_org, = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            chef_slicing_pizza.display_pizza_slices(x_org, y_org, pygame.mouse.get_pos())
            cutting_pizza = False
            x_org = None
            
        # draw line when cutting pizza
        if cutting_pizza:
            chef_slicing_pizza.display_cutting_line(x_org, y_org)
        
    pygame.display.update()

pygame.quit()
