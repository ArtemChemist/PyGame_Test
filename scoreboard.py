import pygame
import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.scrn = screen
        self.scrn_rect = screen.get_rect()
        self.ai_set = ai_settings
        self.stats = stats
        self.ships = Group()
        #Set up the font
        self.font = pygame.font.SysFont(None, 48)
        self.txt_color = (30,30,30)

        #Prep the initial score txt-image
        self.prep_score()
        self.prep_level()
        self.prep_hi_score()

        self.prep_ships()

    def prep_score(self):
        self.rounded_score = int(round(self.stats.score))
        score_str = "Score: {:,}".format(self.rounded_score)
        self.score_img = self.font.render(score_str,True, self.txt_color, self.ai_set.bcgr_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.scrn_rect.right-30
        self.score_rect.top = self.scrn_rect.top+10
    
    def prep_hi_score(self):
        hiscore_str = "Top score: {:,}".format(self.stats.hi_score)
        self.hi_score_img = self.font.render(hiscore_str,True, self.txt_color, self.ai_set.bcgr_color)
        self.hi_score_rect = self.hi_score_img.get_rect()
        self.hi_score_rect.right = self.lvl_rect.left-30
        self.hi_score_rect.top = self.scrn_rect.top+10

    def prep_level(self):
        lvl_str = "Level: {:,}".format(self.stats.level)
        self.lvl_img = self.font.render(lvl_str,True, self.txt_color, self.ai_set.bcgr_color)
        self.lvl_rect = self.lvl_img.get_rect()
        self.lvl_rect.right = self.score_rect.left-100
        self.lvl_rect.top = self.scrn_rect.top+10
    
    def prep_ships(self):
        self.ships.empty()
        for ship_num in range (self.stats.ships_left):
            ship = Ship(self.scrn, self.ai_set)
            ship.rect.x = 10 + ship_num*ship.rect.width
            ship.rect.top = self.scrn_rect.top+10
            self.ships.add(ship)

    def show(self):
        self.scrn.blit(self.score_img, self.score_rect)
        self.scrn.blit(self.hi_score_img, self.hi_score_rect)
        self.scrn.blit(self.lvl_img, self.lvl_rect)
        self.ships.draw(self.scrn)

