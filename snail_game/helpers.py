import pygame

from snail_game.player import Player


def sprites_collided(
    player: Player,
    obstacle_group: pygame.sprite.Group,  # type: ignore
) -> bool:
    if pygame.sprite.spritecollide(player, obstacle_group, False):  # type: ignore
        obstacle_group.empty()
        return True
    else:
        return False
