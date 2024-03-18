import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, config, screen):
        #Inicializa o alien e o posiciona na tela
        super(Alien, self).__init__()
        self.screen = screen
        self.config = config

        #Carrega a imagem do alien
        self.init_image = pygame.image.load('sprites\\enemy.png')
        self.size = self.init_image.get_size()
        self.image = pygame.transform.scale(self.init_image, (int(self.size[0]/5), int(self.size[1]/5)))
        self.rect = self.image.get_rect()

        #Inicializa o alien proximo a parte superior
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Armazena a posição exata do alien
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def checaBordas(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):

        self.x += (self.config.alien_speed * self.config.alien_dir)
        self.rect.x = self.x





















