import pygame

class Character:
    # Define width, height, and color as class attributes
    WIDTH = 30   # Character width
    HEIGHT = 80  # Character height
    COLOR = (0, 128, 255)  # Spaceman color

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        # Draw the spaceman using basic shapes
        # Head
        head_radius = 15
        pygame.draw.circle(surface, (255, 255, 255), (self.x + self.WIDTH // 2, self.y + head_radius), head_radius)  # Head
        # Body (starts below the head)
        pygame.draw.rect(surface, self.COLOR, (self.x, self.y + head_radius * 2, self.WIDTH, self.HEIGHT))  # Body

        # Legs (drawn from the bottom of the body)
        leg_height = self.HEIGHT // 2
        pygame.draw.rect(surface, self.COLOR, (self.x, self.y + self.HEIGHT + head_radius * 2, self.WIDTH // 3, leg_height))  # Left leg
        pygame.draw.rect(surface, self.COLOR, (self.x + self.WIDTH * 2 // 3, self.y + self.HEIGHT + head_radius * 2, self.WIDTH // 3, leg_height))  # Right leg

        # Arms (drawn starting from the body)
        pygame.draw.rect(surface, self.COLOR, (self.x - self.WIDTH // 2, self.y + head_radius * 2 + 10, self.WIDTH // 2, self.HEIGHT // 2))  # Left arm
        pygame.draw.rect(surface, self.COLOR, (self.x + self.WIDTH, self.y + head_radius * 2 + 10, self.WIDTH // 2, self.HEIGHT // 2))  # Right arm


    def move(self, dx):
        self.x += dx

    def reset_position(self, new_x):
        self.x = new_x

    def get_dimensions(self):
        return self.WIDTH, self.HEIGHT