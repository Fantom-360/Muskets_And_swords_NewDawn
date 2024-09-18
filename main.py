import pygame 
import math 

screen_setup = (800,600)

radius = 30

num_rows = 3

num_columms = 3



def draw_hexagon(surface, color, center, size, border_thickness = 2):
    
    SIDECOLOR = (0,0,0)
    points = []

    for i in range(6):

        angle = math.radians(60*i)

        x = center[0] + size * math.cos(angle)
        y = center[1] + size * math.sin(angle)

        points.append((x, y))

    pygame.draw.polygon(surface, color, points)

    for i in range(6):
        pygame.draw.line(surface, SIDECOLOR, points[i], points[(i+1) % 6], border_thickness)
    


pygame.init()

screen = pygame.display.set_mode(screen_setup)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
    
    screen.fill((255, 255, 255))  # White background
    
    # Example hexagon positions

    for row in range(1):

        for columm in range(3):
                
                row += 1

            #if (row % 2) == 1:

                x = screen_setup[0]/32 + (radius * 3 * row)

                y = screen_setup[1]/4 + (radius * math.sqrt(3))

                draw_hexagon(screen, (0, 0, 255), (x, y), radius) 

        
             
        

    pygame.display.flip()

pygame.quit()

# * (columm + row/2)