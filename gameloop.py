from continent import *
from player import *
from card import *
from random import shuffle

class GameLoop:
    def __init__(self, num_players):
        self.colors = ["Azul", "Amarelo", "Vermelho", "Preto", "Branco", "Verde"]
        self.players = []
        self.cards = []
        self.objective_cards = []
        self.continents = []
        self.territories = []
        self.num_players = num_players
        self.turn = 0
        self.phase = 0
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
        self.objective_cards.append("Conquistar na totalidade a Europa, a Oceania e mais um terceiro.")
        self.objective_cards.append("Conquistar na totalidade a Ásia e a América do Sul.")
        self.objective_cards.append("Conquistar na totalidade a Europa, a América do Sul e mais um terceiro continente.")
        self.objective_cards.append("Conquistar 18 territórios e ocupar cada um deles com pelo menos dois exércitos.")
        self.objective_cards.append("Conquistar na totalidade a Ásia e a África.")
        self.objective_cards.append("Conquistar na totalidade a América do Norte e a África.")
        self.objective_cards.append("Conquistar na totalidade a América do Norte e a Oceania.")
        self.objective_cards.append("Conquistar 24 territórios à sua escolha.")
        self.objective_cards.append("Destruir totalmente OS exércitos azuis.")
        self.objective_cards.append("Destruir totalmente OS exércitos amarelos.")
        self.objective_cards.append("Destruir totalmente OS exércitos vermelhos.")
        self.objective_cards.append("Destruir totalmente OS exércitos pretos.")
        self.objective_cards.append("Destruir totalmente OS exércitos brancos.")
        self.objective_cards.append("Destruir totalmente OS exércitos verdes.")

        # embaralha as cartas de objetivo
        shuffle(self.objective_cards)
        
        # distribui as cartas de objetivo
        for player in self.players:
            player.objective_card = self.objective_cards.pop()

        # adiciona territórios a lista FALTA TERMINAR
        self.territories.append(Territory("Alasca", "América do Norte", ["Mackenzie", "Vancouver", "Vladivostok"], 0))
        self.territories.append(Territory("Mackenzie", "América do Norte", ["Alasca", "Vancouver", "Groelândia", "Ottawa"], 0))
        self.territories.append(Territory("Vancouver", "América do Norte", ["Alasca", "Mackenzie", "Ottawa", "Califórnia"], 0))
        self.territories.append(Territory("Groelândia", "América do Norte", ["Mackenzie", "Labrador", "Islândia"], 0))
        self.territories.append(Territory("Ottawa", "América do Norte", ["Mackenzie", "Vancouver", "Califórnia", "Nova Yorque", "Labrador"], 0))
        self.territories.append(Territory("Labrador", "América do Norte", ["Ottawa", "Groelândia", "Nova Yorque"], 0))
        self.territories.append(Territory("Nova Yorque", "América do Norte", ["Ottawa", "Labrador", "Califórnia", "Mexico"], 0))
        self.territories.append(Territory("Califórnia", "América do Norte", ["Vancouver", "Ottawa", "Nova Yorque", "Mexico"], 0))
        self.territories.append(Territory("Mexico", "América do Norte", ["Nova Yorque", "Califórnia", "Venezuela"], 0))
        self.territories.append(Territory("Venezuela", "América do Sul", ["Mexico", "Peru", "Brasil"], 0))
        self.territories.append(Territory("Peru", "América do Sul", ["Venezuela", "Brasil", "Argentina"], 0))
        self.territories.append(Territory("Brasil", "América do Sul", ["Venezuela", "Peru", "Argentina", "Argélia"], 0))
        self.territories.append(Territory("Argentina", "América do Sul", ["Peru", "Brasil"], 0))
        self.territories.append(Territory("Argélia", "África", ["Brasil", "França", "Egito", "Sudão", "Congo"], 0))
        self.territories.append(Territory("Egito", "África", ["Argélia", "Sudão", "Oriente Médio", "Polônia", "França"], 0))
        self.territories.append(Territory("Sudão", "África", ["Argélia", "Egito", "Oriente Médio", "Congo", "Madagascar"], 0))
        self.territories.append(Territory("Congo", "África", ["Argélia", "Sudão", "África do Sul"], 0))
        self.territories.append(Territory("Madagascar", "África", ["Sudão", "África do Sul"], 0))
        self.territories.append(Territory("África do Sul", "África", ["Congo", "Madagascar", "Sudão"], 0))
        self.territories.append(Territory("França", "Europa", ["Argélia", "Egito", "Polônia", "Inglaterra", "Alemanha"], 0))
        self.territories.append(Territory("Polônia", "Europa", ["Egito", "França", "Alemanha", "Moscou", "Oriente Médio"], 0))
        self.territories.append(Territory("Inglaterra", "Europa", ["França", "Alemanha", "Suécia", "Islândia"], 0))
        self.territories.append(Territory("Alemanha", "Europa", ["França", "Polônia", "Inglaterra"], 0))
        self.territories.append(Territory("Suécia", "Europa", ["Inglaterra", "Moscou"], 0))
        self.territories.append(Territory("Moscou", "Europa", ["Polônia", "Suécia", "Oriente Médio"], 0))
        self.territories.append(Territory("Islândia", "Europa", ["Inglaterra", "Groelândia"], 0))

        # embaralha os territórios
        shuffle(self.territories)

        # embaralha os jogadores
        shuffle(self.players)

        # distribui os territórios
        for territory in self.territories:
            territory.owner = self.players[self.territories.index(territory) % len(self.players)].name


        # adiciona continentes a lista
        self.continents.append(Continent("África", 3, self.territories))
        self.continents.append(Continent("América do Norte", 5, self.territories))
        self.continents.append(Continent("América do Sul", 2, self.territories))
        self.continents.append(Continent("Ásia", 7, self.territories))
        self.continents.append(Continent("Europa", 5, self.territories))
        self.continents.append(Continent("Oceania", 2, self.territories))

        # adiciona cartas a lista
        self.cards.append(Card("África do Sul", "Triângulo"))
        self.cards.append(Card("Alasca", "Triângulo"))
        self.cards.append(Card("Alemanha", "Círculo"))
        self.cards.append(Card("Aral", "Triângulo"))
        self.cards.append(Card("Argélia", "Círculo"))
        self.cards.append(Card("Argentina", "Quadrado"))
        self.cards.append(Card("Austrália", "Triângulo"))
        self.cards.append(Card("Bolívia", "Triângulo"))
        self.cards.append(Card("Bornéu", "Quadrado"))
        self.cards.append(Card("Brasil", "Círculo"))
        self.cards.append(Card("Califórnia", "Quadrado"))
        self.cards.append(Card("China", "Círculo"))
        self.cards.append(Card("Congo", "Quadrado"))
        self.cards.append(Card("Dudinka", "Círculo"))
        self.cards.append(Card("Egito", "Triângulo"))
        self.cards.append(Card("França", "Quadrado"))
        self.cards.append(Card("Groelândia", "Círculo"))
        self.cards.append(Card("Índia", "Quadrado"))
        self.cards.append(Card("Inglaterra", "Círculo"))
        self.cards.append(Card("Islândia", "Triângulo"))
        self.cards.append(Card("Japão", "Quadrado"))
        self.cards.append(Card("Labrador", "Quadrado"))
        self.cards.append(Card("Mackenzie", "Círculo"))
        self.cards.append(Card("Madagascar", "Círculo"))
        self.cards.append(Card("México", "Quadrado"))
        self.cards.append(Card("Mongolia", "Círculo"))
        self.cards.append(Card("Moscou", "Triângulo"))
        self.cards.append(Card("Nova Guiné", "Círculo"))
        self.cards.append(Card("Nova Yorque", "Triângulo"))
        self.cards.append(Card("Omsk", "Quadrado"))
        self.cards.append(Card("Oriente Médio", "Quadrado"))
        self.cards.append(Card("Ottawa", "Círculo"))
        self.cards.append(Card("Polônia", "Quadrado"))
        self.cards.append(Card("Sibéria", "Triângulo"))
        self.cards.append(Card("Sudão", "Quadrado"))
        self.cards.append(Card("Suécia", "Círculo"))
        self.cards.append(Card("Sumatra", "Quadrado"))
        self.cards.append(Card("Tchita", "Triângulo"))
        self.cards.append(Card("Vancouver", "Triângulo"))
        self.cards.append(Card("Venezuela", "Triângulo"))
        self.cards.append(Card("Vietnã", "Triângulo"))
        self.cards.append(Card("Vladivostok", "Círculo"))
        self.cards.append(Card("Coringa", "Coringa"))

        # embaralha as cartas
        shuffle(self.cards)
