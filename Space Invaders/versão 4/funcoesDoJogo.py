import sys
import pygame
from bullet import *
from alien import *

def eventCheck(config, screen, ship, aliens, bullets):

    keys_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                newBullet = Bullet(config, screen, ship)
                bullets.add(newBullet)

    if keys_pressed[pygame.K_LEFT]:
        if ship.rect.left > 10:
            ship.rect.centerx -= 1

    if keys_pressed[pygame.K_RIGHT]:
        if ship.rect.right < 1190:
            ship.rect.centerx += 1


def tick(config, screen, ship, aliens, bullets):

    screen.fill(config.bg_color)

    for b in bullets.sprites():
        b.desenhaProj()

    ship.blitme()

    #alien.blitme()
    aliens.draw(screen)

    pygame.display.flip()

def createFleet(config, screen, aliens):

    alien = Alien(config, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    dispx = (config.screen_width - (2 * alien_width))
    dispy = (config.screen_height - (6 * alien_height))
    rows = int(dispy/(2.5*alien_height))

    numeroDeAliens = int(dispx/(2*alien_width))

    for e in range(rows):

        for numero in range(numeroDeAliens):
            alien = Alien(config, screen)

            alien.x = alien_width + 1.5 * alien_width * numero
            alien.rect.x = alien.rect.x + alien.x
            alien.rect.y = alien.rect.height + 2*alien.rect.height*e
            aliens.add(alien)

def mudaDirecaoDaTropa(config, aliens):
    for alien in aliens.sprites():
        alien.rect.y += config.alien_drop
    config.alien_dir *= -1

def checaFrota(config, aliens):
    for alien in aliens.sprites():
        if alien.checaBordas():
            mudaDirecaoDaTropa(config, aliens)
            break

def atualizaAliens(config, aliens):
    checaFrota(config, aliens)
    aliens.update()

def alienSpeedUp(config):
    config.alien_speed += 0.5


















