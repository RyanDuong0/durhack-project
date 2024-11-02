import pygame
import math

class SolarSystem:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Solar System")

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.sun_pos = (400, 400)
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
