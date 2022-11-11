from continent import *
from player import *
from card import *
from territory import *
from objective import *
from constants import *
from dice import *
from pygame import *
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

class GameLoop(pygame.sprite.Sprite):
    def __init__(self, num_players):
        self.colors = [VERMELHO, AZUL, VERDE, AMARELO, PRETO, BRANCO]
        self.players = []
        self.cards = []
        self.objective_cards = []
        self.continents = []
        self.territories = []
        self.num_players = num_players
        self.turn = 0
        self.current_player = 0
        self.winner = None

        # adiciona jogadores a lista
        for i in range(num_players):
            self.players.append(Player("Jogador " + str(i + 1)))
        
        # escolha de cores dos jogadores
        for player in self.players:
            print("Escolha uma cor para o jogador", player.name)
            for color in self.colors:
                print(color)
            player.color = input()
            self.colors.remove(player.color)
        
        # adiciona cartas de objetivo a lista
        self.objective_cards.append(Objective(OBJETIVO_1))
        self.objective_cards.append(Objective(OBJETIVO_2))
        self.objective_cards.append(Objective(OBJETIVO_3))
        self.objective_cards.append(Objective(OBJETIVO_4))
        self.objective_cards.append(Objective(OBJETIVO_5))
        self.objective_cards.append(Objective(OBJETIVO_6))
        self.objective_cards.append(Objective(OBJETIVO_7))
        self.objective_cards.append(Objective(OBJETIVO_8))
        self.objective_cards.append(Objective(OBJETIVO_9))
        self.objective_cards.append(Objective(OBJETIVO_10))
        self.objective_cards.append(Objective(OBJETIVO_11))
        self.objective_cards.append(Objective(OBJETIVO_12))
        self.objective_cards.append(Objective(OBJETIVO_13))
        self.objective_cards.append(Objective(OBJETIVO_14))

        
        # distribui as cartas de objetivo aos jogadores
        for player in self.players:
            territory_die = Dice(len(self.objective_cards))
            player.objective = self.objective_cards[territory_die.roll() - 1]
            self.objective_cards.remove(player.objective)



        # cria grafo dos territórios
        self.territories.append(Territory(ALASCA, AMERICA_DO_NORTE, [MACKENZIE, VANCOUVER, VLADIVOSTOK], TROPAS_MINIMAS))
        self.territories.append(Territory(MACKENZIE, AMERICA_DO_NORTE, [ALASCA, VANCOUVER, GROELANDIA, OTTAWA], TROPAS_MINIMAS))
        self.territories.append(Territory(VANCOUVER, AMERICA_DO_NORTE, [ALASCA, MACKENZIE, OTTAWA, CALIFORNIA], TROPAS_MINIMAS))
        self.territories.append(Territory(GROELANDIA, AMERICA_DO_NORTE, [MACKENZIE, LABRADOR, ISLANDIA], TROPAS_MINIMAS))
        self.territories.append(Territory(OTTAWA, AMERICA_DO_NORTE, [MACKENZIE, VANCOUVER, CALIFORNIA, NOVA_YORQUE, LABRADOR], TROPAS_MINIMAS))
        self.territories.append(Territory(LABRADOR, AMERICA_DO_NORTE, [OTTAWA, GROELANDIA, NOVA_YORQUE], TROPAS_MINIMAS))
        self.territories.append(Territory(NOVA_YORQUE, AMERICA_DO_NORTE, [OTTAWA, LABRADOR, CALIFORNIA, MEXICO], TROPAS_MINIMAS))
        self.territories.append(Territory(CALIFORNIA, AMERICA_DO_NORTE, [VANCOUVER, OTTAWA, NOVA_YORQUE, MEXICO], TROPAS_MINIMAS))
        self.territories.append(Territory(MEXICO, AMERICA_DO_NORTE, [NOVA_YORQUE, CALIFORNIA, VENEZUELA], TROPAS_MINIMAS))
        self.territories.append(Territory(VENEZUELA, AMERICA_DO_SUL, [MEXICO, PERU, BRASIL], TROPAS_MINIMAS))
        self.territories.append(Territory(PERU, AMERICA_DO_SUL, [VENEZUELA, BRASIL, ARGENTINA], TROPAS_MINIMAS))
        self.territories.append(Territory(BRASIL, AMERICA_DO_SUL, [VENEZUELA, PERU, ARGENTINA, ARGELIA], TROPAS_MINIMAS))
        self.territories.append(Territory(ARGENTINA, AMERICA_DO_SUL, [PERU, BRASIL], TROPAS_MINIMAS))
        self.territories.append(Territory(ARGELIA, AFRICA, [BRASIL,  FRANCA, EGITO, SUDAO, CONGO], TROPAS_MINIMAS))
        self.territories.append(Territory(EGITO, AFRICA, [ARGELIA, SUDAO, ORIENTE_MEDIO, POLONIA,  FRANCA], TROPAS_MINIMAS))
        self.territories.append(Territory(SUDAO, AFRICA, [ARGELIA, EGITO, ORIENTE_MEDIO, CONGO, MADAGASCAR], TROPAS_MINIMAS))
        self.territories.append(Territory(CONGO, AFRICA, [ARGELIA, SUDAO, AFRICA_DO_SUL], TROPAS_MINIMAS))
        self.territories.append(Territory(MADAGASCAR, AFRICA, [SUDAO, AFRICA_DO_SUL], TROPAS_MINIMAS))
        self.territories.append(Territory(AFRICA_DO_SUL, AFRICA, [CONGO, MADAGASCAR, SUDAO], TROPAS_MINIMAS))
        self.territories.append(Territory(FRANCA, EUROPA, [ARGELIA, EGITO, POLONIA, INGLATERRA, ALEMANHA], TROPAS_MINIMAS))
        self.territories.append(Territory(POLONIA, EUROPA, [EGITO, FRANCA, ALEMANHA, MOSCOU, ORIENTE_MEDIO], TROPAS_MINIMAS))
        self.territories.append(Territory(INGLATERRA, EUROPA, [FRANCA, ALEMANHA, SUECIA, ISLANDIA], TROPAS_MINIMAS))
        self.territories.append(Territory(ALEMANHA, EUROPA, [FRANCA, POLONIA, INGLATERRA], TROPAS_MINIMAS))
        self.territories.append(Territory(SUECIA, EUROPA, [INGLATERRA, MOSCOU], TROPAS_MINIMAS))
        self.territories.append(Territory(MOSCOU, EUROPA, [POLONIA, SUECIA, ORIENTE_MEDIO], TROPAS_MINIMAS))
        self.territories.append(Territory(ISLANDIA, EUROPA, [INGLATERRA, GROELANDIA], TROPAS_MINIMAS))
        self.territories.append(Territory(ORIENTE_MEDIO, ASIA, [EGITO, POLONIA, MOSCOU, INDIA, ARAL, SUDAO], TROPAS_MINIMAS))
        self.territories.append(Territory(INDIA, ASIA, [ORIENTE_MEDIO, ARAL, CHINA, VIETNA, SUMATRA], TROPAS_MINIMAS))
        self.territories.append(Territory(ARAL, ASIA, [ORIENTE_MEDIO, INDIA, CHINA, OMSK, MOSCOU], TROPAS_MINIMAS))
        self.territories.append(Territory(CHINA, ASIA, [ARAL, INDIA, VIETNA, OMSK, MONGOLIA, TCHITA, JAPAO, VLADIVOSTOK], TROPAS_MINIMAS))
        self.territories.append(Territory(VIETNA, ASIA, [INDIA, CHINA, BORNEU], TROPAS_MINIMAS))
        self.territories.append(Territory(JAPAO, ASIA, [CHINA, VLADIVOSTOK], TROPAS_MINIMAS))
        self.territories.append(Territory(VLADIVOSTOK, ASIA, [CHINA, JAPAO, SIBERIA, TCHITA, ALASCA], TROPAS_MINIMAS))
        self.territories.append(Territory(SIBERIA, ASIA, [VLADIVOSTOK, TCHITA, DUDINKA], TROPAS_MINIMAS))
        self.territories.append(Territory(TCHITA, ASIA, [SIBERIA, VLADIVOSTOK, CHINA, MONGOLIA, DUDINKA], TROPAS_MINIMAS))
        self.territories.append(Territory(MONGOLIA, ASIA, [TCHITA, CHINA, OMSK, DUDINKA], TROPAS_MINIMAS))
        self.territories.append(Territory(OMSK, ASIA, [MONGOLIA, CHINA, ARAL, MOSCOU, DUDINKA], TROPAS_MINIMAS))
        self.territories.append(Territory(DUDINKA, ASIA, [OMSK, MONGOLIA, TCHITA, SIBERIA], TROPAS_MINIMAS))
        self.territories.append(Territory(SUMATRA, OCEANIA, [INDIA, AUSTRALIA], TROPAS_MINIMAS))
        self.territories.append(Territory(BORNEU, OCEANIA, [VIETNA, AUSTRALIA, NOVA_GUINE], TROPAS_MINIMAS))
        self.territories.append(Territory(AUSTRALIA, OCEANIA, [SUMATRA, BORNEU, NOVA_GUINE], TROPAS_MINIMAS))
        self.territories.append(Territory(NOVA_GUINE, OCEANIA, [AUSTRALIA, BORNEU], TROPAS_MINIMAS))


        # distribui os territorios aos jogadores
        player_dice = Dice(len(self.players))
        for territory in self.territories:
            territory.owner = self.players[player_dice.roll() - 1]


        # adiciona continentes a lista
        self.continents.append(Continent(AFRICA, BONUS_ASIA, self.territories))
        self.continents.append(Continent(AMERICA_DO_NORTE, BONUS_AMERICA_DO_NORTE, self.territories))
        self.continents.append(Continent(AMERICA_DO_SUL, BONUS_AMERICA_DO_SUL, self.territories))
        self.continents.append(Continent(ASIA, BONUS_ASIA, self.territories))
        self.continents.append(Continent(EUROPA, BONUS_EUROPA, self.territories))
        self.continents.append(Continent(OCEANIA, BONUS_OCEANIA, self.territories))

        # adiciona cartas a lista
        self.cards.append(Card(AFRICA_DO_SUL, TRIANGULO))
        self.cards.append(Card(ALASCA, TRIANGULO))
        self.cards.append(Card(ALEMANHA, CIRCULO))
        self.cards.append(Card(ARAL, TRIANGULO))
        self.cards.append(Card(ARGELIA, CIRCULO))
        self.cards.append(Card(ARGENTINA, QUADRADO))
        self.cards.append(Card(AUSTRALIA, TRIANGULO))
        #self.cards.append(Card(BORNEU, QUADRADO))
        self.cards.append(Card(BRASIL, CIRCULO))
        self.cards.append(Card(CALIFORNIA, QUADRADO))
        self.cards.append(Card(CHINA, CIRCULO))
        self.cards.append(Card(CONGO, QUADRADO))
        self.cards.append(Card(DUDINKA, CIRCULO))
        self.cards.append(Card(EGITO, TRIANGULO))
        #escandinavia
        self.cards.append(Card(FRANCA, QUADRADO))
        self.cards.append(Card(GROELANDIA, CIRCULO))
        self.cards.append(Card(INDIA, QUADRADO))
        self.cards.append(Card(INGLATERRA, CIRCULO))
        #italia
        self.cards.append(Card(ISLANDIA, TRIANGULO))
        self.cards.append(Card(JAPAO, QUADRADO))
        self.cards.append(Card(LABRADOR, QUADRADO))
        self.cards.append(Card(MACKENZIE, CIRCULO))
        self.cards.append(Card(MADAGASCAR, CIRCULO))
        #marrocos
        self.cards.append(Card(MEXICO, QUADRADO))
        self.cards.append(Card(MONGOLIA, CIRCULO))
        self.cards.append(Card(MOSCOU, TRIANGULO))
        self.cards.append(Card(NOVA_GUINE, CIRCULO))
        self.cards.append(Card(NOVA_YORQUE, TRIANGULO))
        #nova zelandia
        self.cards.append(Card(OMSK, QUADRADO))
        self.cards.append(Card(ORIENTE_MEDIO, QUADRADO))
        self.cards.append(Card(OTTAWA, CIRCULO))
        self.cards.append(Card(PERU, QUADRADO))
       # self.cards.append(Card(POLONIA, QUADRADO))
        self.cards.append(Card(SIBERIA, TRIANGULO))
        self.cards.append(Card(SUDAO, QUADRADO))
       # self.cards.append(Card(SUECIA, CIRCULO))
        self.cards.append(Card(SUMATRA, QUADRADO))
        self.cards.append(Card(TCHITA, TRIANGULO))
        self.cards.append(Card(VANCOUVER, TRIANGULO))
        self.cards.append(Card(VENEZUELA, TRIANGULO))
        self.cards.append(Card(VIETNA, TRIANGULO))
        self.cards.append(Card(VLADIVOSTOK, CIRCULO))
        self.cards.append(Card(CORINGA, CORINGA))


    def start(self):
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

        while self.winner is not None:
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
                    return
                
                if(botoes!=None):
                    for valores in botoes:
                        if(pygame.Rect.collidepoint(valores.rect,pygame.mouse.get_pos())):
                            print("passou por algo")
                            if(pygame.mouse.get_pressed(num_buttons=3)[0]==True):
                                valores.update()

                pygame.display.flip()

            for player in self.players:
                self.current_player = player
                self.turns_phases()
                self.is_winner(self.current_player)
        # mostra o vencedor
        print(f"O jogador {self.winner.name} venceu!")
                
    def turns_phases(self):
        # fase de distribuicao de tropas
        self.distribute_troops()
        # fase de ataque
        self.attack_phase()
        # fase de movimentacao
        self.move_troops_phase()
        # recebe carta de territorio
        self.give_territory_card()

    