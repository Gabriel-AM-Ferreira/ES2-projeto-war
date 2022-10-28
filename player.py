from dice import *
from territory import *
from continent import *
from constants import *
from card import *

# tabela de trocas war
# 3 cartas iguais = 4 tropas
# 3 cartas diferentes = 6 tropas
# 4 cartas iguais = 8 tropas
# 4 cartas diferentes = 10 tropas
# 5 cartas iguais = 15 tropas
# 5 cartas diferentes = 20 tropas
# 6 cartas iguais = 25 tropas
# 6 cartas diferentes = 30 tropas


class Player:
    def __init__(self, name):
        self.name = name
        self.color = ""
        self.objective = None
        self.cards = []
        self.territories = []
        self.continents = []
        self.conquered_territoty = False


    def add_normal_troops(self, troops_to_add):
        self.add_troops(troops_to_add, self.territories)

    def add_extra_troops(self):
        for continent in self.continents:
            print(f"Adicionando tropas extras do continente {continent.name}")
            self.add_troops(continent.bonus, continent.territories)

    def add_troops(self, troops_to_add, territory_list):
        while troops_to_add > 0:
            print(f"Você tem {troops_to_add} tropas para distribuir.")
            while True:
                territory_name = input(f"Em qual territorio deseja adicionar tropas {self.name}?\n{[territory.name for territory in territory_list]}\n")
                terr = self.get_territory(territory_name, territory_list)
                if terr is not None:
                    break
                print("Territorio invalido")

            while True:
                quantity = int(input("Quantas tropas deseja adicionar? "))
                if quantity <= troops_to_add and quantity > 0:
                    break
                print("Quantidade invalida de tropas")            

            terr.add_troops(quantity)
            troops_to_add -= quantity

    def get_territory(self, territory_name, territory_list):
        for territory in territory_list:
            if territory.name == territory_name:
                return territory
        return None

    def exchange_cards(self, exchange_number):
        cards_to_exchange = []
        while True:
            for _ in range(3):
                while True:
                    card_name = input(f"Qual carta deseja trocar?\n{[card.territory for card in self.cards]}\n")
                    card = self.get_card(card_name)
                    if card is not None:
                        break
                    print("Carta invalida")
                cards_to_exchange.append(card)
                self.cards.remove(card)
            if self.is_valid_exchange(cards_to_exchange):
                break
            print("Troca invalida")
            for card in cards_to_exchange:
                self.cards.append(card)
            cards_to_exchange = []
        # verficar se o jogador possui os territorios das cartas
        self.cards_that_have_territories(cards_to_exchange)

        self.add_troops(4+(exchange_number*2), self.territories)
        return cards_to_exchange

    def is_valid_exchange(self, cards_to_exchange):
        if len(cards_to_exchange) != 3:
            return False
        if self.same_symbol(cards_to_exchange):
            return True
        if self.diff_symbols(cards_to_exchange):
            return True
        return False

    # retorna true se as cartas tem o mesmo simbolo (deve contar o coringa)
    def same_symbol(self, cards_to_exchange):
        symbols = []
        for card in cards_to_exchange:
            if card.symbol != CORINGA:
                symbols.append(card.symbol)
        if len(set(symbols)) == 1:
            return True
        return False

    def diff_symbols(self, cards_to_exchange):
        num_coringas = 0
        symbols = []
        for card in cards_to_exchange:
            if card.symbol == CORINGA:
                num_coringas += 1
            else:
                symbols.append(card.symbol)
        if len(set(symbols)) + num_coringas == 3:
            return True
        return False

    def get_card(self, card_name):
        for card in self.cards:
            if card.territory == card_name:
                return card
        return None

    def cards_that_have_territories(self, cards_to_exchange):
        for card in cards_to_exchange:
            for territory in self.territories:
                if territory.name == card.territory:
                    territory.add_troops(2)


    

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