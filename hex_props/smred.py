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
HIGHLIGHT = (255, 200, 0)  # Highlight color

# Hexagon properties
hex_size = 30
map_width = 5  # Number of hex columns
map_height = 5   # Number of hex rows

def hex_corner(center, size, i):
    """Calculate the corner of a hexagon given its center, size, and corner index (0-5)."""
    angle_deg = 60 * i # Offset for flat-topped hex
    angle_rad = math.pi / 180 * angle_deg
    return (center[0] + size * math.cos(angle_rad),
            center[1] + size * math.sin(angle_rad))

def draw_hexagon(surface, center, size, color=BLACK):
    """Draw a hexagon at a given center position."""
    points = [hex_corner(center, size, i) for i in range(6)]
    pygame.draw.polygon(surface, color, points, 2)  # 2 means line thickness

def axial_to_pixel(q, r, size):
    """Convert axial coordinates (q, r) to pixel coordinates (x, y) for hexagon center."""
    x = size * 3/2 * q  # Horizontal spacing based on q
    y = size * math.sqrt(3) * r + (q % 2) * (size * math.sqrt(3) / 2)  # Adjust vertical spacing
    return (x + WIDTH // 2, y + HEIGHT // 2)  # Center on screen

def pixel_to_axial(x, y, size):
    """Convert pixel coordinates (x, y) to axial coordinates (q, r)."""
    x = (x - WIDTH // 2) / size
    y = (y - HEIGHT // 2) / size
    
    q = (2/3 * x)
    r = (-1/3 * x + (math.sqrt(3)/3) * y)
    
    return round(q), round(r)

def get_neighbors(q, r):
    """Get neighboring axial coordinates for a hexagon."""
    directions = [(+1, 0), (0, +1), (-1, +1), (-1, 0), (0, -1), (+1, -1)]
    return [(q + dq, r + dr) for dq, dr in directions]

def build_adjacency_list(map_width, map_height):
    """Build adjacency list for hex grid."""
    adjacency_list = {}
    
    for r in range(map_height):
        for q in range(map_width):
            # Add each hexagon and its neighbors
            adjacency_list[(q, r)] = get_neighbors(q, r)
    
    return adjacency_list

def draw_grid(surface, map_width, map_height, hex_size):
    """Draw a hexagonal grid."""
    for r in range(map_height):
        for q in range(map_width):
            center = axial_to_pixel(q, r, hex_size)
            draw_hexagon(surface, center, hex_size)

# Build adjacency list
adjacency_list = build_adjacency_list(map_width, map_height)

# Print adjacency list for debugging
print("Adjacency List:")
for hexagon, neighbors in adjacency_list.items():
    print(f"{hexagon}: {neighbors}")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(WHITE)
    
    # Draw the grid
    draw_grid(screen, map_width, map_height, hex_size)
    
    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()
    
    # Convert mouse position to axial coordinates
    q, r = pixel_to_axial(mouse_pos[0], mouse_pos[1], hex_size)
    
    # Highlight the hexagon under the mouse
    if (0 <= q < map_width) and (0 <= r < map_height):
        center = axial_to_pixel(q, r, hex_size)
        draw_hexagon(screen, center, hex_size, HIGHLIGHT)
    
    # Update the display
    pygame.display.flip()

pygame.quit()