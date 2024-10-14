import math
import pygame
import time
from hex_props.hex_items import item_calls as calls

class Hex_node:
    def __init__(self, column:int, row:int, terrain_tuple=("1", "1")):
        self.q = column
        self.r = row
        self.terrain_tuple = terrain_tuple
        self.image = self.load_image()

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
        
        

    
        

    

