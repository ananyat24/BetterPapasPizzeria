import pygame
from chef_files.slicing_pizza import SlicingPizza
from chef_files.adding_toppings import AddingToppings
from chef_files.oven import Oven
from constants import Constants
from chefOrderTicket import orderTicketFill

class Chef(): 
    # create the screen
    def __init__(self):
        pygame.init()
        
        # intialize all the variables
        self.gameloop = True
        self.c = Constants()
        
        # variables for cutting pizza
        self.cutting_pizza = False
        self.x_org, self.y_org = None, None
        
        # variables for adding toppings
        self.adding_toppings = False
        self.topping = None
        
        # variables for baking pizza
        self.oven_button_clicked = False
        
        # setup data network for connection between chef and waiter
        self.data = {"stage": "in_level", "role": "chef", "to_send_to_chef": None, "to_send_to_waiter": None}
        
        self.num_cuts = 0
        
        self.run()
        

    def setup(self):
        self.screen = pygame.display.set_mode((self.c.screen_width, self.c.screen_height))
        
        # fill out the order ticket
        self.order_ticket = orderTicketFill(self.screen)
        
        # note: the 3 below depends on user input for number of cuts (need to change this when putting everything together)
        self.chef_slicing_pizza = SlicingPizza(self.screen, self.num_cuts, self.c, self.order_ticket)
        
        self.chef_adding_toppings = AddingToppings(self.screen, self.c)
        self.chef_oven = Oven(self.screen, self.c)

        # start with adding toppings
        self.chef_adding_toppings.bg_to_toppings_board()
        self.c.curr_screen_name = "toppings"

        # display whole pizza before the cutting process
        pizza_image = pygame.image.load("pictures/plain_pizza_pic.png")
        self.chef_adding_toppings.add_pizza_image(pizza_image, self.chef_adding_toppings.pizza_image_location)
        self.chef_adding_toppings.pizza_fly_in()
        
        # initialize the buttons on the bottom of each screen
        self.left_middle_button = pygame.Rect((450, 690, 70, 220))
        self.right_middle_button = pygame.Rect((720, 695, 70, 220))
        
        # oven button
        self.oven_clock_button = pygame.Rect((130, 110, int(self.c.screen_width/2) - 200, 550))


    def run(self):   
        self.setup()
        
        self.order_ticket.run()
        
        self.chef_slicing_pizza.number_cuts_left = self.c.VALUES_JSON["CUTS"]

        # gameloop
        while self.gameloop:
            
            """
            self.data = n.send(self.data)
            most_recent_ticket = self.data["to_send_to_chef"]
            
            # if there is a ticket, display it on the chef screen
            if(most_recent_ticket):
                self.c.VALUES_JSON = most_recent_ticket
                self.order_ticket.run()
                
            """
            
            for event in pygame.event.get():
                
                if self.c.curr_screen_name != "satisfaction":
                    self.order_ticket.run()
                
                if event.type == pygame.QUIT:
                    self.gameloop = False
                    
                
                # check for mouse clicks
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                    # check if the user is trying to cut the pizza
                    if self.c.background_image == self.chef_slicing_pizza.background_image:
                        self.cutting_pizza = True
                        if self.x_org == None:
                            self.x_org, self.y_org, = pygame.mouse.get_pos()
                    
                    # check if the user is trying to drag and drop toppings
                    elif self.c.background_image == self.chef_adding_toppings.background_image:
                        for topping_option in self.chef_adding_toppings.topping_boxes:
                            if topping_option.rect.collidepoint(pygame.mouse.get_pos()):
                                self.adding_toppings = True
                                self.topping = topping_option
                                break
                            
                    """
                    # check if the user is trying to stop the clock
                    elif self.c.background_image == self.chef_oven.background_image:
                        if self.oven_clock_button.collidepoint(pygame.mouse.get_pos()):
                            self.chef_oven.clock_stopped = True
                            self.chef_slicing_pizza.bg_to_cutting_board()
                    """
                
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    # check if the user has finished making one cut on the pizza
                    if self.x_org != None:
                        self.chef_slicing_pizza.display_pizza_slices(self.x_org, self.y_org, pygame.mouse.get_pos())
                        self.cutting_pizza = False
                        self.x_org = None
                        if self.chef_slicing_pizza.number_cuts_left == 0:
                            self.c.curr_screen_name == "satisfaction"
                            self.chef_slicing_pizza.satisfaction_score.bg_to_complete_pizza()
                    
                    # check if the user is placing a topping on the pizza
                    if self.adding_toppings:
                        self.c.toppings.append((self.topping.one_topping_image, pygame.mouse.get_pos()))
                        self.adding_toppings = False
                        self.topping = None
                        
                        
                # check if buttons for switching screens have been clicked
                elif self.left_middle_button.collidepoint(pygame.mouse.get_pos()):
                    if self.c.curr_screen_name == "toppings" or self.c.curr_screen_name == "oven":
                        self.c.curr_screen_name = "cutting"
                        self.chef_slicing_pizza.bg_to_cutting_board()
                    elif self.c.curr_screen_name == "cutting":
                        self.c.curr_screen_name = "toppings"
                        self.chef_adding_toppings.bg_to_toppings_board()
                        self.chef_adding_toppings.pizza_fly_in()
                    else:
                        if self.left_middle_button.collidepoint(pygame.mouse.get_pos()):
                            self.chef_slicing_pizza.satisfaction_score.display_satisfaction_score()
                elif self.right_middle_button.collidepoint(pygame.mouse.get_pos()):
                    if self.c.curr_screen_name == "oven":
                        self.c.curr_screen_name = "toppings"
                        self.chef_adding_toppings.bg_to_toppings_board()
                        self.chef_adding_toppings.pizza_fly_in()
                    else:
                        self.c.curr_screen_name = "oven"
                        self.chef_oven.bg_to_oven()
                    
                    
                # draw line when cutting pizza
                if self.cutting_pizza:
                    self.chef_slicing_pizza.display_cutting_line(self.x_org, self.y_org, self.order_ticket)
                
                
                # drag the topping onto the pizza
                if self.adding_toppings:
                    self.topping.topping_follow_cursor(self.c.toppings, self.order_ticket)
                    
                
                # stop the clock if needed
                if self.chef_oven.clock_stopped:
                    pygame.time.wait(500)
                    self.chef_slicing_pizza.bg_to_cutting_board()
                
                
            pygame.display.update()

        pygame.quit()
        
        
chef = Chef()