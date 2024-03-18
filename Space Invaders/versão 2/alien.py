import pygame
from pygame.sprite import Sprites

class Alien(Sprite):

    def __init__(self, config, screen):
        #Inicializa o alien e o posiciona na tela
        super(Alien, self).__init__()
        self.screen = screenself.config = config

        #Carrega a imagem do alien
        self.init_image = pygame.image.load('Imagens\\inimigo.png')
        self.rect = self.image.get_rect()

        self.size = self.init_image.get_size()
        self.image = pygame.transform.scale(self.init_image, (int(self.size[0]/3), int(self.size[1]/3)))

        #Inicializa o alien proximo a parte superior
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Armazena a posição exata do alien
        self.x = float(self.rect.x)

    def blitme(self):
        self.scren.blit(self.image, self.rect)















