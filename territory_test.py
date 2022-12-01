import unittest
from constants import *
from territory import *
from player import *
from getObject import get_object_by_name
from unittest.mock import patch, MagicMock

class TerritoryTest(unittest.TestCase):

    

    def setUp(self):
        self.territories = []
        self.territories.append(Territory(VENEZUELA, AMERICA_DO_SUL, [MEXICO, PERU, BRASIL], TROPAS_MINIMAS))
        self.territories.append(Territory(PERU, AMERICA_DO_SUL, [VENEZUELA, BRASIL, ARGENTINA], TROPAS_MINIMAS))
        self.territories.append(Territory(ARGENTINA, AMERICA_DO_SUL, [PERU, BRASIL], TROPAS_MINIMAS))
        self.territories.append(Territory(ARGELIA, AFRICA, [BRASIL,  FRANCA, EGITO, SUDAO, CONGO], TROPAS_MINIMAS))
        self.territoryDefault = Territory(BRASIL, AMERICA_DO_SUL, [VENEZUELA, PERU, ARGENTINA, ARGELIA], TROPAS_MINIMAS)
        neighbor_list = []
        for neighbor_name in self.territoryDefault.neighbors:
            neighbor_list.append(get_object_by_name(neighbor_name, self.territories))
        self.territoryDefault.neighbors = neighbor_list
        self.enemyPlayerDefault = Player("Inimigo")
        self.playerDefault = Player("Tester")
        self.territoryDefault.owner = self.playerDefault

    def test_should_add_correct_amount_of_troops(self):
        original_troops = self.territoryDefault.troops
        self.territoryDefault.add_troops(4)
        self.assertEqual(self.territoryDefault.troops, original_troops+4)

    def test_should_remove_correct_amount_of_troops(self):
        original_troops = self.territoryDefault.troops
        self.territoryDefault.remove_troops(1)
        self.assertEqual(self.territoryDefault.troops, original_troops-1)

    def test_should_give_all_enemies(self):
        for neightbor in self.territoryDefault.neighbors:
            neightbor.owner = self.playerDefault
        self.territoryDefault.neighbors[0].owner = self.enemyPlayerDefault
        self.assertEqual(len(self.territoryDefault.get_hostile_neighbors()),1)

    def test_should_give_all_allies(self):
        for neightbor in self.territoryDefault.neighbors:
            neightbor.owner = self.enemyPlayerDefault
        self.territoryDefault.neighbors[0].owner = self.playerDefault
        self.assertEqual(len(self.territoryDefault.get_friendly_neighbors()),1)