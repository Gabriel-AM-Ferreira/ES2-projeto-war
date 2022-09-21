from territory import *

class Continent:
    def __init__(self, name, bonus, territories):
        self.name = name 
        self.bonus = bonus
        self.territories = []

        # adiciona territorios a lista
        for territory in territories:
            if territory.continent == name:
                self.territories.append(territory.name)
