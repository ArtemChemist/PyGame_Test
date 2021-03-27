class GameStats():
    def __init__(self, ai_settings):
        self.set = ai_settings
        self.active = True
        self.ships_left= self.set.ship_limit
        self.resetstats()
    def resetstats(self):
        self.ships_left = self.set.ship_limit
