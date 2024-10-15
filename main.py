import math
import pygame
import pygame.gfxdraw
from hex_props.Hexagons import Hex_node
from Levels.level1 import level_1

pygame.init()
screen_setup = (900, 600)
hex_color = (0, 0, 255)
screen = pygame.display.set_mode(screen_setup)
clock = pygame.time.Clock()
hex_size = 30
hex_width = 3/2 * hex_size
hex_height = math.sqrt(3) * hex_size
hex_offset_x = 3/4 * hex_width
hex_offset_y = hex_height
x_start = 50
y_start = 50

def draw_Hex_with_Terrain(surface, pos, hex_node:Hex_node):
    border_thickness = 2
    border_color = (0,0,0)
    points = []

    for i in range(6):

        angle = math.radians(60*i)

        point_x = pos[0] + hex_size * math.cos(angle)
        point_y = pos[1] + hex_size * math.sin(angle)

        points.append((point_x, point_y))

    pygame.gfxdraw.textured_polygon(surface, points, hex_node.image,hex_size*-1, hex_size*-1)

    #pygame.draw.polygon(surface, (0,0,0), points, 2)

    #rect_surface = pygame.surface(a.width, a.height)

    #hex_node.draw_terrain(surface, (pos[0] - hex_size, pos[1] - hex_size))

    for i in range(6):

        pygame.draw.line(surface, border_color, points[i], points[(i+1) % 6], border_thickness)

def create_hex_grid(columns:int, rows:int):
    """Create the hexagon grid and corresponding Hex_node instances."""
    def_terrain_tuple = ("1", "1")
    def_hex_graph = {}

    for row in range(rows):
        for column in range(columns):
            hex_node = Hex_node(column, row, def_terrain_tuple)
            def_hex_graph[(column, row)] = hex_node

    return def_hex_graph

def axial_to_pixel(axial_coords:tuple):
    """ (columns, rows) """
    
    x = x_start + (hex_offset_x)*axial_coords[0] + (hex_offset_x/3)*axial_coords[0]
    y = y_start + (hex_offset_y)*axial_coords[1]

    if axial_coords[0] % 2 == 1:
        y += hex_offset_y/2

    xy_coords = (x, y)
    return xy_coords

run = True
rows = 2
columns = 2

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    hex_graph = create_hex_grid(columns, rows)
    hex_graph.update(level_1)
            
    for key, value in hex_graph.items():
        hex_pos = axial_to_pixel(key)
        draw_Hex_with_Terrain(screen, hex_pos, value)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()



