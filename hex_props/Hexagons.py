import math
import pygame
import time
from hex_props.hex_items import item_calls as calls

class Hex_node:
    def __init__(self, column:int, row:int, terrain_tuple=("1", "1"), map_size:tuple = (None, None)):
        self.q = column
        self.r = row
        self.terrain_tuple = terrain_tuple
        self.map_size = map_size
        self.image = self.load_image()
        self.even_dir = [(+1,  0), (+1, -1), (0, -1), (-1, 0), (-1, +1), (0, +1)]
        self.odd_dir = [(+1,  0), (+1, +1), (0, +1), (-1, 0), (-1, -1), (0, -1)]
        self.neighbors = self.get_neighbors()
        self.movement_cost = 1
        self.walkeble = True
        #self.land_bonus = self.get_land_bonus()
        

    def draw_terrain(self, screen, pos):
        """Draw the terrain image on the screen."""
        if self.image:
            screen.blit(self.image, pos)
        else:
            print(f"No image available for hex at ({self.q}, {self.r})")

    def load_image(self):
        """Use the terrain_tuple to call the appropriate image."""
        try:
            image_path = calls.call_img(self.terrain_tuple[0], self.terrain_tuple[1])
            #print(f"Loading image from: {image_path}")  # Debugging line
            image = pygame.image.load(image_path)
            #print(f"Image loaded successfully: {image_path}")  # Debugging line
            return image
        except pygame.error as e:
            print(f"Error loading image: {e}")
            return None
        
    def get_neighbors(self):

        if self.q % 2 == 0:  # Even column
            directions = self.even_dir
            
        else:  # Odd column
            directions = self.odd_dir
        
        neighbors = []
        for direction in directions:


            dq, dr = direction
            neighbor_q = self.q + dq
            neighbor_r = self.r + dr
            if (neighbor_q < 0 or neighbor_r < 0) or (neighbor_r == self.map_size[0] or neighbor_q == self.map_size[1]):
                continue
            neighbors.append((neighbor_q, neighbor_r))
        
        return neighbors
    '''
    def get_land_bonus(self):
        if self.terrain_tuple[1] == "1":
            if self.troop == musket:
                musket.self.attact_chance += (10/100)
            if self.troop == horse:
                horse.self.movement += 0.5
        if self.terrain_tuple[1] == "2":
            if self.troop == musket:
                musket.self.defence = (musket.self.defence/100 + 10/100)*100
            if self.troop == horse:
                horse.self.movement -= 1
        if self.terrain_tuple[1] == "3":
            if self.troop == cannon:
                cannon.self.range += 2
    '''


        

    
        

    

