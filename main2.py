import math
import pygame

pygame.init()

screen_setup = (800, 600)

hex_color = (0, 0, 255)

screen = pygame.display.set_mode(screen_setup)

clock = pygame.time.Clock()

#basic hex parameter

hex_size = 30
hex_width = 3/2 * hex_size
hex_height = math.sqrt(3) * hex_size

#hex offsets for flat top hexes and for [grid]

hex_offset_x = 3/4 * hex_width
hex_offset_y = hex_height

x_start = 50
y_start = 50

def draw_hex(surface, color, pos, hex_size):

    #border setings

    border_thickness = 3
    border_color = (0,0,0)

    #main logic part for drawing hexagons

    points = []

    for i in range(6):

        angle = math.radians(60*i)

        point_x = pos[0] + hex_size * math.cos(angle)
        point_y = pos[1] + hex_size * math.sin(angle)

        points.append((point_x, point_y))

    pygame.draw.polygon(surface, color, points)

    #drawing a border on hexagon

    for i in range(6):

        pygame.draw.line(surface, border_color, points[i], points[(i+1) % 6], border_thickness)

x_hex_down = x_start + hex_offset_x/2 + hex_size
y_hex_down = y_start + hex_offset_y/2
x_hex_far_left = x_start + hex_size * 3

pos1 = (x_start, y_start)
pos2 = (x_hex_down, y_hex_down)
pos4 = (x_hex_far_left, y_start)
pos3 = (pos1[0], pos1[1]+ hex_offset_y)
pos5 = (pos2[0], pos2[1]+ hex_offset_y)
pos6 = (pos4[0], pos4[1]+ hex_offset_y)

run = True

rows = 5
columns = 5

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False
        
    screen.fill((255, 255, 255))
    '''
    draw_hex(screen, hex_color, pos1, hex_size) 
    draw_hex(screen, hex_color, pos2, hex_size)
    draw_hex(screen, hex_color, pos4, hex_size)
    draw_hex(screen, hex_color, pos3, hex_size)
    draw_hex(screen, hex_color, pos5, hex_size)
    draw_hex(screen, hex_color, pos6, hex_size)
    '''
    for row in range(rows):

        for column in range(columns):

            x = x_start + (hex_size*column) + (hex_offset_x*column)/2
            y = y_start + (hex_height*row)/2 + (hex_offset_y*row)/2

            if column % 2 == 1:

                y += hex_offset_y/2

            hex_pos = (x, y)

            draw_hex(screen, hex_color, hex_pos, hex_size)
       

    pygame.display.flip()

    clock.tick(60)

pygame.quit()






