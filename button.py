import pygame
class Button():
    def __init__(self, ai_settings, screen=pygame.Surface((800, 600)), msg = ''):
        #set up the screen where the button resides
        self.scrn = screen
        self.scrn_rect = screen.get_rect()

        #setup the button itself
        self.width = 200
        self.height = 50
        self.color = (0,255,0)
        self.txt_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        #Build button rect, then center it.
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.scrn_rect.center

        #prep message
        self.prep_msg(msg)

    #Need to render image fom message text
    def prep_msg(self,msg=""):
        #Use pygame function to render an image out of text
        self.msg_image = self.font.render(msg,True, self.txt_color,self.color)
        #Make a rect object from this image
        self.msg_image_rect = self.msg_image.get_rect()
        #Center the just made rect object of the text-image in the button. 
        self.msg_image_rect.center = self.rect.center
    
    def draw (self):
        #Fill the whole button with the bckgr color
        self.scrn.fill(self.color, self.rect)
        #Put the image of text on top of the background
        self.scrn.blit(self.msg_image, self.msg_image_rect)

