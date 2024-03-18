import sys
import pygame
from configuracoes import *
from nave import *
import funcoesDoJogo as func
from pygame.sprite import Group
from alien import *
from button import *
from imagemFundo import *

def run_game():

    pygame.init()
    config = Settings()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))

    pygame.display.set_caption('Space Invaders')

    play = Button(config, screen, 'Play')
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()

    func.createFleet(config,screen,aliens)
    func.playSound('sounds\\menu.mp3')

    gameOn = False

    while True:
        func.eventCheck(config,screen,ship,aliens,bullets)
        #func.playSound('sounds\\battle.mp3')
        if gameOn and len(aliens) > 0:

            #func.playSound('sounds\\battle.mp3')
            func.tick(config,screen,ship,aliens,bullets)
            alienCount = len(aliens)
            collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
            if alienCount > len(aliens):
                func.soundEffect('sounds\\laser7.wav')
            bullets.update()
            func.atualizaAliens(config,aliens)
            gameOn = func.checkGame(screen,aliens)
            #if gameOn == True:
                #func.playSound('sounds\\battle.mp3')
            #elif gameOn == False:
                #func.playSound('sounds\\menu.mp3')

        elif gameOn and len(aliens) == 0:
            func.createFleet(config,screen,aliens)
            func.alienSpeedUp(config)

        else:
            pygame.time.wait(500)
            #func.playSound('sounds\\menu.mp3')
            screenImage = imageScreen(screen,'sprites\\background2.png')
            func.initScreen(config, screen, play, screenImage)
            gameOn = func.checkPlayButton(play,config)

run_game()

























