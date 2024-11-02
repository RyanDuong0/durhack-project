import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BUTTON_COLOR = (30, 144, 255)  # Dodger Blue
BUTTON_HOVER_COLOR = (70, 130, 180)  # Steel Blue

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game - Start Screen")

# Load assets
font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)
title_text = font.render("Space Adventure", True, WHITE)

# Load background image
background_image = pygame.image.load("Image/background.jpg")  # Path to your background image
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Resize to fit screen

try:
    cog_image = pygame.image.load("Image/download.png")  # Path to your cog image
    cog_image = pygame.transform.scale(cog_image, (50, 50))  # Scale cog image to 50x50 pixels
except pygame.error as e:
    print(f"Unable to load cog image: {e}")
    pygame.quit()
    sys.exit()

# Button class
class Button:
    def __init__(self, text, x, y, width, height, font, bg_color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_surf = font.render(text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, surface):
        # Check if the mouse is over the button for hover effect
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            pygame.draw.rect(surface, self.bg_color, self.rect)
        surface.blit(self.text_surf, self.text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
class ImageButton:
    def __init__(self, image, x, y, width, height):
        self.image = image
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        # Draw the button background
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(surface, BUTTON_HOVER_COLOR, self.rect)
        else:
            pygame.draw.rect(surface, BUTTON_COLOR, self.rect)

        # Draw the cog image centered in the button area
        image_rect = self.image.get_rect(center=self.rect.center)
        surface.blit(self.image, image_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
# Initialize buttons
start_button = Button("Start", WIDTH // 2 - 100, HEIGHT // 2, 200, 50, button_font, BUTTON_COLOR, BUTTON_HOVER_COLOR)
quit_button = Button("Quit", WIDTH // 2 - 100, HEIGHT // 2 + 70, 200, 50, button_font, BUTTON_COLOR, BUTTON_HOVER_COLOR)

# Create a settings button
cog_imge = Button("Settings", WIDTH // 2 - 100, HEIGHT - 150, 200, 50, button_font, BUTTON_COLOR, BUTTON_HOVER_COLOR)

def draw_start_screen():
    screen.blit(background_image, (0, 0))  # Draw the background image
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))  # Center the title
    start_button.draw(screen)  # Draw the "Start" button
    quit_button.draw(screen)  # Draw the "Quit" button
    cog_imge.draw(screen)  # Draw the "Settings" button
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check button clicks
            if start_button.is_clicked(event):
                print("Game starts!")  # Placeholder for starting the game
                # Call the main game function here

            if quit_button.is_clicked(event):
                pygame.quit()
                sys.exit()

            if cog_imge.is_clicked(event):
                print("Settings clicked!")  # Placeholder for opening settings

        draw_start_screen()
        clock.tick(FPS)

if __name__ == "__main__":
    main()