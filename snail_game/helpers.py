import pygame
from snail_game.constants import (
    BLACK_COLOR,
    GAMEOVER_COLOR,
    PLAY_AGAIN,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)

from snail_game.player import Player


def sprites_collided(
    player: Player,
    obstacle_group: pygame.sprite.Group,  # type: ignore
) -> bool:
    if pygame.sprite.spritecollide(player, obstacle_group, False):  # type: ignore
        return True
    else:
        return False


def player_wins(player: Player) -> bool:
    return player.victory


def draw_end_game_screen(screen: pygame.Surface, main_text: str) -> None:
    gameover_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameover_surface.fill(GAMEOVER_COLOR)
    screen.blit(gameover_surface, (0, 0))

    font = pygame.font.Font(None, 50)
    text = font.render(main_text, False, BLACK_COLOR)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)
    screen.blit(text, textRect)

    font_play_again = pygame.font.Font(None, 20)
    text_play_again = font_play_again.render(PLAY_AGAIN, False, BLACK_COLOR)
    textRect_play_again = text_play_again.get_rect()
    textRect_play_again.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)
    screen.blit(text_play_again, textRect_play_again)


def reset_game_state(player: Player, obstacle_group: pygame.sprite.Group) -> None:  # type: ignore
    obstacle_group.empty()  # type: ignore
    player.reset()
