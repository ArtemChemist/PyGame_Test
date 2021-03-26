import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.set = ai_settings
        self.screen = screen


        self.rect = pygame.Rect(0,0,self.set.bullet_width, self.set.bullet_length)
        self.x = float(ship.rect.centerx)
        self.y = float(ship.rect.top)

        self.color = ai_settings.bulet_color
        self.speed = ai_settings.bullet_speed
       
        self.moving = False
    def update():
        """ moves bullet image once it's fired"""
        self.y -=self.speed
        self.rect.y = init(self.y)
    def draw (self):
        pygem.draw.rect(self.screen, self.color, self.rect)
