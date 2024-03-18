import pygame

class imageScreen(self, screen, path):
    self.screen = screen
    self.image = pygame.image.load(path)

    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    #self.rect.centerx = self.screen_rect.centerx
    self.rect.center = self.screen_rect.centerx

    def blitme(self):
        self.screen.bit(self.image, self.rect)










