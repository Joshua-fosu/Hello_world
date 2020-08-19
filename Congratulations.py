import pygame.ftfont

class CongratulatoryMessage:
    """Congratulate user on playing the game..."""
    def __init__(self, screen, stats, ai_settings):
        #Attributing values
        self.screen = screen
        self.stats = stats
        self.ai_settings = ai_settings
        #Get rect of screen...
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont(None, 50)
        self.color = 0, 0, 0
        self.prep_message_high()
        self.prep_message_low()

    def prep_message_high(self):
        """Print this message if user had higher than high score"""
        self.msg = "Congratulations!!!" + "\n"
        self.msg += "You have beat the current high score..."
        self.msg += f"The new high score is {self.stats.high_score}."
        self.msg_image = self.font.render(self.msg, True, self.color,
                                          self.ai_settings.bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.screen_rect.centerx
        self.msg_image_rect.top = 200

    def prep_message_low(self):
        """Print this message if user had lower than the high score"""
        self.info = "That was a good performance"
        self.info += "Try to beat the high score next time..."
        self.info_image = self.font.render(self.info, True, self.color,
                                           self.ai_settings.bg_color)
        self.info_rect = self.info_image.get_rect()
        self.info_rect.centerx = self.screen_rect.centerx
        self.info_rect.top = 200

    def show_higher(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def show_lower(self):
        self.screen.blit(self.info_image, self.info_rect)