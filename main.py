import math
import pygame
from hex_props.Hexagons import Hex_node

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

def draw_hex(surface, color, pos, hex_size):
    border_thickness = 2
    border_color = (0,0,0)
    points = []

    for i in range(6):

        angle = math.radians(60*i)

        point_x = pos[0] + hex_size * math.cos(angle)
        point_y = pos[1] + hex_size * math.sin(angle)

        points.append((point_x, point_y))
    pygame.draw.polygon(surface, color, points)
    
    for i in range(6):

        pygame.draw.line(surface, border_color, points[i], points[(i+1) % 6], border_thickness)

def draw_hex_grid(columns:int, rows:int):
    def_terrain_tuple = ("1", "1")
    def_hex_graph = {}

    for row in range(rows):

        for column in range(columns):
            x = x_start + (hex_offset_x)*column + (hex_offset_x*1/3)*column
            y = y_start + (hex_offset_y)*row

            if column % 2 == 1:
                y += hex_offset_y/2

            hex_pos = (x, y)
            draw_hex(screen, hex_color, hex_pos, hex_size)
            def_hex_graph[column, row] = Hex_node(column, row, def_terrain_tuple)

    return def_hex_graph

def axial_to_pixel(q, r):
    xy_coords = []
    x = x_start + (hex_offset_x)*q + (hex_offset_x*1/3)*q
    y = y_start + (hex_offset_y)*r

    if q % 2 == 1:
        y += hex_offset_y/2

    xy_coords.append((x, y))
    return xy_coords

run = True
rows = 2
columns = 2

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            
    screen.fill((255, 255, 255))
    a = draw_hex_grid(columns, rows)

    for q, r in a.keys():
        pos = axial_to_pixel(q, r)

        for map_object in a.values():
            Hex_node.draw_terrain(Hex_node, screen, pos)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
print(a)