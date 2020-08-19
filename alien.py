import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Create a class for alien..."""
    def __init__(self, screen, ai_settings):
        #Inherit from sprite properly
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #Get rect of screen..


        #load image of alien
        self.image = pygame.image.load('images/his.bmp')
        self.rect = self.image.get_rect()

        #Attributing properties
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store position of alien..
        self.x = float(self.rect.x)

    def update(self):
        """Move alien accordingly..."""
        self.x += (self.ai_settings.alien_direction * self.ai_settings.alien_speed)
        #Update position
        self.rect.x = self.x

    def check_edges(self):
        """Check if alien has reached the edge of screen.."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        """Draw alien to screen..."""
        self.screen.blit(self.image, self.rect)

