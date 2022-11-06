from dice import *
from territory import *
from continent import *
from constants import *
from card import *
from inputPlayer import ask_quantity, ask_card, ask_territory, ask_quantity_combat, ask_yes_or_no
from validator import is_valid_exchange


class Player:
    def __init__(self, name):
        self.name = name
        self.color = ""
        self.objective = None
        self.cards = []
        self.territories = []
        self.continents = []
        self.defeated_players = []
        self.conquered_territory = False


    def add_normal_troops(self, troops_to_add):
        self.add_troops(troops_to_add, self.territories)

    def add_extra_troops(self):
        for continent in self.continents:
            print(f"Adicionando tropas extras do continente {continent.name}")
            self.add_troops(continent.bonus, continent.territories)

    def add_troops(self, troops_to_add, territory_list):
        while troops_to_add > 0:
            print(f"Você tem {troops_to_add} tropas para distribuir.")
            terr = ask_territory(territory_list, "Qual territorio deseja adicionar tropas?")
            quantity = ask_quantity(troops_to_add, "Quantas tropas deseja adicionar?")    
            terr.add_troops(quantity)
            troops_to_add -= quantity

    def exchange_cards(self, exchange_number):
        cards_to_exchange = []
        while True:
            for _ in range(3):
                card = ask_card(self.cards)
                cards_to_exchange.append(card)
                self.cards.remove(card)
            if is_valid_exchange(cards_to_exchange):
                break
            print("Troca invalida")
            for card in cards_to_exchange:
                self.cards.append(card)
            cards_to_exchange = []
        # verficar se o jogador possui os territorios das cartas
        self.cards_that_have_territories(cards_to_exchange)

        self.add_troops(self.get_troops_by_exchange(exchange_number), self.territories)
        return cards_to_exchange


    def cards_that_have_territories(self, cards_to_exchange):
        for card in cards_to_exchange:
            for territory in self.territories:
                if territory.name == card.name:
                    territory.add_troops(2)

    def get_troops_by_exchange(self, exchange_number):
        return max(4+(exchange_number*2), (exchange_number-1)*5)

    def get_attacking_territory(self):
        while True:
            terr = ask_territory(self.territories, "Com qual território deseja atacar?")
            if terr.troops > 1 and len(terr.get_hostile_neighbors()) > 0:
                return terr
            print("Esse territorio não pode atacar.")
            if not ask_yes_or_no("Deseja continuar atacando?"):
                return None
    
    def get_defending_territory(self, attacking_territory):
        hostile_neighbors = attacking_territory.get_hostile_neighbors()
        return ask_territory(hostile_neighbors, "Qual o territorio alvo?")

    def choose_attacking_troops(self, attacking_territory):
        print(f"O territorio {attacking_territory.name} possui {attacking_territory.troops} tropas.")
        return ask_quantity_combat(attacking_territory.troops-1, "Com quantas tropas deseja atacar?")

    def choose_defending_troops(self, defending_territory):
        print(f"O territorio {defending_territory.name} possui {defending_territory.troops} tropas.")
        return ask_quantity_combat(defending_territory.troops, "Com quantas tropas deseja defender?")

    def choose_moving_troops(self, from_territory):
        print(f"O territorio {from_territory.name} possui {from_territory.troops} tropas.")
        return ask_quantity(from_territory.troops-1, "Com quantas tropas deseja mover?")

    def add_territory(self, territory):
        self.territories.append(territory)
        territory.owner = self
        self.conquered_territory = True
    
    def remove_territory(self, territory):
        self.territories.remove(territory)
        territory.owner = None

    def add_continent(self, continent):
        self.continents.append(continent)

    def remove_continent(self, continent):
        self.continents.remove(continent)

    def ask_from_territory(self):
        while True:
            terr = ask_territory(self.territories, "De qual territorio deseja mover tropas?")
            if terr.troops > 1 and len(terr.get_friendly_neighbors()) > 0:
                return terr
            print("Esse territorio não pode mover tropas.")
            if not ask_yes_or_no("Deseja continuar movendo tropas?"):
                return None

    def ask_to_territory(self, from_territory):
        friendly_neighbors = from_territory.get_friendly_neighbors()
        return ask_territory(friendly_neighbors, "Para qual territorio deseja mover tropas?")
    
    
       



if __name__ == '__main__':
    player = Player("Matheus")
    terr = Territory("Brasil", "America do Sul", [], 0)
    terr_2 = Territory("Argentina", "America do Sul", [], 0)
    terr_3 = Territory("Venezuela", "America do Sul", [], 0)
    terr_4 = Territory("Peru", "America do Sul", [], 0)
    terr_5 = Territory("China", "Asia", [], 0)
    terr_6 = Territory("India", "Asia", [], 0)
    terr_7 = Territory("Mexico", "America do Norte", [], 0)

    continents = []
    continents.append(Continent("America do Sul", 2, [terr, terr_2, terr_3, terr_4]))
    continents.append(Continent("Asia", 7, [terr_5, terr_6]))
    continents.append(Continent("America do Norte", 5, [terr_7]))
    print(f"continents: {[c.name for c in continents]}")

    card_list = []
    card_list.append(Card(AFRICA_DO_SUL, TRIANGULO))
    card_list.append(Card(ALEMANHA, CIRCULO))
    
    card_list.append(Card(ARGELIA, CIRCULO))
    card_list.append(Card(ARGENTINA, QUADRADO))
    card_list.append(Card(AUSTRALIA, TRIANGULO))
    card_list.append(Card(BORNEU, QUADRADO))
    card_list.append(Card(CALIFORNIA, QUADRADO))
    card_list.append(Card(CHINA, CIRCULO))
    card_list.append(Card(CONGO, QUADRADO))
    card_list.append(Card(DUDINKA, CIRCULO))
    card_list.append(Card(FRANCA, QUADRADO))
    card_list.append(Card(GROELANDIA, CIRCULO))
    card_list.append(Card(INDIA, QUADRADO))
    card_list.append(Card(INGLATERRA, CIRCULO))
    card_list.append(Card(ISLANDIA, TRIANGULO))
    card_list.append(Card(JAPAO, QUADRADO))
    card_list.append(Card(LABRADOR, QUADRADO))
    card_list.append(Card(MACKENZIE, CIRCULO))
    card_list.append(Card(MADAGASCAR, CIRCULO))
    card_list.append(Card(MEXICO, QUADRADO))
    card_list.append(Card(MONGOLIA, CIRCULO))
    card_list.append(Card(MOSCOU, TRIANGULO))
    card_list.append(Card(NOVA_GUINE, CIRCULO))
    card_list.append(Card(NOVA_YORQUE, TRIANGULO))
    card_list.append(Card(OMSK, QUADRADO))
    card_list.append(Card(ORIENTE_MEDIO, QUADRADO))
    card_list.append(Card(OTTAWA, CIRCULO))
    card_list.append(Card(PERU, QUADRADO))
    card_list.append(Card(POLONIA, QUADRADO))
    card_list.append(Card(SIBERIA, TRIANGULO))
    card_list.append(Card(SUDAO, QUADRADO))
    card_list.append(Card(SUECIA, CIRCULO))
    card_list.append(Card(SUMATRA, QUADRADO))
    card_list.append(Card(TCHITA, TRIANGULO))
    card_list.append(Card(VANCOUVER, TRIANGULO))
    card_list.append(Card(VENEZUELA, TRIANGULO))
    card_list.append(Card(VIETNA, TRIANGULO))
    card_list.append(Card(VLADIVOSTOK, CIRCULO))
    

    player.territories.append(terr)
    terr.owner = player
    player.territories.append(terr_2)
    terr_2.owner = player
    player.territories.append(terr_3)
    terr_3.owner = player
    player.territories.append(terr_4)
    terr_4.owner = player
    player.territories.append(terr_5)
    terr_5.owner = player

    print(f"territories: {[t.name for t in player.territories]}")

    player.cards.append(Card(ARAL, TRIANGULO))
    player.cards.append(Card(ALASCA, TRIANGULO))
    player.cards.append(Card(EGITO, TRIANGULO))
    player.cards.append(Card(BRASIL, CIRCULO))
    player.cards.append(Card(SUDAO, QUADRADO))
    player.cards.append(Card(CORINGA, CORINGA))
    player.cards.append(Card(CORINGA, CORINGA))

    exchange_number = 0

    for continent in continents:
        print(f"Continente {continent.name}: {[terr.name for terr in continent.territories]}")
        if continent.is_complete(player):
            print(f"Continente {continent.name} completo")
            player.continents.append(continent)
    print(player.name)
    print(f"Continents: {[c.name for c in player.continents]}")

    while True:
        print("1 - Adicionar tropas")
        print("2 - Atacar")
        print("3 - Trocar cartas")
        print("4 - Remover tropas")
        print("5 - Sair")
        option = int(input("Escolha uma opcao: "))
        if option == 1:
            player.add_normal_troops(10)
            player.add_extra_troops()
            for territory in player.territories:
                print(territory.name, territory.troops)
            
        elif option == 2:
            pass
        elif option == 3:
            player.exchange_cards(exchange_number)
            exchange_number += 1
            for territory in player.territories:
                print(territory.name, territory.troops)
        elif option == 4:
            pass
        elif option == 5:
            break
        else:
            print("Opcao invalida")