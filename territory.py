from player import *

class Territory:
    def __init__(self, name, continent, neighbors_list, troops):
        self.name = name
        self.continent = continent
        self.neighbors = neighbors_list
        self.troops = troops
        self.owner = ""

    