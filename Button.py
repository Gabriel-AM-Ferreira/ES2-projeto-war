# faz butão
from menu import *
import gameloop
from gameloop import *


class Button:
    def __init__(self, screen, position, text):
        pygame.font.init()

        self.screen=screen
        self.position = position
        self.text = text
        self.fontsize = 50
        self.fontcor = (255, 0, 0)
        self.cor = (50,50,50)




        font = pygame.font.SysFont("Comic Sans MS", self.fontsize)
        self.tamanho = font.render(self.text, 1, self.fontcor)
        self.x, self.y, self.w, self.h = self.tamanho.get_rect()
        self.x, self.y = self.position

        pygame.draw.rect(self.screen, (self.cor), (self.x, self.y, self.w, self.h))

        self.height = self.h
        self.width= self.w
        self.rect =self.screen.blit(self.tamanho, (self.x, self.y))
        self.clica = False
    def clicado (Button, event):
        if (event.type == pygame.MOUSEBUTTONDOWN):
            return Button.rect.collidepoint(pygame.mouse.get_pos())
        else:
            return False
    def colore (Button, cor):
        Button.cor = cor
        pygame.draw.rect(Button.screen, cor, (Button.x, Button.y, Button.w, Button.h))
        pygame.display.flip()








