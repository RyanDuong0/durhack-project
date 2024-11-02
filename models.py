import pygame
import math

WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BUTTON_COLOR = (30, 144, 255)  # Dodger Blue
BUTTON_HOVER_COLOR = (70, 130, 180)  # Steel Blue
SLIDER_COLOR = (100, 100, 255)  # Light blue for the slider

font_size = 50  # Default font size

class Button:
    def __init__(self, text, x, y, width, height, bg_color, hover_color):
        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.update_text()  # Initialize text surface

    def update_text(self):
        # Update the text surface whenever font size changes
        self.text_surf = self.font.render(self.text, True, WHITE)
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

class SolarSystem:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Solar System")

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.sun_pos = (600, 400)
        self.clock = pygame.time.Clock()

        # Font settings
        self.font = pygame.font.Font(None, 36)

        # Planet data: (color, radius, distance from sun, speed, name)
        self.planets = [
            ((255, 0, 0), 5, 70, 0.047, "Mercury"),
            ((255, 165, 0), 8, 90, 0.035, "Venus"),
            ((0, 0, 255), 10, 120, 0.029, "Earth"),
            ((255, 69, 0), 8, 160, 0.024, "Mars"),
            ((255, 70, 43), 40, 200, 0.013, "Jupiter"),
            ((216, 202, 157), 35, 280, 0.009, "Saturn"),
            ((225, 238, 238), 20, 320, 0.007, "Uranus"),
            ((0, 147, 125), 25, 350, 0.005, "Neptune"),
        ]

        self.angles = [0] * len(self.planets)

        #create buttons
        self.back_button = Button("BACK", WIDTH // 2 - 100, HEIGHT // 2 + 150, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)

    def draw_planet(self, x, y, color, radius, name, rings=False):
        pygame.draw.circle(self.screen, color, (int(x), int(y)), radius)
        # Render the text and blit it near the planet
        text_surface = self.font.render(name, True, self.white)
        self.screen.blit(text_surface, (x + radius + 5, y))

        if rings:
            ring_width = int(radius * 1.5)  # Ring width relative to planet size
            ring_height = int(radius * 0.5)  # Ring height relative to planet size
            ring_color = (200, 200, 200)  # Light grey color for the rings
            pygame.draw.ellipse(self.screen, ring_color,
                                (x - ring_width // 2, y - ring_height // 2, ring_width, ring_height), 2)

    def run(self):
        running = True
        while running:
            self.screen.fill(self.black)
            pygame.draw.circle(self.screen, (255, 255, 0), self.sun_pos, 50)  # Sun
            for i, (color, radius, distance, speed, name) in enumerate(self.planets):
                self.angles[i] += speed
                x = self.sun_pos[0] + math.cos(self.angles[i]) * distance
                y = self.sun_pos[1] + math.sin(self.angles[i]) * distance
                self.draw_planet(x, y, color, radius, name)

            pygame.display.flip()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()



if __name__ == "__main__":
    solar_system = SolarSystem()
    solar_system.run()
