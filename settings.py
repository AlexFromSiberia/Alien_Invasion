class Settings:
    """ Класс для хранения всех настроек игры """
    def __init__(self):
        """ All the GAME settings """

        # Screen options
        self.full_screen_mode = False
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40, 40, 40)

        # ship settings
        self.ship_limit = 3

        # Bullets settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 60, 60)
        self.bullets_allowed = 3

        # Aliens
        self.fleet_drop_speed = 10

        # Change difficulty
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # How quickly the alien point values increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

