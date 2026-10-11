"""
Hook: the player's fishing hook. Moves only vertically, at a fixed
horizontal position. The player controls it directly - holding the
down key (S / Down arrow) moves it toward the pond floor, holding the
up key (W / Up arrow) moves it back toward the surface. The one
exception is right after a catch: the hook ignores input and
automatically retracts to the surface so the catch can be scored (see
catch_fish()).
"""

import pygame

IDLE = "idle"
RETRACTING = "retracting"


class Hook:
    def __init__(self, x, surface_y, max_depth_y, speed=4, width=14, height=14):
        self.x = x
        self.surface_y = surface_y
        self.max_depth_y = max_depth_y
        self.y = surface_y
        self.speed = speed
        self.width = width
        self.height = height
        self.state = IDLE

    def move_down(self):
        """Player is holding the down key."""
        if self.state == IDLE:
            self.y = min(self.y + self.speed, self.max_depth_y)

    def move_up(self):
        """Player is holding the up key."""
        if self.state == IDLE:
            self.y = max(self.y - self.speed, self.surface_y)

    def update(self):
        if self.state == RETRACTING:
            self.y -= self.speed
            if self.y <= self.surface_y:
                self.y = self.surface_y
                self.state = IDLE

    def catch_fish(self):
        """Called when a fish has been caught - immediately head back up."""
        self.state = RETRACTING

    def get_rect(self):
        return pygame.Rect(
            int(self.x - self.width / 2), int(self.y - self.height / 2),
            self.width, self.height,
        )
