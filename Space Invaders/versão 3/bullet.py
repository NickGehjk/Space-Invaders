import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, config, screen, ship):

        super(Bullet,self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, config.bullet_width, config.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = config.bullet_color
        self.speed_factor = config.bullet_spd

    def update(self):

        self.y -= self.speed_factor
        self.rect.y = self.y

    def desenhaProj(self):
        pygame.draw.rect(self.screen, self.color, self.rect)























