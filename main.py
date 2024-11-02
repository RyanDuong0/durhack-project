import pygame
import sys
from game import Game

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game - Start Screen")

# Load assets
font = pygame.font.Font(None, 74)
title_text = font.render("Space Adventure", True, WHITE)
start_text = font.render("Press Enter to Start", True, WHITE)

# Load background image
background_image = pygame.image.load("Image/background.jpg")  # Path to your background image
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Resize to fit screen

def draw_start_screen():
    screen.blit(background_image, (0, 0))  # Draw the background image
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Game()  # Placeholder for starting the game
                    # You can call the main game function here

        draw_start_screen()
        clock.tick(FPS)

if __name__ == "__main__":
    main()