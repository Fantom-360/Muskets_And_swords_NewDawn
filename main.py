import pygame
import math

# Screen setup
screen_setup = (800, 600)
radius = 30
num_rows = 7
num_columns = 7

def draw_hexagon(surface, color, center, size, border_thickness=2):
    SIDECOLOR = (0, 0, 0)
    points = []
    
    for i in range(6):
        angle = math.radians(60 * i)
        x = center[0] + size * math.cos(angle)
        y = center[1] + size * math.sin(angle)
        points.append((x, y))
    
    pygame.draw.polygon(surface, color, points)
    
    for i in range(6):
        pygame.draw.line(surface, SIDECOLOR, points[i], points[(i + 1) % 6], border_thickness)

pygame.init()
screen = pygame.display.set_mode(screen_setup)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))  # White background

    # Calculate the spacing between hexagons
    # Special thanks to  __kumarmohit0911__ for helping with logic of generationg hexagon grid the right way
     
    hex_width = radius * 2
    hex_height = math.sqrt(3) * radius
    x_offset = hex_width * 3/4
    y_offset = hex_height

    coordinates = []
    

    for row in range(num_rows):
        
        for col in range(num_columns):

            rq_cors= []

            x = (screen_setup[0] / 2) - (num_columns * x_offset) / 2 + col * x_offset
            y = (screen_setup[1] / 2) - (num_rows * y_offset) / 2 + row * y_offset
            if col % 2 == 1:
                y += y_offset / 2  # Shift every other column down
            draw_hexagon(screen, (0, 0, 255), (x, y), radius)
            #making coords for hexagons
            rq_cors.append(row)
            rq_cors.append(col)
            
            #appending hex coords in form of 2D matrix
            coordinates.append(rq_cors)
    



    pygame.display.flip()

pygame.quit()

print(coordinates)