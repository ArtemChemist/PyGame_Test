import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
import alien as al

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

    #Make a group of bullets
    bullets = Group()

    #Make an alien
    alien = al.Alien(ai_set,screen)

    #Start the main loop
    while True:
        #Every turn of the main cycle
        gf.check_events(ai_set, screen, ship, bullets)  #Listen to keyboard/mouse events
        ship.update()                                   #Update ship position on te screen
        gf.update_bullets(bullets)
        gf.update_screen(ai_set, screen, ship, bullets, alien) #Update screen

run_game()
