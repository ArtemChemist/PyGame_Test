import pygame
import pygame.font


class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.scrn = screen
        self.scrn_rect = screen.get_rect()
        self.ai_set = ai_settings
        self.stats = stats
        #Set up the font
        self.font = pygame.font.SysFont(None, 48)
        self.txt_color = (30,30,30)

        #Prep the initial score txt-image
        self.prep_score()

    def prep_score(self):
        rounded_score = int(round(self.stats.score))
        score_str = "{:,}".format(rounded_score)
        self.score_img = self.font.render(score_str,True, self.txt_color, self.ai_set.bcgr_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.scrn_rect.right-20
        self.score_rect.top = self.scrn_rect.top+20
    def show(self):
        self.scrn.blit(self.score_img, self.score_rect)

