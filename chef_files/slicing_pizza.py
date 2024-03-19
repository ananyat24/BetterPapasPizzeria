import pygame
from chef_files.chef import Chef
from constants import Constants

class SlicingPizza(Chef):
    
    def __init__(self, screen:pygame.display, num_cuts:int):
        self.c = Constants() # get the constants        
        
        cutting_board_img = pygame.image.load("pictures/cutting_board.png")
        cutting_board_image = pygame.transform.scale(cutting_board_img, (self.c.screen_width, self.c.screen_height))
        
        self.number_cuts_left = num_cuts
        
        super().__init__(screen, cutting_board_image)
    
    
    # show the line when cutting the pizza
    def display_cutting_line(self, x_org:int, y_org:int):
        x_fin, y_fin = pygame.mouse.get_pos()
        if x_org != x_fin:
            # check if all slices have already been cut
            if self.number_cuts_left > 0:
                # before drawing the line, erase any lines that may have existed before
                self.display_current_pizza()
                # draw dashed line
                dash_length = int((x_fin - x_org)/15)
                slope = (y_fin - y_org) / (x_fin - x_org)
                b = y_org - slope * x_org
                for i in range(1, 16, 2):
                    x_start = x_org + (i-1) * dash_length
                    y_start = int(x_start * slope) + b
                    x_fin = x_start + dash_length
                    y_fin = int(x_fin * slope) + b
                    pygame.draw.line(self.screen, (195,177,225), (x_start, y_start), (x_fin, y_fin), 8)
    
    
    # show the cut pizza slices
    def display_pizza_slices(self, x_org:int, y_org:int, curr_pos:tuple):
        # check if all slices have already been cut
        if self.number_cuts_left > 0:
            x_curr = curr_pos[0]
            y_curr = curr_pos[1]
            # ensure that the line does not extend past the pizza
            height = self.pizza_image.get_height()
            width = self.pizza_image.get_width()
            if x_org < self.pizza_image_location[0]:
                x_org = self.pizza_image_location[0]
            elif x_org > self.pizza_image_location[0] + width:
                x_org = self.pizza_image_location[0] + width
            if x_curr < self.pizza_image_location[0]:
                x_curr = self.pizza_image_location[0]
            elif x_curr > self.pizza_image_location[0] + width:
                x_curr = self.pizza_image_location[0] + width
            if y_org < self.pizza_image_location[1]:
                y_org = self.pizza_image_location[1]
            elif y_org > self.pizza_image_location[1] + height:
                y_org = self.pizza_image_location[1] + height
            if y_curr < self.pizza_image_location[1]:
                y_curr = self.pizza_image_location[1]
            elif y_curr > self.pizza_image_location[1] + height:
                y_curr = self.pizza_image_location[1] + height
            # "erase" the purple cutting line
            self.display_current_pizza()
            # draw a line so that it looks like the pizza has been cut
            self.draw_line_slowly((207,212,215), x_org, y_org, x_curr, y_curr, 8)
            self.lines.append((self.screen, (207,212,215), (x_org, y_org), (x_curr, y_curr), 8))
    
    
    # drawing the pizza cut line slowly instead of all at once
    def draw_line_slowly(self, color, x_org, y_org, x_fin, y_fin, width):
        if x_org != x_fin:
            interval = (x_fin - x_org)/10
            slope = (y_fin - y_org) / (x_fin - x_org)
            b = y_org - slope * x_org
            for i in range(10):
                x_start = x_org + (i) * interval
                y_start = x_start * slope + b
                x_end = x_start + interval
                y_end = x_end * slope + b
                pygame.draw.line(self.screen, color, (x_start, y_start), (x_end, y_end), width)
                pygame.display.update()
                pygame.time.wait(50)
            # since 1 cut has been made, decrease the number of cuts left by 1
            self.number_cuts_left -= 1
            
            
    # have the pizza fly in before the cutting process starts
    def pizza_fly_in(self):
        final_x_coor = self.pizza_image_location[0]
        for x_coor in range(0, final_x_coor, 20):
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.pizza_image, (x_coor, self.pizza_image_location[1]))
            pygame.display.update()
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.pizza_image, (final_x_coor, self.pizza_image_location[1]))
            