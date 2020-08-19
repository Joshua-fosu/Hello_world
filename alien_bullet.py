import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):
    """Create class to host alien bullets..."""
    def __init__(self, screen, ai_settings, alien):
        #Inherit from sprite properly...
        super().__init__()
        self.screen = screen

        #Draw rect at 0,0 and set to original position...
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom

        #Call from settings..
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed
        #Store position in another variable
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet down the screen.."""
        self.y += self.speed_factor
        #Update position of bullet..
        self.rect.y = self.y

    def draw_alien_bullet(self):
        #Draw bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)
