import pygame
import os
import sys
import time
import random

class Player:

    directions = {"left":(-12,0), "right":(12,0), "up":(0,-12), "down":(0,12)}

    def __init__(self, username: str, sprite_sheet:str, start_x, start_y):
        self.spritesheet = pygame.image.load(os.path.join("Images", "joyspritesheet1"))
        self.spritesheet=pygame.transform.scale(self.spritesheet, (576, 192))
        
        #frame of spritesheet player is currently using
        self.current_frame = 0
        #splits standard spritesheet
        self.spritesheet_frames = [self.spritesheet.subsurface((i * (self.spritesheet.get_width() // 4), 0, self.spritesheet.get_width() // 4, self.spritesheet.get_height())) for i in range(4)]
        self.player_rectangle=self.spritesheet_frames[self.current_frame].get_rect()
        self.player_rectangle.topleft = (start_x, start_y)
        #defines variables for animation
        self.flipped = False
        self.lastup = None
        self.lastleft = None
        self.direction = None
        self.framegap = 10

    def handlemove(self, direction, framecounter, firstchange): 
        if self.is_paralyzed:
            return
        if self.attacking: 
            return
        self.direction = direction
        if self.direction == None:
            return
        elif self.direction == "left":
            if framecounter % self.framegap == 0 or firstchange:
                if self.current_frame != 10:
                    self.current_frame = 10
                else:
                    if self.lastleft == 13:
                        self.current_frame = 16
                        self.lastleft = 16
                    else:
                        self.current_frame = 13
                        self.lastleft = 13
                if self.flipped:
                    self.spritesheet_frames = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_frames]
                    self.spritesheet_dframes = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_dframes]
                    self.spritesheet_aframes = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_aframes]
                    self.spritesheet_adframes = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_adframes]
                    self.flipped = False
        elif self.direction == "right":
            if framecounter % self.framegap == 0 or firstchange:
                if self.current_frame != 10:
                    self.current_frame = 10
                else:
                    if self.lastleft == 13:
                        self.current_frame = 16
                        self.lastleft = 16
                    else:
                        self.current_frame = 13
                        self.lastleft = 13
                if not self.flipped:
                    self.spritesheet_frames = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_frames]
                    self.spritesheet_dframes = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_dframes]
                    self.spritesheet_aframes = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_aframes]
                    self.spritesheet_adframes = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_adframes]
                    self.flipped = True
        elif self.direction == "up":
            if framecounter % self.framegap == 0 or firstchange:
                if self.lastup == 14:
                    self.current_frame = 17
                    self.lastup = 17
                else:
                    self.current_frame = 14
                    self.lastup = 14
        else:
            if framecounter % self.framegap == 0 or firstchange:
                if self.lastup == 12:
                    self.current_frame = 15
                    self.lastup = 15
                else:
                    self.current_frame = 12
                    self.lastup = 12
        
        self.player_rectangle.move_ip(self.directions[self.direction][0], self.directions[self.direction][1])
        