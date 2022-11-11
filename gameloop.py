try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *
    from continent import *
    from player import *
    from card import *
    from territory import *
    from objective import *
    from constants import *
    from dice import *
    from random import shuffle
    from distributePhase import *
    from attackPhase import *
    from movementPhase import *
    from getObject import get_object_by_name
    from inputPlayer import ask_player_name, ask_color
    import re
    from pygame import *
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


class GameLoop:
    def __init__(self, num_players):
        self.colors = [VERMELHO, AZUL, VERDE, AMARELO, PRETO, BRANCO]
        self.players = []
        self.cards = []
        self.used_cards = []
        self.objective_cards = []
        self.continents = []
        self.territories = []
        self.num_players = num_players
        self.turn = -1
        self.current_player = None
        self.winner = None
        self.exchange_number = 0

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

        # adiciona jogadores a lista
        self.add_players(num_players)

        # mostra os jogadores e suas cores
        for player in self.players:
            print(f"Jogador {player.name} criado.")
            print(player.name, "escolheu a cor", player.color)            
        
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


        
        # cria grafo dos territórios
        self.territories.append(Territory(ALASCA, AMERICA_DO_NORTE, [MACKENZIE, VANCOUVER, VLADIVOSTOK], TROPAS_MINIMAS, (58, 220)))
        self.territories.append(Territory(MACKENZIE, AMERICA_DO_NORTE, [ALASCA, VANCOUVER, GROELANDIA, OTTAWA], TROPAS_MINIMAS,(221, 246)))
        self.territories.append(Territory(VANCOUVER, AMERICA_DO_NORTE, [ALASCA, MACKENZIE, OTTAWA, CALIFORNIA], TROPAS_MINIMAS,(149, 281)))
        self.territories.append(Territory(GROELANDIA, AMERICA_DO_NORTE, [MACKENZIE, LABRADOR, ISLANDIA], TROPAS_MINIMAS,(380, 219)))
        self.territories.append(Territory(OTTAWA, AMERICA_DO_NORTE, [MACKENZIE, VANCOUVER, CALIFORNIA, NOVA_YORQUE, LABRADOR], TROPAS_MINIMAS,(238, 282)))
        self.territories.append(Territory(LABRADOR, AMERICA_DO_NORTE, [OTTAWA, GROELANDIA, NOVA_YORQUE], TROPAS_MINIMAS,(291, 307)))
        self.territories.append(Territory(NOVA_YORQUE, AMERICA_DO_NORTE, [OTTAWA, LABRADOR, CALIFORNIA, MEXICO], TROPAS_MINIMAS,(240, 331)))
        self.territories.append(Territory(CALIFORNIA, AMERICA_DO_NORTE, [VANCOUVER, OTTAWA, NOVA_YORQUE, MEXICO], TROPAS_MINIMAS,(186, 351)))
        self.territories.append(Territory(MEXICO, AMERICA_DO_NORTE, [NOVA_YORQUE, CALIFORNIA, VENEZUELA], TROPAS_MINIMAS,(213, 386)))
        self.territories.append(Territory(VENEZUELA, AMERICA_DO_SUL, [MEXICO, PERU, BRASIL], TROPAS_MINIMAS,(300, 445)))
        self.territories.append(Territory(PERU, AMERICA_DO_SUL, [VENEZUELA, BRASIL, ARGENTINA], TROPAS_MINIMAS,(289, 472)))
        self.territories.append(Territory(BRASIL, AMERICA_DO_SUL, [VENEZUELA, PERU, ARGENTINA, ARGELIA], TROPAS_MINIMAS,(367, 511)))
        self.territories.append(Territory(ARGENTINA, AMERICA_DO_SUL, [PERU, BRASIL], TROPAS_MINIMAS,(331, 545)))
        self.territories.append(Territory(ARGELIA, AFRICA, [BRASIL,  FRANCA, EGITO, SUDAO, CONGO], TROPAS_MINIMAS,(540, 408)))
        self.territories.append(Territory(EGITO, AFRICA, [ARGELIA, SUDAO, ORIENTE_MEDIO, POLONIA,  FRANCA], TROPAS_MINIMAS,(554, 373)))
        self.territories.append(Territory(SUDAO, AFRICA, [ARGELIA, EGITO, ORIENTE_MEDIO, CONGO, MADAGASCAR], TROPAS_MINIMAS,(569, 407)))
        self.territories.append(Territory(CONGO, AFRICA, [ARGELIA, SUDAO, AFRICA_DO_SUL], TROPAS_MINIMAS,(561, 460)))
        self.territories.append(Territory(MADAGASCAR, AFRICA, [SUDAO, AFRICA_DO_SUL], TROPAS_MINIMAS,(641, 520)))
        self.territories.append(Territory(AFRICA_DO_SUL, AFRICA, [CONGO, MADAGASCAR, SUDAO], TROPAS_MINIMAS,(559, 513)))
        self.territories.append(Territory(FRANCA, EUROPA, [ARGELIA, EGITO, POLONIA, INGLATERRA, ALEMANHA], TROPAS_MINIMAS,(515, 314)))
        self.territories.append(Territory(POLONIA, EUROPA, [EGITO, FRANCA, ALEMANHA, MOSCOU, ORIENTE_MEDIO], TROPAS_MINIMAS,(0,0)))
        self.territories.append(Territory(INGLATERRA, EUROPA, [FRANCA, ALEMANHA, SUECIA, ISLANDIA], TROPAS_MINIMAS,(506, 278)))
        self.territories.append(Territory(ALEMANHA, EUROPA, [FRANCA, POLONIA, INGLATERRA], TROPAS_MINIMAS,(542, 306)))
        self.territories.append(Territory(SUECIA, EUROPA, [INGLATERRA, MOSCOU], TROPAS_MINIMAS,(0,0)))
        self.territories.append(Territory(MOSCOU, EUROPA, [POLONIA, SUECIA, ORIENTE_MEDIO], TROPAS_MINIMAS,(640, 250)))
        self.territories.append(Territory(ISLANDIA, EUROPA, [INGLATERRA, GROELANDIA], TROPAS_MINIMAS,(461, 236)))
        self.territories.append(Territory(ORIENTE_MEDIO, ASIA, [EGITO, POLONIA, MOSCOU, INDIA, ARAL, SUDAO], TROPAS_MINIMAS,(646, 399)))
        self.territories.append(Territory(INDIA, ASIA, [ORIENTE_MEDIO, ARAL, CHINA, VIETNA, SUMATRA], TROPAS_MINIMAS,(710, 363)))
        self.territories.append(Territory(ARAL, ASIA, [ORIENTE_MEDIO, INDIA, CHINA, OMSK, MOSCOU], TROPAS_MINIMAS,(673, 335)))
        self.territories.append(Territory(CHINA, ASIA, [ARAL, INDIA, VIETNA, OMSK, MONGOLIA, TCHITA, JAPAO, VLADIVOSTOK], TROPAS_MINIMAS,(833, 382)))
        self.territories.append(Territory(VIETNA, ASIA, [INDIA, CHINA, BORNEU], TROPAS_MINIMAS,(786, 398)))
        self.territories.append(Territory(JAPAO, ASIA, [CHINA, VLADIVOSTOK], TROPAS_MINIMAS,(891, 361)))
        self.territories.append(Territory(VLADIVOSTOK, ASIA, [CHINA, JAPAO, SIBERIA, TCHITA, ALASCA], TROPAS_MINIMAS,(914, 255)))
        self.territories.append(Territory(SIBERIA, ASIA, [VLADIVOSTOK, TCHITA, DUDINKA], TROPAS_MINIMAS,(852, 249)))
        self.territories.append(Territory(TCHITA, ASIA, [SIBERIA, VLADIVOSTOK, CHINA, MONGOLIA, DUDINKA], TROPAS_MINIMAS,(806, 282)))
        self.territories.append(Territory(MONGOLIA, ASIA, [TCHITA, CHINA, OMSK, DUDINKA], TROPAS_MINIMAS,(777, 312)))
        self.territories.append(Territory(OMSK, ASIA, [MONGOLIA, CHINA, ARAL, MOSCOU, DUDINKA], TROPAS_MINIMAS,(687, 278)))
        self.territories.append(Territory(DUDINKA, ASIA, [OMSK, MONGOLIA, TCHITA, SIBERIA], TROPAS_MINIMAS,(780, 254)))
        self.territories.append(Territory(SUMATRA, OCEANIA, [INDIA, AUSTRALIA], TROPAS_MINIMAS,(799, 458)))
        self.territories.append(Territory(BORNEU, OCEANIA, [VIETNA, AUSTRALIA, NOVA_GUINE], TROPAS_MINIMAS,(0,0)))
        self.territories.append(Territory(AUSTRALIA, OCEANIA, [SUMATRA, BORNEU, NOVA_GUINE], TROPAS_MINIMAS,(870, 514)))
        self.territories.append(Territory(NOVA_GUINE, OCEANIA, [AUSTRALIA, BORNEU], TROPAS_MINIMAS,(902, 468)))

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
        #self.cards.append(Card(POLONIA, QUADRADO))
        self.cards.append(Card(SIBERIA, TRIANGULO))
        self.cards.append(Card(SUDAO, QUADRADO))
        #self.cards.append(Card(SUECIA, CIRCULO))
        self.cards.append(Card(SUMATRA, QUADRADO))
        self.cards.append(Card(TCHITA, TRIANGULO))
        self.cards.append(Card(VANCOUVER, TRIANGULO))
        self.cards.append(Card(VENEZUELA, TRIANGULO))
        self.cards.append(Card(VIETNA, TRIANGULO))
        self.cards.append(Card(VLADIVOSTOK, CIRCULO))
        self.cards.append(Card(CORINGA, CORINGA))
        

        # aleatoriza os jogadores
        shuffle(self.players)

        # distribui os territorios aos jogadores aleatoriamente
        self.distribute_territories()
        self.continent_check()

        # mostra os territorios dos jogadores
        for player in self.players:
            print(f"Territorios do jogador {player.name}: {[territory.name for territory in player.territories]}")
            print(len(player.territories))

        # distribui as cartas de objetivo aos jogadores
        self.distribute_objectives()

        # embaralha as cartas de territorio
        shuffle(self.cards)

        # cria grafo dos territorios
        self.create_map()

        

    
    def create_map(self):
        for territory in self.territories:
            territory.continent = get_object_by_name(territory.continent, self.continents)
            neighbor_list = []
            for neighbor_name in territory.neighbors:
                neighbor_list.append(get_object_by_name(neighbor_name, self.territories))
            territory.neighbors = neighbor_list


    def start(self):
        map= None
        novo_jogo= Iniciar_jogo()
        botoes=None

        while self.winner is None:
            for event in pygame.event.get():
                if(novo_jogo != None):
                    if(pygame.Rect.collidepoint(novo_jogo.rect, pygame.mouse.get_pos())):
                        novo_jogo.update(True)
                        if(pygame.mouse.get_pressed(num_buttons=3)[0]== True):
                            map = instancia_mapa()
                            novo_jogo = None
                    else:
                        novo_jogo.update(False)
                else:
                    pass
                if event.type == QUIT:
                    return
                
                if(len(self.territories)!=0):
                    for valores in self.territories:
                        if(pygame.Rect.collidepoint(valores.botao.rect,pygame.mouse.get_pos())):
                            print(valores.name)
                            if(pygame.mouse.get_pressed(num_buttons=3)[0]==True):
                                valores.update()

                pygame.display.flip()

            if map != None :   
                self.turn += 1
                print(f"Turno atual: {self.turn}")
                for player in self.players:
                    print(f"Jogador atual: {player.name}")
                    self.current_player = player
                    # verifica se o objetivo ainda pode ser alcançado
                    self.check_if_objective_can_be_completed(self.current_player)
                    self.turns_phases()
                    if self.is_winner(self.current_player):
                        self.winner = self.current_player
                        break
        # mostra o vencedor
        print(f"O jogador {self.winner.name} venceu!")
                
    def turns_phases(self):
        # fase de distribuicao de tropas
        self.distribute_troops_phase()
        if self.turn > 0:
            # fase de ataque
            self.attack_phase()
            # fase de movimentacao
            self.move_troops_phase()
            # recebe carta de territorio
            self.give_territory_card()

    def distribute_troops_phase(self):
        distribute_troops(self.current_player)
        self.used_cards, self.exchange_number = cards_exchange(self.current_player, self.exchange_number, self.used_cards)

    def attack_phase(self):
        print(f"Fase de ataque do {self.current_player.name}")
        while True:
            print("1 - Atacar")
            print("2 - Passar")
            option = input("Opcao: ")
            if option == "1":
                attack(self.current_player)
            elif option == "2":
                break
            else:
                print("Opcao invalida!")


    def move_troops_phase(self):
        print(f"Fase de movimentacao do {self.current_player.name}")
        while True:
            print("1 - Mover")
            print("2 - Passar")
            option = input("Opcao: ")
            if option == "1":
                print("Movimentacao")
                move_troops(self.current_player)
            elif option == "2":
                break
            else:
                print("Opcao invalida!")

    def give_territory_card(self):
        if self.current_player.conquered_territory:
            self.current_player.conquered_territory = False
            self.current_player.cards.append(self.cards.pop())
            print(f"O jogador {self.current_player.name} recebeu uma carta de territorio!")
    

    def is_winner(self, player):
        print(player.objective.description)
        return player.objective.is_complete()

    def check_if_objective_can_be_completed(self, player):
        if re.search("Destruir", player.objective.description):
            if re.search(player.color, player.objective.description):
                player.objective = Objective(OBJETIVO_1)
                player.objective.owner = player

            change_objective = True
            for p in self.players:
                if re.search(p.color, player.objective.description):
                    change_objective = False
                    break
            if change_objective:
                player.objective = Objective(OBJETIVO_1)
                player.objective.owner = player

    def distribute_territories(self):
        shuffle(self.territories)
        for i in range(len(self.territories)):
            self.territories[i].owner = self.players[i % len(self.players)]
            self.territories[i].owner.territories.append(self.territories[i])

    def add_players(self, num_players):
        for i in range(num_players):
            player = Player(ask_player_name())
            self.players.append(player)
            color = ask_color(self.colors)
            player.color = color
            self.colors.remove(color)

    def distribute_objectives(self):
        shuffle(self.objective_cards)
        for player in self.players:
            player.objective = self.objective_cards.pop()
            player.objective.owner = player
            print(f"O jogador {player.name} recebeu o objetivo: {player.objective.description}")

    def continent_check(self):
        for player in self.players:
            for continent in self.continents:
                continent.conquer_continent(player)

if __name__ == '__main__':
    n = int(input("Digite o numero de jogadores: "))
    game = GameLoop(n)
    # teste para destruir jogador
    # while(len(game.players[1].territories) > 1):
    #     game.players[0].territories.append(game.players[1].territories.pop())
    # game.players[0].objective = Objective(OBJETIVO_9)
    # game.players[0].objective.owner = game.players[0]
    # game.players[1].color = AZUL
    game.start()


