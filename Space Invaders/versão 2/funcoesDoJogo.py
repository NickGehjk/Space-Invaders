import sys
import pygame
from bullet import Bullet

def eventCheck(config, screen, ship, bullets):

    keys_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                novoProj = Bullet(config, screen, ship)
                bullets.add(novoProj)

    if keys_pressed[pygame.K_LEFT]:
        ship.rect.centerx -= 1

    if keys_pressed[pygame.K_RIGHT]:
        ship.rect.centerx += 1


def tick(config, screen, ship, bullets):

    screen.fill(config.bg_color)
    for b in bullets.sprites():
        b.desenhaProj()
    ship.blitme()
    pygame.display.flip()

















