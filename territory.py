from player import *

class Territory:
    def __init__(self, name, continent, neighbors_list, troops, cordenada):
        self.name = name
        self.continent = continent
        self.neighbors = neighbors_list
        self.troops = troops
        self.cordenadas = cordenada
        self.owner = None

    