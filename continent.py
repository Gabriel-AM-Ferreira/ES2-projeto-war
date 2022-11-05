from territory import *

class Continent:
    def __init__(self, name, bonus, territories):
        self.name = name 
        self.bonus = bonus
        self.territories = []

        # adiciona territorios a lista
        for territory in territories:
            if territory.continent == name:
                self.territories.append(territory)
        print(f"Continente {self.name} criado com {[terr.name for terr in self.territories]} territorios")

    def is_complete(self, player):
        for territory in self.territories:
            if territory.owner != player:
                return False
        return True

    def conquer_continent (self, player):
        if self.is_complete(player):
            player.continents.append(self)

    def lose_continent (self, player):
        if self in player.continents:
            player.continents.remove(self)