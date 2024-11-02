import pygame
import sys
from models import SolarSystem

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
SLIDER_COLOR = (100, 100, 255)  # Light blue for the slider

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game - Start Screen")

# Load assets
font_size = 50  # Default font size
font = pygame.font.Font(None, font_size)
button_font = pygame.font.Font(None, font_size)
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
    def __init__(self, text, x, y, width, height, bg_color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.update_text()  # Initialize text surface

    def update_text(self):
        # Update the text surface whenever font size changes
        font = pygame.font.Font(None, font_size)
        self.text_surf = font.render(self.text, True, WHITE)
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

# Slider class for text size
class Slider:
    def __init__(self, x, y, width):
        self.rect = pygame.Rect(x, y, width, 20)
        self.handle_rect = pygame.Rect(x, y, 20, 20)  # Handle size
        self.value = 50  # Default value (corresponds to a font size of 50)

    def draw(self, surface):
        # Draw the slider track
        pygame.draw.rect(surface, WHITE, self.rect)
        # Draw the handle
        pygame.draw.rect(surface, SLIDER_COLOR, self.handle_rect)

    def update(self, mouse_x):
        # Update the handle position based on mouse x position
        if self.rect.x <= mouse_x <= self.rect.x + self.rect.width:
            self.handle_rect.centerx = mouse_x
            # Map the x position to a font size range (20 to 100)
            self.value = int(((mouse_x - self.rect.x) / self.rect.width) * (100 - 20) + 20)
            return self.value
        return self.value

# Initialize buttons and slider
start_button = Button("Start", WIDTH // 2 - 100, HEIGHT // 2, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)
quit_button = Button("Quit", WIDTH // 2 - 100, HEIGHT // 2 + 70, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)
settings_button = Button("", 10, HEIGHT - 60, 50, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)  # Only for image
slider = Slider(WIDTH // 2 - 150, HEIGHT // 2, 300)  # Slider for text size

# Settings state
settings_active = False

def draw_start_screen():
    global font, title_text
    screen.blit(background_image, (0, 0))  # Draw the background image
    font = pygame.font.Font(None, font_size)  # Update the main font for the title
    title_text = font.render("Space Adventure", True, WHITE)  # Update title text
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))  # Center the title
    start_button.draw(screen)  # Draw the "Start" button
    quit_button.draw(screen)  # Draw the "Quit" button
    screen.blit(cog_image, (settings_button.rect.x, settings_button.rect.y))  # Draw the cog image
    pygame.display.flip()

def draw_settings_screen():
    global font
    screen.fill(BLACK)  # Clear the screen
    settings_text = font.render("Settings", True, WHITE)
    screen.blit(settings_text, (WIDTH // 2 - settings_text.get_width() // 2, HEIGHT // 3))  # Center the settings title

    # Draw the slider and its label
    slider.draw(screen)
    slider_value_text = font.render(f"Text Size: {slider.value}", True, WHITE)
    screen.blit(slider_value_text, (WIDTH // 2 - slider_value_text.get_width() // 2, HEIGHT // 2 - 50))

    # Draw the magnifier instruction
    magnifier_text = font.render("Press M to magnify", True, WHITE)
    screen.blit(magnifier_text, (WIDTH // 2 - magnifier_text.get_width() // 2, HEIGHT // 2 + 40))

    pygame.display.flip()

def main():
    global settings_active, font_size
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check button clicks
            if start_button.is_clicked(event):
                print("Game starts!")  # Placeholder for starting the game
                solar_system = SolarSystem()
                solar_system.run()

            if quit_button.is_clicked(event):
                pygame.quit()
                sys.exit()

            if settings_button.is_clicked(event):
                settings_active = True

            # If in settings mode
            if settings_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Go back to start screen
                        settings_active = False
                    elif event.key == pygame.K_m:  # Magnify text size
                        font_size += 5
                        for button in [start_button, quit_button]:  # Update buttons with new font size
                            button.update_text()  # Update button text surfaces with new font size
                        font = pygame.font.Font(None, font_size)  # Update font with new size

            # Update slider value if the mouse is dragged
            if settings_active and event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:  # Check if the left mouse button is held down
                    slider.update(event.pos[0])

        if settings_active:
            font_size = slider.update(slider.handle_rect.centerx)  # Get updated font size from slider
            draw_settings_screen()  # Draw the settings screen
        else:
            draw_start_screen()  # Draw the main screen

        clock.tick(FPS)

if __name__ == "__main__":
    main()
