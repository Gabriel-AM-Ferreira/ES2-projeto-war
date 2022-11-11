VERSION = "0.4"

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *
except ImportError as err:
    print(f"couldn't load module. {err}")
    sys.exit(2)

class fisica():

    def load_png(name):
        """ Load image and return image object"""
        fullname = os.path.join("data", name)
        try:
            image = pygame.image.load(fullname)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except FileNotFoundError:
            print(f"Cannot load image: {fullname}")
            raise SystemExit
        return image, image.get_rect()

    def listar_integrar_botões(a):
        botoes =[]
        for i in range(len(a)):
            botoes.append(botao(a[i]))

        return botoes

class Iniciar_jogo(pygame.sprite.Sprite,fisica):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = fisica.load_png('novojogo.png')
        self.screen = pygame.display.get_surface()
        self.rect.center = self.screen.get_rect().center
        self.valor=1
        self.screen.blit(self.image,(self.screen.get_rect().centerx - self.image.get_rect()[2]/2,self.screen.get_rect().centery - self.image.get_rect()[3]/2))
        

    def update(self, a):

        if((a==True) and (self.valor==1)):
            self.image, self.rect = fisica.load_png('Novojogoclickado.png')
            self.screen = pygame.display.get_surface()
            self.rect.center = self.screen.get_rect().center
            self.area = self.screen.get_rect()
            self.valor=2
            self.screen.blit(self.image,(self.screen.get_rect().centerx - self.image.get_rect()[2]/2,self.screen.get_rect().centery - self.image.get_rect()[3]/2))
          
        else:
            if(self.valor==2 and a ==False):
                self.image, self.rect = fisica.load_png('novojogo.png')
                self.screen = pygame.display.get_surface()
                self.rect.center = self.screen.get_rect().center
                self.area = self.screen.get_rect()
                self.valor=1
                self.screen.blit(self.image,(self.screen.get_rect().centerx - self.image.get_rect()[2]/2,self.screen.get_rect().centery - self.image.get_rect()[3]/2))
        
class instancia_mapa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = fisica.load_png('mapaWar.png')
        self.screen = pygame.display.get_surface()
        self.rect.center = self.screen.get_rect().center
        self.valor=1
        self.screen.blit(self.image,(0,0))
        

    def update(self, a):
        pass

class botao(pygame.sprite.Sprite):
    def __init__(self,a):
        pygame.sprite.Sprite.__init__(self)
        self.a=a
        self.image, self.rect = fisica.load_png('neutro.png')
        self.screen = pygame.display.get_surface()
        self.rect.centerx = a[0]
        self.rect.centery = a[1]
        self.rect.x += self.rect[3]/2
        self.rect.y += self.rect[3]
        self.valor=1
        self.screen.blit(self.image,(a))
        

    def update(self):
        if(self.valor==1):
            self.image, self.rect = fisica.load_png('selecionado.png')
            self.screen = pygame.display.get_surface()
            self.rect.centerx = self.a[0]
            self.rect.centery = self.a[1]
            self.rect.x += self.rect[3]/2
            self.rect.y += self.rect[3]
            self.valor=2
            self.screen.blit(self.image,(self.a))
        elif(self.valor==2):
            self.image, self.rect = fisica.load_png('inimigo.png')
            self.screen = pygame.display.get_surface()
            self.rect.centerx = self.a[0]
            self.rect.centery = self.a[1]
            self.rect.x += self.rect[3]/2
            self.rect.y += self.rect[3]
            self.valor=3
            self.screen.blit(self.image,(self.a))
        else:
            self.image, self.rect = fisica.load_png('neutro.png')
            self.screen = pygame.display.get_surface()
            self.rect.centerx = self.a[0]
            self.rect.centery = self.a[1]
            self.rect.x += self.rect[3]/2
            self.rect.y += self.rect[3]
            self.valor=3
            self.screen.blit(self.image,(self.a))

class menu():
    pygame.init()

    #criação da tela
    size = width, height = 1600 ,  900
    speed = [2, 2]
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)

    #pixelando o plano de fundo
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0 ))

    screen.blit(background, (0, 0))
    
    map= None
    novo_jogo= Iniciar_jogo()
    lista_pos=[(331, 545), (300, 445), (367, 511), (289, 472), (213, 386), (186, 351), (240, 331), (149, 281), (238, 282), (291, 307), (221, 246), (58, 220), (380, 219), (461, 236), (548, 256), (506, 278), (515, 314), (542, 306), (583, 319), (524, 358), (554, 373), (540, 408), (569, 407), (561, 460), (559, 513), (641, 520), (646, 399), (710, 363), (673, 335), (687, 278), (780, 254), (852, 249), (806, 282), (777, 312), (914, 255), (891, 361), (833, 382), (786, 398), (799, 458), (870, 514), (903, 514), (902, 468), (1011, 563), (640, 250)]
    botoes=None

    

    while True:
        for event in pygame.event.get():
                if(novo_jogo != None):
                    if(pygame.Rect.collidepoint(novo_jogo.rect, pygame.mouse.get_pos())):
                        novo_jogo.update(True)
                        if(pygame.mouse.get_pressed(num_buttons=3)[0]== True):
                            map = instancia_mapa()
                            botoes= fisica.listar_integrar_botões(lista_pos)
                            novo_jogo = None
                    else:
                        novo_jogo.update(False)
                else:
                    pass
                if event.type == QUIT:
                    pass
                
                if(botoes!=None):
                    for valores in botoes:
                        if(pygame.Rect.collidepoint(valores.rect,pygame.mouse.get_pos())):
                            print("passou por algo")
                            if(pygame.mouse.get_pressed(num_buttons=3)[0]==True):
                                valores.update()

                pygame.display.flip()

                #if(lista_pos2!=None):
                #    if(len(lista_pos2)==1):
                #        print(lista_pos2)
    



if __name__ == '__main__': menu()