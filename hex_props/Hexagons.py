import math
import pygame
import time

class Hex_node:
    def __init__(self, column:int, row:int, level_props:tuple):
        self.q = column
        self.r = row
        self.neighbors = []
        self.season, self.land_type = level_props[0], level_props[1]
        

    def draw_terrain(self):
        

    

