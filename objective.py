import re
from constants import AMERICA_DO_NORTE, AMERICA_DO_SUL, AFRICA, EUROPA, ASIA, OCEANIA
from getObject import is_continent_owned_by_player
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

        elif re.search(AMERICA_DO_NORTE, self.description):
            if re.search(OCEANIA, self.description):
                return is_continent_owned_by_player(AMERICA_DO_NORTE, self.owner) and is_continent_owned_by_player(OCEANIA, self.owner)
            elif re.search(AFRICA, self.description): 
                return is_continent_owned_by_player(AMERICA_DO_NORTE, self.owner) and is_continent_owned_by_player(AFRICA, self.owner)

        elif re.search(ASIA, self.description):
            if re.search(AMERICA_DO_SUL, self.description):
                return is_continent_owned_by_player(ASIA, self.owner) and is_continent_owned_by_player(AMERICA_DO_SUL, self.owner)
            if re.search(AFRICA, self.description):
                return is_continent_owned_by_player(ASIA, self.owner) and is_continent_owned_by_player(AFRICA, self.owner)

        elif re.search(EUROPA, self.description) and len(self.owner.continents)>=3:
            if re.search(AMERICA_DO_SUL, self.description):
                return is_continent_owned_by_player(EUROPA, self.owner) and is_continent_owned_by_player(AMERICA_DO_SUL, self.owner)
            elif re.search(OCEANIA, self.description):
                return is_continent_owned_by_player(EUROPA, self.owner) and is_continent_owned_by_player(OCEANIA, self.owner)

        return False

    def conquer(self, continent):
        for cont in self.owner.continents:
            if cont.name == continent:
                return True
        return False

    # verificar se o objetivo é destruir
    def destroy(self):
        for d_p in self.owner.defeated_players:
            if d_p.color in self.description:
                return True

    # verificar se o objetivo é conquistar
    def conquer(self):
        type = self.description.split(" ")[1]
        if type == "24":
            return self.conquer_24()
        elif type == "18":
            return self.conquer_18()
        else:
            return self.conquer_continents()

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
