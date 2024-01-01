import pygame
from snail_game.constants import (
    END_GAME_TEXT,
    END_GAME_VICTORY,
    FPS,
    GAME_TITLE,
    GROUND_COLOR,
    HORIZON_HEIGHT,
    RESPAWN_TIME,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SKY_COLOR,
)
from snail_game.helpers import (
    draw_end_game_screen,
    player_wins,
    reset_game_state,  # type: ignore
    sprites_collided,  # type: ignore
)

from snail_game.obstacle import Obstacle

from snail_game.player import Player


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

clock = pygame.time.Clock()

obstacle_respawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_respawn_timer, RESPAWN_TIME)

sky_surface = pygame.Surface((800, 300))
sky_surface.fill(SKY_COLOR)

ground_surface = pygame.Surface((800, 100))
ground_surface.fill(GROUND_COLOR)

player = Player()
player_group = pygame.sprite.GroupSingle()  # type: ignore
player_group.add(player)  # type: ignore

obstacle = Obstacle()
obstacle_group = pygame.sprite.Group()  # type: ignore
obstacle_group.add(obstacle)  # type: ignore

running = True
game_active = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if game_active:
        for event in events:
            if event.type == obstacle_respawn_timer:
                obstacle_group.add(Obstacle())  # type: ignore

        screen.blit(ground_surface, (0, HORIZON_HEIGHT))
        screen.blit(sky_surface, (0, 0))

        player_group.update(events)
        player_group.draw(screen)

        obstacle_group.update()
        obstacle_group.draw(screen)

        if sprites_collided(player, obstacle_group):
            reset_game_state(player, obstacle_group)
            game_active = False

        if player_wins(player):
            reset_game_state(player, obstacle_group)
            game_active = False

    else:
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                game_active = True

        if player.victory:
            draw_end_game_screen(screen, END_GAME_VICTORY)
        else:
            draw_end_game_screen(screen, END_GAME_TEXT)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
