import pygame

class Settings:
    """Manage all settings in game and characteristics of elements..."""
    def __init__(self):
        self.screen_width = 1300
        self.screen_length = 750
        self.bg_color = 255, 255, 255
        #Input bullet characteristics...
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = 0, 0, 0
        self.bullet_speed = 3
        self.bullets_allowed = 3
        #Input ship speed...
        self.ship_speed = 3
        self.ship_lives = 3
        #Input alien speed movements..
        self.alien_direction = 0.5
        self.alien_speed = 2
        self.fleet_drop_speed = 5
        self.alien_score = 50
        #Increase level by a set amount...
        self.level_up = 1.05