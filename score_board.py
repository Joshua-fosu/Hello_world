import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """Create a class to manage scores and levels.."""
    def __init__(self, screen, stats, ai_settings):
        #Attributing arguments...
        self.screen = screen
        self.stats = stats
        self.ai_settings = ai_settings
        #Get rect of screen...
        self.screen_rect = self.screen.get_rect()
        #Input text attributes...
        self.font = pygame.font.SysFont(None, 30)
        self.color = 0, 0, 0
        self.prep_score()
        self.prep_high_score()
        self.prep_levels()
        self.prep_ship(screen, ai_settings)

    def prep_score(self):
        """Render score in form of image..."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.image = self.font.render(score_str, True, self.color,
                                      self.ai_settings.bg_color)
        self.image_rect = self.image.get_rect()
        self.image_rect.right = self.screen_rect.right - 20
        self.image_rect.top = 20

    def prep_high_score(self):
        """Render high score in the form of image..."""
        rounded_high_score = int(round(self.stats.high_score, -1))
        high_score = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render("High score: " + high_score, True, self.color,
                                                 self.ai_settings.bg_color)
        self.high_rect = self.high_score_image.get_rect()
        self.high_rect.centerx = self.screen_rect.centerx
        self.high_rect.top = 20

    def prep_levels(self):
        """Render levels in form of image..."""
        levels_str = str(self.stats.levels)
        self.levels_image = self.font.render(levels_str, True, self.color,
                                             self.ai_settings.bg_color)
        self.levels_rect = self.levels_image.get_rect()
        self.levels_rect.right = self.screen_rect.right -20
        self.levels_rect.top = 40

    def prep_ship(self, screen, ai_settings):
        self.ships = Group()
        for ship_number in range(self.stats.ship_lives):
            ship = Ship(screen, ai_settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def draw_score(self):
        """Draw to screen"""
        self.screen.blit(self.image, self.image_rect)
        self.screen.blit(self.high_score_image, self.high_rect)
        self.screen.blit(self.levels_image, self.levels_rect)
        self.ships.draw(self.screen)
