import sys
import pygame

def eventCheck(ship):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:
        ship.rect.centerx -= 1

    if keys_pressed[pygame.K_RIGHT]:
        ship.rect.centerx += 1


def tick(config, screen, ship):

    screen.fill(config.bg_color)
    ship.blitme()
    pygame.display.flip()



















