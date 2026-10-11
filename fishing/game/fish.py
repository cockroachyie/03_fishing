"""
Fish: swims horizontally at a fixed depth, wrapping around when it
exits the screen. SmallFish and BigFish are the two fish types from
Task 2.
"""

import pygame


class Fish:
    def __init__(self, x, y, speed, width=36, height=18, point_value=10, color=(80, 180, 220)):
        self.x = float(x)
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.point_value = point_value
        self.color = color

    def update(self, screen_width):
        self.x += self.speed
        if self.speed > 0 and self.x > screen_width:
            self.x = -self.width
        elif self.speed < 0 and self.x < -self.width:
            self.x = screen_width

    def get_rect(self):
        return pygame.Rect(
            int(self.x - self.width / 2), int(self.y - self.height / 2),
            self.width, self.height,
        )


class SmallFish(Fish):
    """Small, slow, low-value, green fish."""

    def __init__(self, x, y, speed):
        super().__init__(
            x, y, speed,
            width=24, height=12,
            point_value=5,
            color=(60, 200, 80),
        )


class BigFish(Fish):
    """Big, fast, high-value, red fish."""

    def __init__(self, x, y, speed):
        super().__init__(
            x, y, speed,
            width=52, height=26,
            point_value=25,
            color=(220, 60, 60),
        )
