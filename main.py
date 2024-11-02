import pygame
import sys
from game import Game

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1024, 768
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game - Start Screen")

# Load assets
font = pygame.font.Font(None, 74)
title_text = font.render("Space Adventure", True, WHITE)
start_text = font.render("Press Enter to Start", True, WHITE)

def draw_start_screen():
    screen.fill(BLACK)
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
