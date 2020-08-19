import pygame
from pygame.locals import *
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from score_board import Scoreboard
from Congratulations import CongratulatoryMessage

def run_game():
    pygame.init()
    #Call instance for class Settings...
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_length), RESIZABLE, 32, 32)
    pygame.display.set_caption("Alien_invasion")
    #Call instance for alien
    aliens = Group()
    #Call group for alien bullets
    alien_bullets = Group()
    #Call instance for ship...
    ship = Ship(screen, ai_settings)
    #Call instance for game_stas...
    stats = GameStats(ai_settings)
    #Call instance for button...
    button = Button(ai_settings, screen, "Play")
    #Call instance for score_board...
    sb = Scoreboard(screen, stats, ai_settings)
    cc = CongratulatoryMessage(screen, stats, ai_settings)
    #Call group of bullet..
    bullets = Group()
    gf.create_fleet_of_aliens(screen, ai_settings, aliens, ship)
    #Start main loop for game
    while True:
        gf.check_events(ship, screen, ai_settings, bullets, stats, button, aliens, sb)
        gf.update_screen(screen, ai_settings, bullets, ship, gf, aliens, button, stats, sb)

        if stats.game_active:
            gf.check_fleet_edges(aliens, ai_settings)
            gf.update_aliens(aliens, ai_settings, ship, stats, screen, bullets)
            gf.detect_collisions(bullets, aliens, ai_settings, screen, ship, stats, sb)
            gf.check_fleet_bottom(aliens, screen, stats, bullets, ai_settings, ship, sb)





run_game()