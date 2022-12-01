import unittest
from continent import *
from territory import *
from player import *
from getObject import get_object_by_name
from unittest.mock import patch, MagicMock

class ContinentTest(unittest.TestCase):

    def setUp(self):
        self.territories = []
        self.territories.append(Territory(SUMATRA, OCEANIA, [INDIA, AUSTRALIA], TROPAS_MINIMAS))
        self.territories.append(Territory(BORNEU, OCEANIA, [VIETNA, AUSTRALIA, NOVA_GUINE], TROPAS_MINIMAS))
        self.territories.append(Territory(AUSTRALIA, OCEANIA, [SUMATRA, BORNEU, NOVA_GUINE], TROPAS_MINIMAS))
        self.territories.append(Territory(NOVA_GUINE, OCEANIA, [AUSTRALIA, BORNEU], TROPAS_MINIMAS))
        self.continentDefault = Continent(OCEANIA, BONUS_OCEANIA, self.territories)
        self.playerDefault = Player("Tester")

    def test_should_return_a_completed_continent(self):
        for territory in self.continentDefault.territories:
            territory.owner = self.playerDefault
        self.assertTrue(self.continentDefault.is_complete(self.playerDefault))

    def test_should_give_false_with_incomplete_continent(self):
        self.assertFalse(self.continentDefault.is_complete(self.playerDefault))

    def test_should_give_continent_to_player(self):
        original_number_of_continents = len(self.playerDefault.continents)
        for territory in self.continentDefault.territories:
            territory.owner = self.playerDefault
        self.continentDefault.conquer_continent(self.playerDefault)
        self.assertEqual(len(self.playerDefault.continents),original_number_of_continents+1)
    
    def test_should_take_continent_from_player(self):
        self.playerDefault.continents.append(self.continentDefault)
        original_number_of_continents = len(self.playerDefault.continents)
        self.continentDefault.lose_continent(self.playerDefault)
        self.assertEqual(len(self.playerDefault.continents),original_number_of_continents-1)


