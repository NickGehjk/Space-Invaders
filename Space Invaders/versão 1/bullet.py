import pygame
from pygame.sprite import sprite

class Bullet(Sprite):

    def __init__(self, config, screen, ship):

        super(Bullet,self).__init__()
        self.screen = screen
