import pygame
import math

# Initialize pygame
pygame.init()

# Window size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hex Grid with Troop Placement")

# Hexagon settings
HEX_SIZE = 30  # The radius of the hexagon
HEX_WIDTH = HEX_SIZE * 2
HEX_HEIGHT = math.sqrt(3) * HEX_SIZE
HEX_SPACING_X = HEX_WIDTH * 3/4  # Horizontal distance between hex centers
HEX_SPACING_Y = HEX_HEIGHT  # Vertical distance between hex centers

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Selected hexes and troop positions
selected_hex = None
troops = []  # List of (x, y) positions for troops

def distance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points (x1, y1) and (x2, y2).
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def draw_hexagon(surface, color, x, y, size, border_color=None):

    """
    Draw a hexagon centered at (x, y) with the given size.
    If border_color is provided, a border will be drawn around the hexagon.
    """
    
    points = []
    for i in range(6):

        angle = math.radians(60*i)

        point_x = x + size * math.cos(angle)

        point_y = y + size * math.sin(angle)

        points.append((point_x, point_y))
    
    # Draw filled hexagon
    pygame.draw.polygon(surface, color, points)
    
    # Draw border if provided
    if border_color:
        pygame.draw.polygon(surface, border_color, points, width=2)

def is_mouse_in_hex(mouse_x, mouse_y, hex_center_x, hex_center_y, radius):

    """
    Check if the mouse is within the given hexagon by measuring the distance
    between the mouse and the hex center.
    """

    dist = distance(mouse_x, mouse_y, hex_center_x, hex_center_y)

    return dist <= radius

def highlight_hex_if_mouse_over(mouse_x, mouse_y, hexagons, radius):
    """
    Iterate through the hexagons and highlight the one the mouse is hovering over.
    Returns the coordinates of the hovered hexagon.
    """
    for hex_center_x, hex_center_y in hexagons:

        if is_mouse_in_hex(mouse_x, mouse_y, hex_center_x, hex_center_y, radius):

            # If the mouse is inside the hexagon, highlight it in red

            draw_hexagon(screen, WHITE, hex_center_x, hex_center_y, radius, border_color=RED)

            return (hex_center_x, hex_center_y)
        
        else:

            # Draw hex in normal white color with black border

            draw_hexagon(screen, WHITE, hex_center_x, hex_center_y, radius, border_color=BLACK)

    return None

def create_hex_grid(columns, rows, hex_size):
    """
    Create a grid of hexagons and return their centers.
    """
    hexagons = []
    
    for row in range(rows):

        for col in range(columns):

            # Calculate hex center positions

            hex_x = hex_size * (3/2) * col

            hex_y = hex_size * math.sqrt(3) * (row + 0.5 * (col % 2))
            
            hexagons.append((hex_x, hex_y))
    
    return hexagons

def place_troop(hex_center_x, hex_center_y, radius):
    """
    Place a troop (a circle) at the center of the given hex.
    """
    pygame.draw.circle(screen, GREEN, (int(hex_center_x), int(hex_center_y)), radius // 3)

# Create a hexagon grid
columns = 10
rows = 10
hexagons = create_hex_grid(columns, rows, HEX_SIZE)

# Game loop
running = True

while running:

    screen.fill(BLUE)  # Fill background with blue color

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Highlight the hex under the mouse and get its center
    hovered_hex = highlight_hex_if_mouse_over(mouse_x, mouse_y, hexagons, HEX_SIZE)

    # Draw troops on the map
    for troop_x, troop_y in troops:

        place_troop(troop_x, troop_y, HEX_SIZE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN and hovered_hex:
            # If a hex is clicked, add it to the list of troops
            troops.append(hovered_hex)

    pygame.display.flip()

# Quit pygame
pygame.quit()