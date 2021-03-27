class Settings():

    def __init__(self):
        
        #Main screen
        self.scrn_width = 1200 # Main screen witdth
        self.scrn_hight = 800 # # Main screen height
        self.bcgr_color = (20,0,20) # Main screen witdth
        self.scrn_size = (self.scrn_width, self.scrn_hight)
        
        #Ship
        self.ship_speed = 2.2
        self.ship_limit = 3

        #Bullets
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_length = 15
        self.bulet_color = (180,0,40)
        self.bul_allowed = 3

        #Aliens
        self.alien_speed = 1
        self.alien_drop_speed = 100
        self.max_aliens = 10
        self.fleet_dir = 1



