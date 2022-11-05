import re
from constants import AMERICA_DO_NORTE, AMERICA_DO_SUL, AFRICA, EUROPA, ASIA, OCEANIA
from getObject import get_object_by_name
class Objective:
    def __init__(self, description):
        self.description = description
        self.owner = None

    # verificar se o objetivo do jogador foi concluído
    def is_complete(self):
        # objetivo é conquistar 24 territorios
        if re.search('24', self.description):
            return len(self.owner.territories) >= 24 
        # objetivo é conquistar 18 territorios
        elif re.search('18', self.description):
            return self.conquer_18()
        # objetivo é destruir um jogador
        elif re.search('Destruir', self.description):
            return self.destroy()
        # objetivo é conquistar America do Norte
        elif re.search(AMERICA_DO_NORTE, self.description) and get_object_by_name(AMERICA_DO_NORTE, self.owner.continents) is not None:
            if re.search(OCEANIA, self.description): # Com Oceania
                return get_object_by_name(OCEANIA, self.owner.continents) is not None
            elif re.search(AFRICA, self.description):  # Com Africa
                return get_object_by_name(AFRICA, self.owner.continents) is not None
        # objetivo é conquistar Asia
        elif re.search(ASIA, self.description) and get_object_by_name(ASIA, self.owner.continents) is not None:
            if re.search(AMERICA_DO_SUL, self.description): # Com America do Sul
                return get_object_by_name(AMERICA_DO_SUL, self.owner.continents) is not None
            if re.search(AFRICA, self.description): # Com Africa
                return get_object_by_name(AFRICA, self.owner.continents) is not None
        # objetivo é conquistar Europa, um continente da sua escolha e
        elif re.search(EUROPA, self.description) and get_object_by_name(EUROPA, self.owner.continents) is not None and len(self.owner.continents)>=3:
            if re.search(AMERICA_DO_SUL, self.description): # America do Sul
                return get_object_by_name(AMERICA_DO_SUL, self.owner.continents) is not None
            elif re.search(OCEANIA, self.description): # Oceania
                return get_object_by_name(OCEANIA, self.owner.continents) is not None
        return False

    # verificar se o jogador destruiu um jogador de certa cor
    def destroy(self):
        for d_p in self.owner.defeated_players:
            if re.search(d_p.color, self.description):
                return True
        return False

    # verificar se o jogador conquistou 18 territorios
    def conquer_18(self):
        count  = 0
        for terr in self.owner.territories:
            if terr.troupes >= 2:
                count += 1
        return count >= 18
