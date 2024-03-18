import pygame

class Ship():

    def __init__(self, screen):

        self.screen = screen

        self.init_image = pygame.image.load('sprites\shipnick.png')
        self.size = self.init_image.get_size()
        self.image = pygame.transform.scale(self.init_image, (int(self.size[0]/3), int(self.size[1]/3)))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):

        self.screen.blit(self.image, self.rect)
