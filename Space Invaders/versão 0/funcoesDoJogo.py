import sys
import pygame

def checa_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def atualiza_tela(configuracoes, screen, ship):

    #atualiza as imagens na tela e alterna para uma nova tela
    screen.fill(configuracoesDoJogo.bg_color)
    #desenha a nave
    ship.blitme()
    #deixa a tela mais recente visível