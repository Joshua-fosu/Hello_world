class GameStats:
    """Create a class to store game stats..."""
    def __init__(self, ai_settings):
        """command attributes... """
        self.ai_settings = ai_settings
        self.ship_lives = 3
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.levels = 0

    def reset_stats(self):
        """Reset stats on opening a new game..."""
        self.ship_lives = self.ai_settings.ship_lives

