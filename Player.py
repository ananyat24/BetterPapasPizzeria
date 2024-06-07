import pygame
import os
import sys
import time
import random

class Player:

    directions = {"left":(-12,0), "right":(12,0), "up":(0,-12), "down":(0,12)}


    def __init__(self, username: str, sprite_sheet:str, start_x, start_y):
        self.spritesheet = pygame.image.load(os.path.join("Images", "joyspritesheet1.png"))
        self.spritesheet=pygame.transform.scale(self.spritesheet, (409, 183))
        self.spritesheet_frames = [self.spritesheet.subsurface((i * (self.spritesheet.get_width() // 4), 0, self.spritesheet.get_width() // 4, self.spritesheet.get_height())) for i in range(4)]
        self.player_rectangle=self.spritesheet_frames[self.current_frame].get_rect()
        self.player_rectangle.topleft.x = start_x
        self.player_rectangle.topleft.y = start_y
        self.flipped = False
        #frame of spritesheet player is currently using
        self.current_frame = 0
        self.direction = None
        self.framegap = 10
        self.action = ""
        self.curr_sheet = None
        self.order = None
   
   #joythumbsup

    def npc_action(self, action:str): 
        self.action = action
        if self.action == "allan_angry":
            self.spritesheet = pygame.image.load(os.path.join("Images", "allanspritesheet_angry.png"))
            self.spritesheet=pygame.transform.scale(self.spritesheet, (1105, 206))
            self.spritesheet_frames = [self.spritesheet.subsurface((i * (self.spritesheet.get_width() // 5), 0, self.spritesheet.get_width() // 5, self.spritesheet.get_height())) for i in range(5)]
            self.current_sheet = self.spritesheet_frames
            for i in range(len(self.spritesheet_frames)):
                self.current_frame = self.curr_sheet[i]

        if self.action == "allan_happy":
            self.spritesheet = pygame.image.load(os.path.join("Images", "allanspritesheet_thumbs up.png"))
            self.spritesheet=pygame.transform.scale(self.spritesheet, (1058, 217))
            self.spritesheet_frames = [self.spritesheet.subsurface((i * (self.spritesheet.get_width() // 5), 0, self.spritesheet.get_width() // 5, self.spritesheet.get_height())) for i in range(5)]
            self.current_sheet = self.spritesheet_frames
            for i in range(len(self.spritesheet_frames)):
                self.current_frame = self.curr_sheet[i]

        
        if self.action == "joy_taking_order":
            self.spritesheet = pygame.image.load(os.path.join("Images", "joyspritesheet3.png"))
            self.spritesheet=pygame.transform.scale(self.spritesheet, (954, 161))
            self.spritesheet_frames = [self.spritesheet.subsurface((i * (self.spritesheet.get_width() // 5), 0, self.spritesheet.get_width() // 5, self.spritesheet.get_height())) for i in range(5)]
            self.current_sheet = self.spritesheet_frames
            for i in range(len(self.spritesheet_frames)):
                self.current_frame = self.curr_sheet[i]

        if self.action == "joy_happy":
            self.spritesheet = pygame.image.load(os.path.join("Images", "joyspritesheet2.png"))
            self.spritesheet=pygame.transform.scale(self.spritesheet, (1661, 195))
            self.spritesheet_frames = [self.spritesheet.subsurface((i * (self.spritesheet.get_width() // 7), 0, self.spritesheet.get_width() // 7, self.spritesheet.get_height())) for i in range(7)]
            self.current_sheet = self.spritesheet_frames
            for i in range(len(self.spritesheet_frames)):
                self.current_frame = self.curr_sheet[i]
        
        if self.action == "joy_smiling":
            self.spritesheet = pygame.image.load(os.path.join("Images", "joyspritesheet1.png"))
            self.spritesheet=pygame.transform.scale(self.spritesheet, (409, 183))
            self.spritesheet_frames = [self.spritesheet.subsurface((i * (self.spritesheet.get_width() // 4), 0, self.spritesheet.get_width() // 4, self.spritesheet.get_height())) for i in range(4)]
            self.current_sheet = self.spritesheet_frames
            for i in range(len(self.spritesheet_frames)):
                self.current_frame = self.curr_sheet[i]

        if self.action == "bertha_smiling":
            self.spritesheet = pygame.image.load(os.path.join("Images", "berthaspritesheet_happy.png"))
            self.spritesheet=pygame.transform.scale(self.spritesheet, (409, 183))
            self.spritesheet_frames = [self.spritesheet.subsurface((i * (self.spritesheet.get_width() // 4), 0, self.spritesheet.get_width() // 4, self.spritesheet.get_height())) for i in range(4)]
            self.current_sheet = self.spritesheet_frames
            for i in range(len(self.spritesheet_frames)):
                self.current_frame = self.curr_sheet[i]
        
        if self.action == "bertha_angry":
            self.spritesheet = pygame.image.load(os.path.join("Images", "berthaspritesheet_angry.png"))
            self.spritesheet=pygame.transform.scale(self.spritesheet, (409, 183))
            self.spritesheet_frames = [self.spritesheet.subsurface((i * (self.spritesheet.get_width() // 6), 0, self.spritesheet.get_width() // 6, self.spritesheet.get_height())) for i in range(6)]
            self.current_sheet = self.spritesheet_frames
            for i in range(len(self.spritesheet_frames)):
                self.current_frame = self.curr_sheet[i] 

        if self.action == "bertha_walking":
            self.spritesheet = pygame.image.load(os.path.join("Images", "berthaspritesheet_standing.png"))
            self.spritesheet=pygame.transform.scale(self.spritesheet, (118, 212))
            self.current_sheet = self.spritesheet






        # self.direction = direction
        # if self.direction == None:
        #     return
        # elif self.direction == "left":
        #     if framecounter % self.framegap == 0 or firstchange:
        #         if self.current_frame != 10:
        #             self.current_frame = 10
    