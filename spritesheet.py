
import pygame
import os
import sys
import time
import random

class spritesheet:
    def __init__(self, filename, py, tw, th, tiles):
        self.sheet = pygame.image.load(filename).convert_alpha()

        self.py = py
        self.tw = tw
        self.th = th
        self.totalCellCount = tiles

        self.rect = self.sheet.get_rect()
        w, h = tw, th
        hw, hh = self.cellCenter = (w / 2, h / 2)

        self.cells = [(1+i*tw, self.py, tw-1, th-1) for i in range(tiles)]
        self.handle = list([
            (0,0), (-hw, 0), (-w, 0),
            (0, -hh), (-hw, -hh), (-w, -hh),
            (0, -h), (-hw, -h), (-w, -h),])

s = spritesheet('Number18.png', 1085, 80, 134, 8)

def draw(self, surface, cellIndex, x, y, handle = 0):
    hdl = self.handle[handle]
    surface.blit(self.sheet, (x + hdl[0], y + hdl[1]), area=self.cells[cellIndex])