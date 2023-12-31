from random import randint
import pygame

from snail_game.constants import HORIZON_HEIGHT

OBSTACLE_COLOR = "blue"
OBSTACLE_HEIGHT = 40
OBSTACLE_WIDTH = 70
OBSTACLE_POSITION_START = 800
OBSTACLE_POSITION_END = 1100


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(OBSTACLE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (
            randint(OBSTACLE_POSITION_START, OBSTACLE_POSITION_END),
            HORIZON_HEIGHT,
        )

    def update(self) -> None:  # type: ignore
        self.rect.right -= 4

        # to do: add killing obstacle if off the screen
