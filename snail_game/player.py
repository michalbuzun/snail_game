from typing import List
import pygame
from datetime import datetime

from snail_game.constants import HORIZON_HEIGHT, SCREEN_WIDTH

PLAYER_HEIGHT = 70
PLAYER_WIDTH = 40
PLAYER_DISTANCE_FROM_LEFT = 80
PLAYER_JUMP_HEIGHT = 100


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.gravity = 0
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (PLAYER_DISTANCE_FROM_LEFT, HORIZON_HEIGHT)
        self.victory = False

    def update(self, events: List[pygame.event.Event]) -> None:  # type: ignore
        self.gravity += int(datetime.now().microsecond % 13 == 0)
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.rect.bottom = PLAYER_JUMP_HEIGHT

                    self._reset_gravity()

        if self.rect.bottom < HORIZON_HEIGHT:
            self.rect.bottom += 1 + self.gravity

        if self.rect.bottom > HORIZON_HEIGHT:
            self.rect.bottom = HORIZON_HEIGHT

        # move player forward
        self.rect.right += 1

        # end of the game player out of the screen
        if self.rect.right >= SCREEN_WIDTH + PLAYER_WIDTH:
            print("game won by player")

    def _reset_gravity(self) -> None:
        self.gravity = 0
