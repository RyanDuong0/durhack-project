import pygame
import sys

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Constants
        self.WIDTH, self.HEIGHT = 800, 600
        self.FPS = 60
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # Set up the screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Space Adventure")

        # Load assets
        self.font = pygame.font.Font(None, 74)
        self.title_text = self.font.render("Space Adventure", True, self.WHITE)
        self.start_text = self.font.render("Press Enter to Start", True, self.WHITE)

        self.clock = pygame.time.Clock()

    def draw_start_screen(self):
        self.screen.fill(self.BLACK)
        self.screen.blit(self.title_text, (self.WIDTH // 2 - self.title_text.get_width() // 2, self.HEIGHT // 3))
        self.screen.blit(self.start_text, (self.WIDTH // 2 - self.start_text.get_width() // 2, self.HEIGHT // 2))
        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.start_game()  # Call the main game function

            self.draw_start_screen()
            self.clock.tick(self.FPS)

    def start_game(self):
        print("Game starts!")



if __name__ == "__main__":
    game = Game()
    game.run()
