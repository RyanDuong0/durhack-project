import pygame
import math
import os


class SolarSystem:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Solar System")

        # Colors
        self.colors = {
            "BLACK": (0, 0, 0),
            "WHITE": (255, 255, 255),
            "ORBIT": (100, 100, 100),
            "TOOLTIP_BG": (255, 255, 255),
            "POPUP_BG": (50, 50, 50),
            "CLOSE_BUTTON": (200, 0, 0),
            "BUTTON": (30, 144, 255),
            "BUTTON_HOVER": (70, 130, 180),
        }

        # Font settings
        self.fonts = {
            "default": pygame.font.Font(None, 24),
            "popup": pygame.font.Font(None, 36),
            "button": pygame.font.Font(None, 36),
        }

        self.close_button_image = self.load_image("close.png", (20, 20))
        self.planets = self.load_planets()
        self.back_button = pygame.Rect(10, 750, 200, 50)
        self.selected_planet = None
        self.sun_img = self.load_image("Sun.png", (100, 100))
        self.sun_position = (600 - self.sun_img.get_width() // 2, 400 - self.sun_img.get_height() // 2)
        self.clock = pygame.time.Clock()

    def load_image(self, name, size):
        return pygame.transform.scale(pygame.image.load(os.path.join("Image", name)), size)

    def load_planets(self):
        planet_data = [
            {"name": "Mercury", "image": "Mercury.png", "radius": 5, "distance": 70, "speed": 0.047,
             "info": "Closest to Sun. Mercury has a high rotation speed and a orbit lasts 176 earth days"},
            {"name": "Venus", "image": "Venus.png", "radius": 8, "distance": 90, "speed": 0.035,
             "info": "Hottest planet, Temperatures reach 867°F (464°C).Venus is the third brightest object in the sky after the Sun and Moon."},
            {"name": "Earth", "image": "Earth.png", "radius": 10, "distance": 120, "speed": 0.029,
             "info": "The only planet to support Life, Earth has around 8.5 billion anad population is expected to reach 10 billion by 2040"},
            {"name": "Mars", "image": "Mars.png", "radius": 8, "distance": 160, "speed": 0.024,
             "info": "Known as the Red Planet, Mars has 2 moons. Mars is also known as the other planet that could potentially support life other than earth"},
            {"name": "Jupiter", "image": "Jupiter.png", "radius": 40, "distance": 200, "speed": 0.013,
             "info": "Largest planet with a dense atmosphere.  It's also the oldest planet, forming from the dust and gases left over from the Sun's formation 4.6 billion years ago."},
            {"name": "Saturn", "image": "Saturn.png", "radius": 35, "distance": 260, "speed": 0.009,
             "info": "Famous for its rings.Saturn's rings are mostly made of orbital rocks"},
            {"name": "Uranus", "image": "Uranus.png", "radius": 20, "distance": 300, "speed": 0.007,
             "info": "The ice giant is surrounded by 13 faint rings and 28 small moons. Uranus rotates at a nearly 90-degree angle from the plane of its orbit."},
            {"name": "Neptune", "image": "Neptune.png", "radius": 20, "distance": 350, "speed": 0.005,
             "info": "Dark, cold, and whipped by supersonic winds, ice giant Neptune is more than 30 times as far from the Sun as Earth. Neptune is the only planet in our solar system not visible to the naked eye. "},
        ] #Data for each planet
        for p in planet_data:
            p["img"] = self.load_image(p["image"], (p["radius"] * 2, p["radius"] * 2))
            p["angle"] = 0  # Initial rotation angle
            p["position"] = (600 + math.cos(p["angle"]) * p["distance"],
                             400 + math.sin(p["angle"]) * p["distance"])  # Initial position
        return planet_data

    def draw_planetary_system(self, mouse_pos):
        self.screen.fill(self.colors["BLACK"])
        self.screen.blit(self.sun_img, self.sun_position)

        for p in self.planets:
            is_hovered = math.hypot(mouse_pos[0] - p["position"][0], mouse_pos[1] - p["position"][1]) < p["radius"] + 5
            original_speed = p["speed"]

            # Slow down the orbit if hovered
            if is_hovered:
                p["speed"] *= 0.2  # Planet speed is reduced by 20% if it is hovered over
                self.draw_tooltip(p["name"], mouse_pos) # Tooltip of planet's name appear

            # Update planet's position and orbit
            p["angle"] += p["speed"]
            p["position"] = (600 + math.cos(p["angle"]) * p["distance"],
                             400 + math.sin(p["angle"]) * p["distance"])
            self.screen.blit(p["img"], (p["position"][0] - p["radius"], p["position"][1] - p["radius"]))

            # Reset the speed after processing
            p["speed"] = original_speed

        # Draw popup if a planet is selected
        if self.selected_planet:
            close_rect = self.draw_popup(self.selected_planet["name"], self.selected_planet["info"])
            return close_rect
        return None

    def draw_tooltip(self, text, pos):
        tooltip_surf = self.fonts["default"].render(text, True, self.colors["BLACK"])
        rect = tooltip_surf.get_rect(topleft=(pos[0] + 10, pos[1] + 10)).inflate(10, 10)
        pygame.draw.rect(self.screen, self.colors["TOOLTIP_BG"], rect)
        self.screen.blit(tooltip_surf, rect.topleft)

    def draw_popup(self, title, info):
        popup_width, popup_height = 500, 300
        popup_rect = pygame.Rect(
            (self.screen.get_width() - popup_width) // 2,
            (self.screen.get_height() - popup_height) // 2,
            popup_width, popup_height)

        pygame.draw.rect(self.screen, self.colors["POPUP_BG"], popup_rect) #

        title_surface = self.fonts["popup"].render(title, True, self.colors["WHITE"])
        self.screen.blit(title_surface, title_surface.get_rect(center=(popup_rect.centerx, popup_rect.top + 20)))

        wrapped_lines = self.wrap_text(info, popup_rect.width - 40, popup_rect.height - 100)
        for i, line in enumerate(wrapped_lines):
            line_surface = self.fonts["default"].render(line, True, self.colors["WHITE"])
            self.screen.blit(line_surface, line_surface.get_rect(center=(popup_rect.centerx, popup_rect.top + 70 + i * self.fonts["default"].get_linesize())))

        close_rect = pygame.Rect(popup_rect.right - 30, popup_rect.top + 10, 20, 20)
        self.screen.blit(self.close_button_image, close_rect.topleft)

        # Explore button
        button_rect = pygame.Rect(popup_rect.centerx - 100, popup_rect.bottom - 60, 200, 50)
        button_color = self.colors["BUTTON_HOVER"] if button_rect.collidepoint(pygame.mouse.get_pos()) else self.colors["BUTTON"] # Get Button Hover colour
        pygame.draw.rect(self.screen, button_color, button_rect)
        button_text_surface = self.fonts["button"].render("Explore", True, self.colors["WHITE"]) # Render text White inside the popup window
        self.screen.blit(button_text_surface, button_text_surface.get_rect(center=button_rect.center)) #Recenters text to Centre

        return close_rect

    def wrap_text(self, text, max_width, max_height):
        wrapped_lines, current_line = [], ""
        for word in text.split():
            test_line = f"{current_line} {word}".strip()
            if self.fonts["default"].size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                wrapped_lines.append(current_line)
                current_line = word

            if sum(self.fonts["default"].get_linesize() for line in wrapped_lines) >= max_height:
                wrapped_lines[-1] += "..."
                break

        if current_line:
            wrapped_lines.append(current_line)

        return wrapped_lines

    def run(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos() #Get mouse position for hovering
            close_rect = self.draw_planetary_system(mouse_pos) #Draw planets for solar system

            # Draw back button
            pygame.draw.rect(self.screen, self.colors["BUTTON"], self.back_button) #Draw back Button
            button_text = self.fonts["button"].render("Back", True, self.colors["WHITE"])
            self.screen.blit(button_text, button_text.get_rect(center=self.back_button.center))

            pygame.display.flip()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.collidepoint(event.pos):
                        return
                    if close_rect and close_rect.collidepoint(event.pos):
                        self.selected_planet = None
                    else:
                        for p in self.planets:
                            if math.hypot(mouse_pos[0] - p["position"][0], mouse_pos[1] - p["position"][1]) < p["radius"] + 5:
                                self.selected_planet = p
        pygame.quit()