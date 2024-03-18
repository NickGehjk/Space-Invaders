class Settings():

    def __init__(self):

        #configurações da tela
        self.screen_width = 1200 #largura
        self.screen_height = 600 #altura
        self.bg_color = (0,0,0) #cor de fundo

        #configurando projéteis
        self.bullet_spd = 2
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 255,255,255

        #configurando aliens
        self.alien_speed = 1
        self.alien_drop = 20
        self.alien_dir = 1

        self.bg_color_play = (248,248,248)
