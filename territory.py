from player import *
import pygame
import os
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

class botao(pygame.sprite.Sprite):
    def __init__(self,cordenadas):
        pygame.sprite.Sprite.__init__(self)
        self.a=cordenadas
        print(self.a[0])
        self.image, self.rect = fisica.load_png('neutro.png')
        self.screen = pygame.display.get_surface()
        self.rect.centerx = self.a[0]
        self.rect.centery = self.a[1]
        self.rect.x += self.rect[3]/2
        self.rect.y += self.rect[3]
        self.valor=1
        self.screen.blit(self.image,(self.a))
        

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

class Territory:
    def __init__(self, name, continent, neighbors_list, troops,cordenada):
        self.name = name
        self.continent = continent
        self.neighbors = neighbors_list
        self.troops = troops
        self.botao = botao(cordenada)
        self.owner = None

    def add_troops(self, number):
        self.troops += number

    def remove_troops(self, number):
        self.troops -= number

    def get_hostile_neighbors(self):
        hostile_neighbors = []
        for neighbor in self.neighbors:
            if neighbor.owner != self.owner:
                hostile_neighbors.append(neighbor)
        return hostile_neighbors

    def get_friendly_neighbors(self):
        friendly_neighbors = []
        for neighbor in self.neighbors:
            if neighbor.owner == self.owner:
                friendly_neighbors.append(neighbor)
        return friendly_neighbors

        
    