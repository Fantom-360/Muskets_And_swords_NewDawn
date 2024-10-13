import math
import pygame
import time
from hex_props.hex_items import item_calls as calls

class Hex_node:
    def __init__(self, column:int, row:int, level_props:tuple):
        self.q = column
        self.r = row
        self.season, self.land_type = level_props[0], level_props[1]
        self.image = calls.call_img(self.season, self.land_type)

    def draw_terrain(self, screen, pos):
        screen.blit(self.image, pos)

    
        

    
        

    

