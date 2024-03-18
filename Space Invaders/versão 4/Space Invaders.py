import sys
import pygame
from configuracoes import *
from nave import *
import funcoesDoJogo as func
from pygame.sprite import Group
from alien import *
from button import *
from imagemFundo import *

def run_game():

    pygame.init()
    config = Settings()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))

    pygame.display.set_caption('Space Invaders')

    ship = Ship(screen)
    bullets = Group()
    #alien = Alien(config, screen)
    aliens = Group()

    func.createFleet(config,screen,aliens)

    while True:

        func.eventCheck(config,screen,ship,aliens,bullets)
        func.tick(config,screen,ship,aliens,bullets)
        collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
        bullets.update()
        func.atualizaAliens(config,aliens)

        if len(aliens) == 0:
            func.createFleet(config,screen,aliens)
            func.alienSpeedUp(config)

run_game()


























