import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
CHARACTER_SIZE = 50
CHARACTER_COLOR = (0, 128, 255)

# Define scenes as tuples of (background_color, sand_color)
scenes = [
    ((0, 0, 0), (194, 178, 128)),   # Scene 1: Black sky, sand color
    ((30, 30, 30), (255, 222, 173)), # Scene 2: Dark gray sky, lighter sand
    ((100, 100, 100), (50, 50, 50))  # Scene 3: Gray sky, dark sand
]

# Initial scene index
current_scene = 0

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2D Character Control')

# Character position
character_x = WIDTH // 2
character_y = HEIGHT - CHARACTER_SIZE - 50  # Position character above the sand

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get key states
    keys = pygame.key.get_pressed()

    # Move left and right
    if keys[pygame.K_LEFT]:
        character_x -= 5
    if keys[pygame.K_RIGHT]:
        character_x += 5

    # Collision and transition logic
    if current_scene == 0:  # Scene 1: Solid wall on the left
        if character_x < 0:
            character_x = 0  # Prevent going past the left wall
        elif character_x > WIDTH - CHARACTER_SIZE:  # Right edge
            current_scene += 1  # Move to Scene 2
            character_x = 0  # Reset position to left side of Scene 2

    elif current_scene == 1:  # Scene 2: No walls
        if character_x < 0:  # Left edge
            current_scene = 0  # Move to Scene 1
            character_x = WIDTH - CHARACTER_SIZE # Reset position to right side of scene 1
        elif character_x > WIDTH - CHARACTER_SIZE:  # Right edge
            current_scene += 1  # Move to Scene 3
            character_x = 0  # Reset position to left side of Scene 3

    elif current_scene == 2:  # Scene 3: Solid wall on the right
        if character_x < 0:  # Left edge
            current_scene = 1  # Move to Scene 2
            character_x =  WIDTH - CHARACTER_SIZE # Reset position to right side of scene 2
        elif character_x > WIDTH - CHARACTER_SIZE:
            character_x = WIDTH - CHARACTER_SIZE  # Prevent going past the right wall

    # Get the current scene colors
    background_color, sand_color = scenes[current_scene]

    # Fill the screen with the current background color
    screen.fill(background_color)

    # Draw the sand floor
    pygame.draw.rect(screen, sand_color, (0, HEIGHT - 50, WIDTH, 50))  # Sand at the bottom

    # Draw the character
    pygame.draw.rect(screen, CHARACTER_COLOR, (character_x, character_y, CHARACTER_SIZE, CHARACTER_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()
