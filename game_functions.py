import sys
import pygame

def check_events():
    """
    Respond to keyboard and mous

    Returns
    -------
    None.

    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
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