import sys
import pygame
from configuracoes import *
from nave import *
import funcoesDoJogo as func

def run_game():

    pygame.init()
    config = Settings()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
    ship = Ship(screen)

    pygame.display.set_caption('Space Invaders')

    while True:

        func.eventCheck(ship)
        func.tick(config,screen,ship)

run_game()




















