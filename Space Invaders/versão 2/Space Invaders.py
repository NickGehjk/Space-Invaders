import sys
import pygame
from configuracoes import *
from nave import *
import funcoesDoJogo as func
from pygame.sprite import Group

def run_game():

    pygame.init()
    config = Settings()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
    ship = Ship(screen)
    bullets = Group()

    pygame.display.set_caption('Space Invaders')

    while True:

        func.eventCheck(config,screen,ship,bullets)
        func.tick(config,screen,ship,bullets)

        bullets.update()

run_game()


















