import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen,ai_set):
        super().__init__()
        #Load the image and get its rectangle
        self.screen = screen
        self.image = pygame.image.load('Img/spaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.moving_r = False
        self.moving_l = False
        self.set = ai_set
        self.center = float(self.rect.centerx)

        # Start the new ship at the bottom center of the screen
        self.center_ship()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        if self.moving_r and (self.center<self.screen_rect.right):
            self.center+=self.set.ship_speed
        if self.moving_l and (self.center>self.screen_rect.left):
            self.center-=self.set.ship_speed
        self.rect.centerx = int(self.center)
    
    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom