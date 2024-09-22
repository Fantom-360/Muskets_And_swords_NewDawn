import math
import pygame

class Hex_node:
    def __init__(self, q, r):
        self.q = q
        self.r = r
        self.neighbors = []

    def add_neightbor(self, neighbor_hex):

        self.neighbors.append(neighbor_hex)

def draw_hex(surface, color, pos, size):

    BORDER_SIZE = 2

    BORDER_COLOR = (0,0,0)

    points = []

    for i in range(6):

        angle = math.radians(60*i)

        x_i = pos[0] + size * math.cos(angle)
        y_i = pos[1] + size * math.sin(angle)

        points.append((x_i, y_i))

    pygame.draw.polygon(surface, color, points)

    for i in range(6):

        pygame.draw.line(surface, BORDER_COLOR, points[i], points[(i+1) % 6], BORDER_SIZE)
    
def axial_to_pixel(q, r, size):
    width = math.sqrt(3) * size
    height = 2 * size
    x = size * (3/2) * q
    y = width * (r + 0.5 *(q % 2))

    return (x, y)

def pixel_to_axial(x, y, size):
    q = (2/3 * x) / size
    r = (-1/3 * x + math.sqrt(3)/3*y) / size

    return hex_round

def build_hex_graph(rows, cols):
    hex_graph = {}

    for r in range(rows):

        for q in range(cols):

            hex_graph[(q, r)] = Hex_node(q, r)

    return hex_graph

def draw_hex_grid(surface, hex_graph, size):

    for (q, r), hexagon in hex_graph.items():

        center = axial_to_pixel(q, r, size)

        draw_hex(surface, (0,0,255), center, size)


pygame.init()

screen_setup = (800, 600)

hex_color = (0, 0, 255)

screen = pygame.display.set_mode(screen_setup)

hex_size = 30

rows = 2

cols = 5

hex_graph = build_hex_graph(rows, cols)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False







    screen.fill((255,255,255))



    draw_hex_grid(screen, hex_graph, hex_size)

    pygame.display.flip()

pygame.quit