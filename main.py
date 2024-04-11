import pygame
# NEEDS TO BE MOVED
# from chef_files.slicing_pizza import SlicingPizza
# from chef_files.adding_toppings import AddingToppings
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


# NEEDS TO BE MOVED
# # note: the '3' in the line below depends on user input for number of cuts (need to change this when putting everything together)
# chef_slicing_pizza = SlicingPizza(screen, 3, c)
# chef_adding_toppings = AddingToppings(screen, c)
# # variables for chef character - cutting pizza
# cutting_pizza = False
# x_org, y_org = None, None
# # variables for chef character - adding toppings
# adding_toppings = False
# topping = None
# chef_slicing_pizza.curr_toppings = []

# # start with adding toppings
# chef_adding_toppings.bg_to_toppings_board()

# # display whole pizza before the cutting process
# pizza_image = pygame.image.load("pictures/plain_pizza_pic.png")
# chef_adding_toppings.add_pizza_image(pizza_image, chef_adding_toppings.pizza_image_location)
# chef_adding_toppings.pizza_fly_in()


# oven_button_clicked = False
    
    


# NEEDS TO BE MOVED
# # note: the '3' in the line below depends on user input for number of cuts (need to change this when putting everything together)
# chef_slicing_pizza = SlicingPizza(screen, 3, c)
# chef_adding_toppings = AddingToppings(screen, c)
# # variables for chef character - cutting pizza
# cutting_pizza = False
# x_org, y_org = None, None
# # variables for chef character - adding toppings
# adding_toppings = False
# topping = None
# chef_slicing_pizza.curr_toppings = []

# # start with adding toppings
# chef_adding_toppings.bg_to_toppings_board()

# # display whole pizza before the cutting process
# pizza_image = pygame.image.load("pictures/plain_pizza_pic.png")
# chef_adding_toppings.add_pizza_image(pizza_image, chef_adding_toppings.pizza_image_location)
# chef_adding_toppings.pizza_fly_in()


# oven_button_clicked = False
    
    

# gameloop
while gameloop:
    # NEEDS TO BE MOVED
    # # create all necessary buttons for chef - later move this to the chef file since it won't work here
    # oven_button = pygame.Rect((550, 560, 105, 10))
    
    
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

            
        
        # # check for mouse clicks
        # elif event.type == pygame.MOUSEBUTTONDOWN:
            
        #     # check if the user is trying to cut the pizza
        #     if c.background_image == chef_slicing_pizza.background_image:
        #         cutting_pizza = True
        #         if x_org == None:
        #             x_org, y_org, = pygame.mouse.get_pos()
            
        #     # check if the user is trying to drag and drop toppings
        #     elif c.background_image == chef_adding_toppings.background_image:
        #         for topping_option in chef_adding_toppings.topping_boxes:
        #             if topping_option.rect.collidepoint(pygame.mouse.get_pos()):
        #                 adding_toppings = True
        #                 topping = topping_option
        #                 break
        
        # elif event.type == pygame.MOUSEBUTTONUP:
            
        #     # check if the user has finished making one cut on the pizza
        #     if x_org != None:
        #         chef_slicing_pizza.display_pizza_slices(x_org, y_org, pygame.mouse.get_pos())
        #         cutting_pizza = False
        #         x_org = None
            
        #     # check if the user is placing a topping on the pizza
        #     if adding_toppings:
        #         chef_slicing_pizza.curr_toppings.append((topping.one_topping_image, pygame.mouse.get_pos()))
        #         adding_toppings = False
        #         topping = None
                
        # # check if button has been clicked
        # elif not oven_button_clicked and oven_button.collidepoint(pygame.mouse.get_pos()):
        #     chef_slicing_pizza.bg_to_cutting_board()
        #     oven_button_clicked = True
            
            
        # # draw line when cutting pizza
        # if cutting_pizza:
        #     chef_slicing_pizza.display_cutting_line(x_org, y_org)
            
        # # drag the topping onto the pizza
        # if adding_toppings:
        #     topping.topping_follow_cursor(chef_slicing_pizza.curr_toppings)
        
    pygame.display.update()
    # n.send("hi")

    # print(n.get_role())

    # text_surface = my_font.render(n.get_role(), False, (0, 0, 0))
    # screen.blit(text_surface, (0,0))


pygame.quit()
