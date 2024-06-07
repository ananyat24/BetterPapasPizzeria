import pygame
from chef_files.slicing_pizza import SlicingPizza
from chef_files.adding_toppings import AddingToppings
from constants import Constants
from chefOrderTicket import orderTicketFill

class Chef(): 
    # create the screen
    def __init__(self):
        pygame.init()
        self.c = Constants()
        
        # intialize all the variables
        self.gameloop = True
        # variables for chef character
        self.cutting_pizza = False
        
       
        self.oven_button_clicked = False

    def setup(self):
        self.screen = pygame.display.set_mode((self.c.screen_width, self.c.screen_height))
         # note: the 3 below depends on user input for number of cuts (need to change this when putting everything together)
        self.chef_slicing_pizza = SlicingPizza(self.screen, 3, self.c)
        self.chef_adding_toppings = AddingToppings(self.screen, self.c)

        # start with adding toppings
        self.chef_adding_toppings.bg_to_toppings_board()

        # display whole pizza before the cutting process
        pizza_image = pygame.image.load("pictures/plain_pizza_pic.png")
        self.chef_adding_toppings.add_pizza_image(pizza_image, self.chef_adding_toppings.pizza_image_location)
        self.chef_adding_toppings.pizza_fly_in()


    def run(self, n, data):   
        self.setup()
        data = {"stage": "in_level", "role": "chef", "to_send_to_chef": None, "to_send_to_waiter": None}
        data = n.send(data)
        print(data) # for testing can remove

        most_recent_ticket = data["to_send_to_chef"]
        # if(most_recent_ticket):
            #there is a ticket then do stuff with it here and uncomment this line

        # gameloop
        x_org, y_org = None, None
        while self.gameloop:
            
            # create all necessary buttons for chef - later move this to the chef file since it won't work here
            oven_button = pygame.Rect((550, 560, 105, 10))
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameloop = False
                    
                
                # check for mouse clicks
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                    # check if the user is trying to cut the pizza
                    if self.c.background_image == self.chef_slicing_pizza.background_image:
                        self.cutting_pizza = True
                        if x_org == None:
                            x_org, y_org, = pygame.mouse.get_pos()
                    
                    # check if the user is trying to drag and drop toppings
                    elif self.c.background_image == self.chef_adding_toppings.background_image:
                        pass
                
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    # check if the user has finished making one cut on the pizza
                    if x_org != None:
                        self.chef_slicing_pizza.display_pizza_slices(x_org, y_org, pygame.mouse.get_pos())
                        self.cutting_pizza = False
                        x_org = None
                        
                # check if button has been clicked
                elif not self.oven_button_clicked and oven_button.collidepoint(pygame.mouse.get_pos()):
                    self.chef_slicing_pizza.bg_to_cutting_board()
                    self.oven_button_clicked = True
                    
                    
                # draw line when cutting pizza
                if self.cutting_pizza:
                    self.chef_slicing_pizza.display_cutting_line(x_org, y_org)
                
                
            pygame.display.update()

        pygame.quit()