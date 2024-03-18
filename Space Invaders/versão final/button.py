import pygame.font

class Button():
    def __init__(self, config, screen, text):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #definir as dimensões e propriedades do botão
        self.width = 200
        self.height = 50
        self.button_color = (44, 84, 84)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom -50
        self.render_txt(text)

    def render_txt(self, text):
        self.render_text = self.font.render(text, True, self.text_color, self.button_color)
        self.render_text_rect = self.render_text.get_rect()
        self.render_text_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.render_text, self.render_text_rect)












