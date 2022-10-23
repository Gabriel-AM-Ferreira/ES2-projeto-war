from dice import *
from territory import *
from continent import *
class Player:
    def __init__(self, name):
        self.name = name
        self.color = ""
        self.objective = None
        self.cards = []
        self.territories = []
        self.continents = []


    def add_normal_troops(self, troops_to_add):
        territory_list = self.territories
        self.add_troops(troops_to_add, territory_list)

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
            pass
        elif option == 4:
            pass
        elif option == 5:
            break
        else:
            print("Opcao invalida")