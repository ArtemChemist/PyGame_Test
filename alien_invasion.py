import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """
    Main game function

    Returns
    -------
    None.

    """
    #Init game, create screen object
    pygame.init()
    ai_set = Settings()
    pygame.display.set_caption('Alien Invasion')
    screen = pygame.display.set_mode(ai_set.scrn_size)

    #Make a ship
    ship = Ship(screen, ai_set)

    #Start the main loop
    while True:
        #Listen to keyboard/mouse events
        gf.check_events(ship)
        #Update ship position on te screen
        ship.update()
        #Update screen every turn of the main cycle
        gf.update_screen(ai_set, screen, ship)

run_game()
