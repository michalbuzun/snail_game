import pygame
from snail_game.constants import (
    FPS,
    GAME_TITLE,
    GROUND_COLOR,
    HORIZON_HEIGHT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SKY_COLOR,
)

from snail_game.player import Player


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption(GAME_TITLE)

clock = pygame.time.Clock()

sky_surface = pygame.Surface((800, 300))
sky_surface.fill(SKY_COLOR)

ground_surface = pygame.Surface((800, 100))
ground_surface.fill(GROUND_COLOR)

player = Player()
player_group = pygame.sprite.GroupSingle()  # type: ignore
player_group.add(player)  # type: ignore

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.blit(ground_surface, (0, HORIZON_HEIGHT))
    screen.blit(sky_surface, (0, 0))

    player_group.update(events)
    player_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
