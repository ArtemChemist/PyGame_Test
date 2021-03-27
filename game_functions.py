import sys
import pygame
from bullet import Bullet
from pygame.sprite import Group
import settings
from alien import Alien
from time import sleep

def check_events(ai_set, screen, ship, bullets):
    """
    Respond to keyboard and mouse
    Returns
    -------
    None.
    """
    # Scroll through all events that wee risen
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Quit if user asked to
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            handle_key_down(ai_set, screen, event, ship, bullets)
        elif event.type == pygame.KEYUP:
            handle_key_up(event, ship)  

def handle_key_down(ai_set, screen, event_to_handle,ship, bullets):

    """
    Respond to keypresses
    Returns
    -------
    None.
    """
    if event_to_handle.key == pygame.K_RIGHT:   #Go right
        ship.moving_r = True
    elif event_to_handle.key == pygame.K_LEFT:  #Go left
        ship.moving_l = True
    elif event_to_handle.key == pygame.K_SPACE:  #make a new bullet
        fire(ai_set,screen,ship,bullets)
    elif event_to_handle.key == pygame.K_q:      #quit if required
        sys.exit()

def handle_key_up(event_to_handle,ship):
    """
    Respond to key releases
    Returns
    -------
    None.
    """            
    if event_to_handle.key == pygame.K_RIGHT: #Go right
        ship.moving_r = False
    if event_to_handle.key == pygame.K_LEFT:  #Go left
        ship.moving_l = False   

def update_screen(ai_set, screen, ship, bullets,aliens):
    """
    Update images on the screen and flip to the new screen

    Parameters
    ----------
    ai_set : Settings
        Game settings
    screen : pygame.display
        main game window
    ship : Ship
        Player's ship
    bullets : Group
        Bullets fied from the ship
    alien : Alien
        Alien
    Returns
    -------
    None.

    """
    screen.fill(ai_set.bcgr_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets:  #Redraw all bullets
        bullet.draw()
    pygame.display.flip()

def update_bullets(ai_set, screen,bullets, aliens):
    bullets.update()                                #Update group of bullets
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if(len(aliens)==0):
        bullets.empty()
        make_fleet(ai_set, screen, aliens)
    for bullet in bullets:
        if bullet.rect.bottom<0:
            bullets.remove(bullet)

def fire(ai_set, screen, ship,bullets):
    if(len(bullets)<ai_set.bul_allowed):
        new_bullet = Bullet(ai_set,screen,ship)
        bullets.add(new_bullet)

def get_number_aliens_raw(ai_set):
    alien = Alien(ai_set)
    width = alien.rect.width
    availabel_space_x =  ai_set.scrn_width - 2*width
    return availabel_space_x//(2*width)

def get_number_aliens_column(ai_set=settings.Settings()):
    alien = Alien(ai_set)
    hight = alien.rect.height
    availabel_space_y =  ai_set.scrn_hight - 3*hight
    return availabel_space_y//(2*hight)

def make_fleet(ai_set, screen=pygame.Surface((1200,800)), aliens = Group()):
    aliens_in_raw = get_number_aliens_raw(ai_set)
    aliens_in_column = get_number_aliens_column(ai_set)
    for k in range (aliens_in_column):
        for i in range(aliens_in_raw):
            if len(aliens)<ai_set.max_aliens:
                alien = Alien(ai_set,screen)
                alien.x = alien.rect.width + 2*alien.rect.width*i
                alien.rect.x = alien.x
                alien.y = alien.rect.height + 2*alien.rect.height*k
                alien.rect.y = alien.y
                aliens.add(alien)

def updat_aliens(ai_set, screen, aliens, ship, stats, bullets):
    check_fleet_bottom(ai_set, stats, screen,ship,aliens, bullets)
    check_fleet_edges(ai_set, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_set, stats, screen,ship,aliens, bullets)

def check_fleet_edges(ai_set, aliens):
    for alien in aliens:
        if alien.check_edges():
            ai_set.fleet_dir *= -1
            for alien in aliens:
                alien.y+=ai_set.alien_drop_speed
                alien.rect.y = alien.y
            break

def check_fleet_bottom(ai_set, stats, screen,ship,aliens, bullets):
    scrn_rect = screen.get_rect()
    for alien in aliens:
        if(alien.rect.bottom >= scrn_rect.bottom):
            ship_hit(ai_set, stats, screen,ship,aliens, bullets)
            break

def ship_hit(ai_set, stats, screen,ship,aliens, bullets):
    if stats.ships_left>0:
        stats.ships_left-=1
        aliens.empty()
        bullets.empty()
        make_fleet(ai_set, screen, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.active = False


