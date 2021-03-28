class Settings():

    def __init__(self):
        #Initialize static settings
        #Main screen
        self.scrn_width = 1200 # Main screen witdth
        self.scrn_hight = 800 # # Main screen height
        self.bcgr_color = (20,0,20) # Main screen witdth
        self.scrn_size = (self.scrn_width, self.scrn_hight)
        
        #Ship
        self.ship_limit = 3

        #Bullets
        self.bullet_width = 3
        self.bullet_length = 15
        self.bulet_color = (180,0,40)
        self.bul_allowed = 10

        #Aliens
        self.alien_drop_speed = 10
        self.max_aliens = 10

        self.speedup_scale = 2
        self.initialize_dynamic_settings()

        #Initialize dynamic settings
    def initialize_dynamic_settings(self):
        self.bullet_speed = 5
        self.alien_speed = 1
        self.ship_speed = 2
        self.fleet_dir = 1
    
    def increase_sped(self):
        self.bullet_speed *= self.speedup_scale
        self.alien_drop_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale




