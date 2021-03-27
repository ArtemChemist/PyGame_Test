import sys
import pygame
from bullet import Bullet

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
        new_bullet = Bullet(ai_set,screen,ship)
        bullets.add(new_bullet)

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

def update_screen(ai_set, screen, ship, bullets):
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

    Returns
    -------
    None.

    """
    screen.fill(ai_set.bcgr_color)
    ship.blitme()
    for bullet in bullets:  #Redraw all bullets
        bullet.draw()
    pygame.display.flip()
