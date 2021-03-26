import pygame
class Ship():
    def __init__(self, screen):
        
        #Load the image and get its rectangle
        self.screen = screen
        self.image = pygame.image.load('Img/spaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        # Start the new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)