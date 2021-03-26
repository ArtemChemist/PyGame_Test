import sys
import pygame

def check_events(ship):
    """
    Respond to keyboard and mous

    Returns
    -------
    None.

    """
    
    # Scroll through all events that wee risen
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Quit if user asked to
            sys.exit()
       
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: #Go right
                ship.moving_r = True
            if event.key == pygame.K_LEFT:  #Go left
                ship.moving_l = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT: #Go right
                ship.moving_r = False
            if event.key == pygame.K_LEFT:  #Go left
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