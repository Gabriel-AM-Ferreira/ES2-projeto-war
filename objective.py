import re
from constants import AMERICA_DO_NORTE, AMERICA_DO_SUL, AFRICA, EUROPA, ASIA, OCEANIA
from getObject import get_object_by_name
class Objective:
    def __init__(self, description):
        self.description = description
        self.owner = None

    # verificar se o objetivo do jogador foi concluído
    def is_complete(self):
        if re.search('24', self.description):
            return self.conquer_24()

        elif re.search('18', self.description):
            return self.conquer_18()

        elif re.search('Destruir', self.description):
            return self.destroy()

        elif re.search(AMERICA_DO_NORTE, self.description) and get_object_by_name(AMERICA_DO_NORTE, self.owner.continents) is not None:
            if re.search(OCEANIA, self.description):
                return get_object_by_name(OCEANIA, self.owner.continents) is not None
            elif re.search(AFRICA, self.description): 
                return get_object_by_name(AFRICA, self.owner.continents) is not None

        elif re.search(ASIA, self.description) and get_object_by_name(ASIA, self.owner.continents) is not None:
            if re.search(AMERICA_DO_SUL, self.description):
                return get_object_by_name(AMERICA_DO_SUL, self.owner.continents) is not None
            if re.search(AFRICA, self.description):
                return get_object_by_name(AFRICA, self.owner.continents) is not None

        elif re.search(EUROPA, self.description) and get_object_by_name(EUROPA, self.owner.continents) is not None and len(self.owner.continents)>=3:
            if re.search(AMERICA_DO_SUL, self.description):
                return get_object_by_name(AMERICA_DO_SUL, self.owner.continents) is not None
            elif re.search(OCEANIA, self.description):
                return get_object_by_name(OCEANIA, self.owner.continents) is not None
        return False

    # verificar se o objetivo é destruir
    def destroy(self):
        for d_p in self.owner.defeated_players:
            if d_p.color in self.description:
                return True
        return False
        
    # verificar se o jogador conquistou 24 territorios
    def conquer_24(self):
        if len(self.owner.territories) >= 24:
            return True
        return False

    # verificar se o jogador conquistou 18 territorios
    def conquer_18(self):
        count  = 0
        for terr in self.owner.territories:
            if terr.troupes >= 2:
                count += 1
        return count >= 18
