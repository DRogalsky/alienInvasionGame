class Settings:
    """a class to store all the settings for Alien Invasion"""

    def __init__(self):
        """initialize the games settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 1.5