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
        self.cards.append(Card(BORNEU, QUADRADO))
        self.cards.append(Card(BRASIL, CIRCULO))
        self.cards.append(Card(CALIFORNIA, QUADRADO))
        self.cards.append(Card(CHINA, CIRCULO))
        self.cards.append(Card(CONGO, QUADRADO))
        self.cards.append(Card(DUDINKA, CIRCULO))
        self.cards.append(Card(EGITO, TRIANGULO))
        self.cards.append(Card(FRANCA, QUADRADO))
        self.cards.append(Card(GROELANDIA, CIRCULO))
        self.cards.append(Card(INDIA, QUADRADO))
        self.cards.append(Card(INGLATERRA, CIRCULO))
        self.cards.append(Card(ISLANDIA, TRIANGULO))
        self.cards.append(Card(JAPAO, QUADRADO))
        self.cards.append(Card(LABRADOR, QUADRADO))
        self.cards.append(Card(MACKENZIE, CIRCULO))
        self.cards.append(Card(MADAGASCAR, CIRCULO))
        self.cards.append(Card(MEXICO, QUADRADO))
        self.cards.append(Card(MONGOLIA, CIRCULO))
        self.cards.append(Card(MOSCOU, TRIANGULO))
        self.cards.append(Card(NOVA_GUINE, CIRCULO))
        self.cards.append(Card(NOVA_YORQUE, TRIANGULO))
        self.cards.append(Card(OMSK, QUADRADO))
        self.cards.append(Card(ORIENTE_MEDIO, QUADRADO))
        self.cards.append(Card(OTTAWA, CIRCULO))
        self.cards.append(Card(PERU, QUADRADO))
        self.cards.append(Card(POLONIA, QUADRADO))
        self.cards.append(Card(SIBERIA, TRIANGULO))
        self.cards.append(Card(SUDAO, QUADRADO))
        self.cards.append(Card(SUECIA, CIRCULO))
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
        while self.winner is None:
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


