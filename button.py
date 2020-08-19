import pygame.font

class Button:
    """Create a class to manage button..."""
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.ai_settings = ai_settings
        #Get rect of screen
        self.screen_rect = self.screen.get_rect()
        #Button physical dimension..
        self.width, self.height = 200, 50
        self.color = 120, 130, 140
        self.font = pygame.font.SysFont(None, 48, True, True)
        #Create a button at 0, 0 and set to designated position
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #Text color
        self.text_color = (20, 30, 40)
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Render msg in form of image..."""
        self.msg_image = self.font.render(msg, True, self.text_color , self.color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center

    def draw_button_msg(self):
        """Draw button and type message to it"""
        pygame.draw.rect(self.screen, self.ai_settings.bg_color, self.rect )
        self.screen.blit(self.msg_image, self.msg_rect)


