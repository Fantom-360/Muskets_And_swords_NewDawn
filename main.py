import pygame
import math

## game set up

pygame.init()

screen_setup = (800, 600)

hex_color = (0, 0, 255)

screen = pygame.display.set_mode(screen_setup)

clock = pygame.time.Clock()


#class HexObject:
#    def __init__(self, surface, color, center, hex_size):

## main sizes/ game values

hex_size = 30

hex_height = math.sqrt(3) * hex_size

hex_widht = 2 * hex_size

x_offset = 3/2 * hex_size

y_offset = hex_height





#main hex drawing func
def drawHex(surface, color, pos):

    border_thickenss = 3

    border_col = (0, 0, 0)

    points = []

    for i in range(6):

        angle = math.radians(60*i)

        x_i = pos[0] + hex_size * math.cos(angle)
        y_i = pos[1] + hex_size * math.sin(angle)

        points.append((x_i, y_i))

    pygame.draw.polygon(surface, color, points)

    for i in range(6):

        pygame.draw.line(surface, border_col, points[i], points[(i+1) % 6], border_thickenss)

# creating a hex map for coords and stuff

def create_hex_map(rows, cols):

    hex_map = []

    for r in range(rows):

        row = []

        for q in range(cols):

            #new hex creating logic based on old one but still new and newly with coords

            x = ((0 + x_offset) - (q / 2) + (q * x_offset))

            y = ((0 + y_offset) - (r / 2) + (r * y_offset))

            if q % 2 == 1:

                y += y_offset / 2

            row.append((x, y))

        hex_map.append(row)
    
    return hex_map

def pixel_to_hex(x, y):

    q = (x * math.sqrt(3)/3 - y / 3) / hex_size
    
    r = y * 2/3 / hex_size

    return hex_round(q, r)

# Function to round hex coordinates to nearest integer
def hex_round(q, r):
    z = -q - r
    rq = round(q)
    rr = round(r)
    rz = round(z)

    q_diff = abs(rq - q)
    r_diff = abs(rr - r)
    z_diff = abs(rz - z)

    if q_diff > r_diff and q_diff > z_diff:
        rq = -rr - rz
    elif r_diff > z_diff:
        rr = -rq - rz

    return (rq, rr)



#main game set up
def main():

    rows, cols = 10, 17 #number of hexes

    hex_map = create_hex_map(rows, cols)

    # main game loop

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False
        
        screen.fill((255, 255, 255))


        for row in hex_map:

            for hex_pos in row:

                drawHex(screen, hex_color, hex_pos)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

    print(hex_map)

if __name__ == "__main__":

    main()