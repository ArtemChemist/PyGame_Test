class GameStats():
    def __init__(self, ai_settings):
        self.set = ai_settings
        self.active = False
        self.ships_left= self.set.ship_limit
        self.resetstats()
        self.hi_score = 0
    def resetstats(self):
        self.ships_left = self.set.ship_limit
        self.score = 0
