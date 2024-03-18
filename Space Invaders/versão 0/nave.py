import pygame

class Ship():

    #inicializa a nave e coloca na poisção inicial
    def __init__(self, screen):

        #carregando a tela do jogo
        self.screen = screen
        #carregando imagem da nave
        self.image = pygame.image.load('imagens/ship.png')

        #coletando o retângulo da imagem e da tela
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #coincidindo a poição central da imagem com posição central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        def blitme(self):
            #desenha a nave na posição atual
            self.screen.blit(self.image, self.rect)


