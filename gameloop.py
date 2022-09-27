from continent import *
from player import *
from card import *
from random import shuffle
from territory import *
from constants import *
class GameLoop:
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
        self.objective_cards.append(OBJETIVO_1)
        self.objective_cards.append(OBJETIVO_2)
        self.objective_cards.append(OBJETIVO_3)
        self.objective_cards.append(OBJETIVO_4)
        self.objective_cards.append(OBJETIVO_5)
        self.objective_cards.append(OBJETIVO_6)
        self.objective_cards.append(OBJETIVO_7)
        self.objective_cards.append(OBJETIVO_8)
        self.objective_cards.append(OBJETIVO_9)
        self.objective_cards.append(OBJETIVO_10)
        self.objective_cards.append(OBJETIVO_11)
        self.objective_cards.append(OBJETIVO_12)
        self.objective_cards.append(OBJETIVO_13)
        self.objective_cards.append(OBJETIVO_14)

        # embaralha as cartas de objetivo
        shuffle(self.objective_cards)
        
        # distribui as cartas de objetivo
        for player in self.players:
            player.objective_card = self.objective_cards.pop()

        # adiciona territórios a lista
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


        # embaralha os territórios
        shuffle(self.territories)

        # embaralha os jogadores
        shuffle(self.players)

        # distribui os territórios
        for territory in self.territories:
            territory.owner = self.players[self.territories.index(territory) % len(self.players)].name

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

        # embaralha as cartas
        shuffle(self.cards)
