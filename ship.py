import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Create ship class"""
    def __init__(self, screen, ai_settings):
        #Inherit from sprite properly
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #Load ship image from folder images
        self.image = pygame.image.load('images/bomb.bmp')
        #Get rect of image of image and screen..
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        #Start ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Check for movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False
        #Store ship position in variables...
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        self.update_position()

    def move_ship(self):
        #Move ship according to direction..
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ai_settings.ship_speed
        if self.moving_up and  self.rect.top > 0.5 * self.ai_settings.screen_length:
            self.y -= self.ai_settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ai_settings.ship_speed
        self.update_position()

    def center_ship(self):
        """Center ship each time at the beginning of each game..."""
        self.rect.bottom = self.screen_rect.bottom


    def update_position(self):
        """Update position of ship..."""
        if self.moving_right or self.moving_left:
            self.rect.centerx = self.x
        if self.moving_up or self.moving_down:
            self.rect.centery = self.y

    def blitme(self):
        """Draw ship on screen..."""
        self.screen.blit(self.image, self.rect)