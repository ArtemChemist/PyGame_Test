import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bulet, self).__init__()
        self.set = ai_settings
        self.screen = screen


        self.rect = pygame.Rect(0,0,self.set.bullet_width, self.set.bullet_length)
        self.x = float(ship.rect.centerx)
        self.y = float(ship.rect.top)

        self.color = ai_settings.bulet_color
        self.speed = ai_settings.bullet_speed
       
        self.moving = False
