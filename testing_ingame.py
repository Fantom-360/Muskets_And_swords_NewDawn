import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0,0,255)
HIGHLIGHT = (255, 200, 0)  # Highlight color

# Set the screen background
screen.fill(WHITE)
pygame.display.set_caption("Hex Grid Map")

def hex_corner(center, size, i):
    """Calculate the corner of a hexagon given its center, size, and corner index (0-5)."""
    angle_deg = 60 * i   # Offset for flat-topped hex
    angle_rad = math.pi / 180 * angle_deg
    return (center[0] + size * math.cos(angle_rad),
            center[1] + size * math.sin(angle_rad))

def draw_hexagon(surface, center, size, color=BLUE):
    """Draw a hexagon at a given center position."""
    points = [hex_corner(center, size, i) for i in range(6)]
    pygame.draw.polygon(surface, color, points, 0)

    for i in range(6):
        pygame.draw.line(surface, BLACK, points[i], points[(i+1) % 6], 3)

def axial_to_pixel(q, r, size):
    """Convert axial coordinates (q, r) to pixel coordinates (x, y) for hexagon center."""
    x = size * (3/2 * q)
    y = size * (math.sqrt(3) * (r + q / 2))
    return (x + WIDTH // 2, y + HEIGHT // 2)  # Offset to center on screen

def build_adjacency_list(map_size):
    adjacency_list = {}
    
    for q in range(-map_size, map_size + 1):
        for r in range(-map_size, map_size + 1):
            if -map_size <= q <= map_size and -map_size <= r <= map_size:
                # Get neighbors (we won't use this here but can be used later for logic)
                neighbors = get_neighbors(q, r)
                adjacency_list[(q, r)] = neighbors
                
    return adjacency_list

# Get neighbors function (reused from earlier)
def get_neighbors(q, r):
    directions = [(+1, 0), (0, +1), (-1, +1), 
                  (-1, 0), (0, -1), (+1, -1)]
    
    return [(q + dq, r + dr) for dq, dr in directions]

# Build and draw the grid
def draw_grid(surface, map_size, hex_size):

    adjacency_list = build_adjacency_list(map_size)

    for (q, r) in adjacency_list.keys():

        center = axial_to_pixel(q, r, hex_size)

        draw_hexagon(surface, center, hex_size)

def pixel_to_axial(x, y, size):
    """Convert pixel coordinates (x, y) to axial coordinates (q, r)."""
    q = (2/3 * x) / size
    r = (-1/3 * x + math.sqrt(3)/3 * y) / size
    return hex_round(q, r)

def hex_round(q, r):
    """Round floating point axial coordinates to the nearest hex."""
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
    
    return (rx, rz)

def drawTroop()


map_size = 3
hex_size = 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(WHITE)
    
    # Draw the grid
    draw_grid(screen, map_size, hex_size)
    
    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()
    
    # Convert mouse position to axial coordinates
    q, r = pixel_to_axial(mouse_pos[0] - WIDTH // 2, mouse_pos[1] - HEIGHT // 2, hex_size)
    
    # Highlight the hexagon under the mouse
    
    if (-map_size <= q <= map_size) and (-map_size <= r <= map_size):
        center = axial_to_pixel(q, r, hex_size)
        draw_hexagon(screen, center, hex_size, HIGHLIGHT)

    
    
    # Update the display
    pygame.display.flip()

pygame.quit()



