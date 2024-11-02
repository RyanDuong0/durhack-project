import pygame
import sys
from charmodel import Character  # Import the Character class

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

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

# Create the character instance with fixed dimensions and color from charmodel
character = Character(WIDTH // 2, HEIGHT - Character.HEIGHT - 50)

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
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        character.move(-5)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        character.move(5)

    # Collision and transition logic
    if current_scene == 0:  # Scene 1: Solid wall on the left
        if character.x < 0:
            character.x = 0  # Prevent going past the left wall
        elif character.x > WIDTH - Character.WIDTH:  # Right edge
            current_scene += 1  # Move to Scene 2
            character.reset_position(0)  # Reset position to left side of Scene 2

    elif current_scene == 1:  # Scene 2: No walls
        if character.x < 0:  # Left edge
            current_scene = 0  # Move to Scene 1
            character.reset_position(WIDTH - Character.WIDTH)  # Reset position to right side of Scene 1
        elif character.x > WIDTH - Character.WIDTH:  # Right edge
            current_scene += 1  # Move to Scene 3
            character.reset_position(0)  # Reset position to left side of Scene 3

    elif current_scene == 2:  # Scene 3: Solid wall on the right
        if character.x < 0:  # Left edge
            current_scene = 1  # Move to Scene 2
            character.reset_position(WIDTH - Character.WIDTH)  # Reset position to right side of Scene 2
        elif character.x > WIDTH - Character.WIDTH:
            character.x = WIDTH - Character.WIDTH  # Prevent going past the right wall

    # Get the current scene colors
    background_color, sand_color = scenes[current_scene]

    # Fill the screen with the current background color
    screen.fill(background_color)

    # Draw the sand floor
    pygame.draw.rect(screen, sand_color, (0, HEIGHT - 50, WIDTH, 50))  # Sand at the bottom

    # Draw the character using the image
    screen.blit(character.image, (character.x, character.y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()
