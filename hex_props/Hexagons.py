import math
import pygame
import time

class Hex_node:
    def __init__(self, q, r):
        self.q = q
        self.r = r
        self.neighbors = []

    

def draw_hex(surface, color, pos, size):

    BORDER_SIZE = 2

    BORDER_COLOR = (0,0,0)

    points = []

    for i in range(6):

        angle = math.radians(60*i)

        x_i = pos[0]+ size * math.cos(angle)
        y_i = pos[1]+ size * math.sin(angle)

        points.append((x_i, y_i))

    pygame.draw.polygon(surface, color, points)

    for i in range(6):

        pygame.draw.line(surface, BORDER_COLOR, points[i], points[(i+1) % 6], BORDER_SIZE)
    
def hex_to_pixel(q, r, size):
   
    x = size * (3/2) * q

    y = size * math.sqrt(3) * (r + 0.5 * (q % 2))

    return (x, y)

def pixel_to_hex(x, y, size):

    q = (2 / 3 * x) / size

    r = (-1 / 3 * x + math.sqrt(3) / 3 * y) / size

    return hex_round(q, r)


def hex_round(q, r):
    x = q
    z = r
    y = -x - z

    rx = round(x)
    ry = round(y)
    rz = round(z)

    x_diff = abs(rx - x)
    y_diff = abs(ry - y)
    z_diff = abs(rz - z)

    if x_diff > y_diff and x_diff > z_diff:
        rx = -ry - rz
    elif y_diff > z_diff:
        ry = -rx - rz
    else:
        rz = -rx - ry

    return (rx, rz)


def build_hex_graph(rows, cols):
    hex_graph = {}

    for r in range(rows):

        for q in range(cols):

            hex_graph[(q, r)] = Hex_node(q, r)

    return hex_graph

def draw_hex_grid(surface, hex_graph, size, highlight_hex=None):

    for (q, r), hex in hex_graph.items():

        center = hex_to_pixel(q, r, size)

        color = (0,0,255)

        if highlight_hex and (q, r) == highlight_hex:

            color = (255,0,0)

        draw_hex(surface, color, center, size)

pygame.init()

screen_setup = (800, 600)

hex_color = (0, 0, 255)

screen = pygame.display.set_mode(screen_setup)

clock = pygame.time.Clock()

hex_size = 20

rows = 2

cols = 2

hex_graph = build_hex_graph(rows, cols)

print(hex_graph)
run = True
while run:

    time.sleep(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255,255,255))

    mouse_pos = pygame.mouse.get_pos()

    highlight_hex = pixel_to_hex(mouse_pos[0], mouse_pos[1], hex_size)

    draw_hex_grid(screen, hex_graph, hex_size, highlight_hex)

    pygame.display.flip()

    clock.tick(60)


pygame.quit
