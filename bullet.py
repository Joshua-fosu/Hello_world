import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Create class to manage bullets from ship..."""
    def __init__(self, screen, ai_settings, ship):
        #Inherit from sprite properly...
        super().__init__()
        self.screen = screen
        #Draw rect of bullet..
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        # Start each bullet journey at top of ship
        self.rect.top = ship.rect.top
        self.rect.centerx = ship.rect.centerx

        #Store float of of bullet position
        self.y = float(self.rect.y)
        #Call for x'tics from ai_settings..
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed

    def update(self):
        self.y -= self.speed_factor
        #Updare rect position..
        self.rect.y = self.y

    def draw_bullet(self):
        #Draw bullet to screen...
        pygame.draw.rect(self.screen, self.color , self.rect)

