class Settings():

    def __init__(self):

        #configurações da tela
        self.screen_width = 1200 #largura
        self.screen_height = 600 #altura
        self.bg_color = (235, 242, 19) #cor de fundo #8, 32, 94

        #configurando projéteis
        self.bullet_spd = 2
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0

        #configurando aliens
        self.alien_spd = 1
        #self.fleet_drop_speed = 1
        #self.fleet_direction = 1
