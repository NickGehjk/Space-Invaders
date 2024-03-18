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

    espaco = config.screen_width - 2 * alien_width
    numeroDeAliens = 14

    for numero in range(numeroDeAliens):
        alien = Alien(config, screen)

        alien.x = alien_width + 2 * alien_width * numero
        alien.rect.x = alien.rect.x + alien.x
        aliens.add(alien)


#def checaFrota(config, aliens):
    #for alien in aliens.sprites():
        #if alien.checaBordas():
            #mudaDirecaoDaTropa(config, aliens)
            #break

#def mudaDirecaoDaTropa(config, aliens):
    #for alien in aliens.sprites():
        #alien.rect.y += config.fleet_drop_speed
    #config.fleet_direction *= -1

#def atualizaAliens(config, aliens):

    #checaFrota(config, aliens)
    #aliens.update()


















