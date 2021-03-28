import pygame
from time import sleep
from pygame.sprite import Group

from game_stats import GameStats
import button as bt
from settings import Settings
from ship import Ship
import game_functions as gf
from scoreboard import Scoreboard

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

    #Make stats instance to store game stats
    stats = GameStats(ai_set)

    #Make a ship
    ship = Ship(screen, ai_set)

    #Make a group of bullets
    bullets = Group()

    #Make an alien
    aliens = Group()
    gf.make_fleet(ai_set, screen, aliens)

    #Make play button
    buttonPlay = bt.Button(ai_set, screen, 'PLAY')

    #Make a scoreboard
    sb = Scoreboard(ai_set, screen, stats)

    #Start the main loop
    while True:
        #Every turn of the main cycle
        gf.check_events(ai_set, stats, screen, sb, ship, bullets, buttonPlay,aliens)  #Listen to keyboard/mouse events
        if stats.active:
            ship.update()                                   #Update ship position on te screen
            gf.update_bullets(ai_set, screen, stats, sb, bullets, aliens)
            gf.updat_aliens(ai_set,screen, aliens,ship,stats, bullets,sb)
        gf.update_screen(ai_set, screen, stats, ship, bullets, aliens, buttonPlay, sb) #Update screen

run_game()
