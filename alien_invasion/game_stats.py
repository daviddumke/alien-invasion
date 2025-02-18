import pygame
from .settings import Settings

class GameStats:
    """Class to manage game statistics."""

    def __init__(self, ai_game):
        """Initialize the game statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Reset all game statistics."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
