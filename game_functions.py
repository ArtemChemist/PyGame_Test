import sys
import pygame

def check_events(ship):
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
            handle_key_down(event, ship)
        elif event.type == pygame.KEYUP:
            handle_key_up(event, ship)  

def handle_key_down(event_to_handle,ship):

    """
    Respond to keypresses
    Returns
    -------
    None.
    """
    if event_to_handle.key == pygame.K_RIGHT: #Go right
        ship.moving_r = True
    if event_to_handle.key == pygame.K_LEFT:  #Go left
        ship.moving_l = True

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

def update_screen(ai_set, screen, ship):
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
    pygame.display.flip()
