from player import *

class Territory:
    def __init__(self, name, continent, neighbors_list, num_armies):
        self.name = name
        self.continent = continent
        self.neighbors = neighbors_list
        self.num_armies = num_armies
        self.owner = ""
    