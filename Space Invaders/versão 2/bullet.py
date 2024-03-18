import pygame
from pygame.sprite import Sprite
from configuracoes import *

class Bullet(Sprite):

    def __init__(self, config, screen, ship):

        super(Bullet,self).__init__()
        self.screen = screen

        #Cria um retangulo para o projetil em (0,0) e depois define a posição correta
        self.rect = pygame.Rect(0, 0, config.bullet_width, config.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Armazena a posição do projetil como um valor decimal
        self.y = float(self.rect.y)

    def update(self):
        #Move o projetil para cima
        self.y -= self.speed_factor
        self.rect.y = self.y

    def desenhaProj(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
















