import pygame
import sys

def run_game():
    #Init game, create scree object
    pygame.init()
    screen = pygame.display.set_caption('Alien Invasion')
    screen = pygame.display.set_mode((1200,800))
    
    #Start the main loop
    while True:
        
        #Listen to keyboard/mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
    #Update screen every turn of the main cycle
        pygame.dysplay.flip()

run_game()