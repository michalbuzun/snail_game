from typing import List
import pygame

from snail_game.constants import HORIZON_HEIGHT

PLAYER_HEIGHT = 70
PLAYER_WIDTH = 40
PLAYER_DISTANCE_FROM_LEFT = 80
PLAYER_JUMP_HEIGHT = 100


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (PLAYER_DISTANCE_FROM_LEFT, HORIZON_HEIGHT)

    def update(self, events: List[pygame.event.Event]) -> None:  # type: ignore
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.rect.midbottom = (
                        PLAYER_DISTANCE_FROM_LEFT,
                        PLAYER_JUMP_HEIGHT,
                    )
