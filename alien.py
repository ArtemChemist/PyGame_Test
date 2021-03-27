import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.set = ai_settings
        
        #Load the image
        self.image = pygame.image.load('Img/ufo.png')
        self.rect = self.image.get_rect()

        #Start the new alien at the to left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the exact position
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
