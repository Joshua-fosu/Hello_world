import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep
import json

def check_events(ship, screen, ai_settings, bullets, stats, button,aliens, sb):
    #Check for various events and respond accordingly...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            get_high_score(stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, screen, ai_settings, bullets, stats, aliens, sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button.rect.collidepoint(mouse_x, mouse_y):
                play_game(stats, aliens, bullets, ship, screen, ai_settings, sb)

def check_keydown_events(event, ship, screen, ai_settings, bullets, stats, aliens, sb):
    #Check for key presses...
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_SPACE:
        add_bullet(screen, ai_settings, ship, bullets)
    elif event.key == pygame.K_q:
        get_high_score(stats)
        sys.exit()
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_p:
        play_game(stats, aliens, bullets, ship, screen, ai_settings, sb)

def check_keyup_events(event, ship):
    #Check for key releases...
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def add_bullet(screen, ai_settings, ship, bullets):
    #Add new bullet if allowed bullets has not been reached...
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(screen, ai_settings, ship)
        bullets.add(new_bullet)

def remove_old_bullet(bullets):
    for bullet in bullets.sprites():
        if bullet.rect.top < 0:
            bullets.remove(bullet)

def update_screen(screen, ai_settings, bullets, ship, gf, aliens, button, stats, sb):
    """Draw components and update screen each time..."""
    screen.fill(ai_settings.bg_color)
    #Draw score to screen
    sb.draw_score()
    # Draw ship on screen...
    ship.blitme()
    # Move ship
    ship.move_ship()
    aliens.draw(screen)
    # Draw all bullets in bullet group...
    draw_all_bullets(bullets)
    bullets.update()

    check_fleet_edges(aliens, ai_settings)
    gf.remove_old_bullet(bullets)
    # Draw play button to screen
    if not stats.game_active:
        button.draw_button_msg()
        pygame.mouse.set_visible(True)
    # Draw most current screen...
    pygame.display.flip()

def draw_all_bullets(bullets):
    """Draw all bullets in sprites..."""
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def create_fleet_of_aliens(screen, ai_settings, aliens, ship):
    """Create fleet of aliens.."""
    alien = Alien(screen, ai_settings)
    number_of_aliens_x = get_number_of_aliens_x(ai_settings, alien)
    number_of_aliens_y = get_number_of_rows(ai_settings, ship)
    #create fleet..
    for row_number in range(number_of_aliens_y):
        for alien_number in range(number_of_aliens_x):
            create_alien(screen, ai_settings, aliens, alien_number, row_number)

def create_alien(screen, ai_settings, aliens, alien_number, row_number):
    """Add every alien to aliens group..."""
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 3 * alien_number * alien_width
    alien.y = alien.rect.height + 2 * row_number * alien.rect.height
    alien.rect.y = alien.y
    alien.rect.x = alien.x
    aliens.add(alien)

def get_number_of_aliens_x(ai_settings, alien):
    # Call for alien...
    alien_width = alien.rect.width
    available_space = ai_settings.screen_width / (3 * alien_width)
    number_of_aliens_x = int(available_space)
    return number_of_aliens_x

def check_fleet_edges(aliens, ai_settings):
    """Check for edges of aliens.."""
    for alien in aliens.sprites():
        if alien.check_edges():
            drop_fleet(aliens, ai_settings)
            change_fleet_direction(ai_settings)
            break

def change_fleet_direction(ai_settings):
    """Change direction of fleet of aliens.."""
    ai_settings.alien_direction *= -1


def update_aliens(aliens, ai_settings, ship, stats, bullets, screen):
    check_fleet_edges(aliens, ai_settings)
    aliens.update()

def get_number_of_rows(ai_settings, ship):
    """return number of available rows..."""
    available_space_y = ai_settings.screen_length - ship.rect.height
    number_of_rows = available_space_y / (3 * ship.rect.height)
    return int(number_of_rows)

def drop_fleet(aliens, ai_settings):
    """Drop fleet on reaching edge of screen..."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

def detect_collisions(bullets, aliens, ai_settings, screen, ship, stats, sb):
    """Detect collisions of bullet with alien ship..."""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #Update score..
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_score * len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)
    if len(aliens) == 0:
        increase_level(stats, sb)
        level_up(ai_settings)
        create_fleet_of_aliens(screen, ai_settings, aliens, ship)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(stats, aliens, bullets, screen, ai_settings, ship, sb)


def ship_hit(stats, aliens, bullets, screen, ai_settings, ship, sb):
    #Check if all lives has been spent
    if stats.ship_lives > 0:
        """respond to alien-ship hit act..."""
        #Deduct lives from ship_lives...
        stats.ship_lives -= 1
        sb.prep_ship(screen, ai_settings)

        #Empty alien...
        aliens.empty()

        #Empty bullets...
        bullets.empty()

        #Reset fleet...
        create_new_fleet(screen, ai_settings, aliens, ship)

        #pause game for a while...
        sleep(0.5)

        #Center ship
        ship.center_ship()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def create_new_fleet(screen, ai_settings, aliens, ship):
    """Create new fleet..."""
    create_fleet_of_aliens(screen, ai_settings, aliens, ship)

def check_fleet_bottom(aliens, screen, stats, bullets, ai_settings, ship, sb):
    """Act as ship_hit if fleet reach..."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom > screen_rect.bottom:
            ship_hit(stats, aliens, bullets, screen, ai_settings, ship, sb)

def play_game(stats, aliens, bullets, ship, screen, ai_settings, sb):
    #Get high score from json
    file_name = "High score.json"
    try:
        with open(file_name) as f_obj:
            score = json.load(f_obj)
            stats.high_score = score
            sb.prep_high_score()
    except FileNotFoundError:
         pass
    #Reset stats
    stats.reset_stats()
    #Make pointer not visible
    pygame.mouse.set_visible(False)

    #Enter game mode...
    stats.game_active = True

    #Empty group list
    aliens.empty()
    bullets.empty()

    #Center ship
    ship.center_ship()

    #Create new fleet
    create_new_fleet(screen, ai_settings, aliens, ship)

def check_high_score(stats, sb):
    """Check if high score has been broken..."""
    if stats.score >= stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def level_up(ai_settings):
    """Increase level each time..."""
    ai_settings.alien_score *= ai_settings.level_up
    ai_settings.alien_speed *= ai_settings.level_up
    ai_settings.fleet_drop_speed *= ai_settings.level_up
    ai_settings.bullet_speed *= ai_settings.level_up
    ai_settings.ship_speed *= ai_settings.level_up

def increase_level(stats, sb):
    """Increase level each time..."""
    stats.levels += 1
    sb.prep_levels()

def get_high_score(stats):
    file_name = "High score.json"
    with open(file_name, 'w') as f_obj:
        json.dump(stats.high_score, f_obj)



