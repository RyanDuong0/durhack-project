# charmodel.py

import pygame

class Character:
    # Define width, height, and color as class attributes
    WIDTH = 60   # Character width
    HEIGHT = 90  # Character height
    IMAGE_PATH = "Image/download.png"  # Replace with your image path

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = self.load_image()

    def load_image(self):
        original_image = pygame.image.load(self.IMAGE_PATH).convert_alpha()  # Load image with transparency
        return pygame.transform.scale(original_image, (self.WIDTH, self.HEIGHT))  # Scale to defined width and height

    def move(self, dx):
        self.x += dx

    def reset_position(self, new_x):
        self.x = new_x

    def get_dimensions(self):
        return self.WIDTH, self.HEIGHT
