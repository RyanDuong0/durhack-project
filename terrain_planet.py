import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
import os

class TerrainRenderer:
    def __init__(self, terrain_model):
        pygame.init()
        pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
        gluPerspective(45, (800 / 600), 0.1, 50.0)
        glTranslatef(0.0, -2.0, -10)

        self.terrain_model = terrain_model  # Path to the terrain model file (unique for each planet)

    def load_texture(self, image_path):
        texture_surface = pygame.image.load(image_path)
        texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
        width, height = texture_surface.get_size()

        tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)

        return tex_id

    def draw_terrain(self):
        # Example vertices for a simple grid terrain; replace this with a 3D model load if available
        glBegin(GL_QUADS)
        for x in range(-5, 5):
            for z in range(-5, 5):
                glColor3f(0.3, 0.5, 0.2)
                glVertex3f(x, 0, z)
                glVertex3f(x + 1, 0, z)
                glVertex3f(x + 1, 0, z + 1)
                glVertex3f(x, 0, z + 1)
        glEnd()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.draw_terrain()  # Call function to draw the loaded 3D terrain model
            pygame.display.flip()
            pygame.time.wait(10)

        pygame.quit()
        sys.exit()

# To run this code when Explore is clicked:
if __name__ == "__main__":
    planet_name = sys.argv[1] if len(sys.argv) > 1 else "earth"  # Default to earth if not specified
    terrain_model_path = os.path.join("Models", f"{planet_name}_terrain.obj")
    renderer = TerrainRenderer(terrain_model_path)
    renderer.run()
