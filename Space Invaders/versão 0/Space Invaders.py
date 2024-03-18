import sys
import pygame
from configuracoes import *
from nave import *

def run_game():

    pygame.init()
    configuracoesDoJogo = Settings()

    screen = pygame.display.set_mode(
        (configuracoesDoJogo.screen_width, configuracoesDoJogo.screen_height))


    pygame.display.set_caption('Space Invaders')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(configuracoesDoJogo.bg_color)
        #desenha a nave
        ship.blitme()
        pygame.display.flip()

run_game()