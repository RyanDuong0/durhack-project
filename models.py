import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Solar System")

black = (0, 0, 0)
white = (255, 255, 255)
sun_pos = (400, 400)
clock = pygame.time.Clock()

# Font settings
font = pygame.font.Font(None, 36)

def draw_planet(x, y, color, radius, name,rings=False):
    pygame.draw.circle(screen, color, (int(x), int(y)), radius)
    # Render the text and blit it near the planet
    text_surface = font.render(name, True, white)
    screen.blit(text_surface, (x + radius + 5, y))

    if rings:
        ring_width = int(radius * 1.5)  # Ring width relative to planet size
        ring_height = int(radius * 0.5)  # Ring height relative to planet size
        ring_color = (200, 200, 200)  # Light grey color for the rings
        pygame.draw.ellipse(screen, ring_color,
                            (x - ring_width // 2, y - ring_height // 2, ring_width, ring_height), 2)

        # Render the text and blit it near the planet
    text_surface = font.render(name, True, white)
    screen.blit(text_surface, (x + radius + 5, y))

# Planet data: (color, radius, distance from sun, speed, name)
planets = [
    ((255, 0, 0), 5, 70, 0.047, "Mercury"),
    ((255, 165, 0), 8, 90, 0.035, "Venus"),
    ((0, 0, 255), 10, 120, 0.029, "Earth"),
    ((255, 69, 0), 8, 160, 0.024, "Mars"),
    ((255,70,43),40,200,0.013,"Jupiter"),
    ((216,202,157),35,280,0.009,"Saturn"),
    ((225,238,238),20,320,0.007,"Uranus"),
    ((0, 147, 125),25,350,0.005,"Neptune",),
]

angles = [0] * len(planets)

running = True
while running:
    screen.fill(black)
    pygame.draw.circle(screen, (255, 255, 0), sun_pos, 50,)  # Sun
    for i, (color, radius, distance, speed, name) in enumerate(planets):
        angles[i] += speed
        x = sun_pos[0] + math.cos(angles[i]) * distance
        y = sun_pos[1] + math.sin(angles[i]) * distance
        draw_planet(x, y, color, radius, name)

        if "rings" in planets:
            for ring_radius in planets["rings"]:
                pygame.draw.circle(screen, (210, 180, 140), (int(x), int(y)), planet["radius"] + ring_radius, 1)


    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
