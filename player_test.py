import unittest
from player import *
from territory import *
from unittest.mock import patch, MagicMock
from territory import *
from continent import *
from card import *
import inputPlayer

class PlayerTester(unittest.TestCase):

    

    def setUp(self):
        self.playerDefault = Player("Tester")
        self.territoryDefault = Territory(ALASCA, AMERICA_DO_NORTE, [MACKENZIE, VANCOUVER, VLADIVOSTOK], 1)
        self.neighborDefault = Territory(MACKENZIE, AMERICA_DO_NORTE, [ALASCA, VANCOUVER, GROELANDIA, OTTAWA], TROPAS_MINIMAS)
        self.territoryList = []
        self.territoryList.append(self.territoryDefault)
        self.playerDefault.add_territory(self.territoryDefault)
        #ask_territory(10,"Qual territorio deseja adicionar tropas?") 

    @unittest.skip("demonstrating skipping")    
    def add_troops2(self):
        original_troops = self.territoryDefault.troops
        with patch("player.ask_territory") as mockask:
            mockask.return_value = self.territoryDefault
            self.playerDefault.add_troops(9,self.territoryList)
            self.assertEqual(self.territoryDefault.troops, original_troops+9)    

    @patch('player.ask_territory')
    @patch('player.ask_quantity')
    def test_should_add_troops(self,mock_qtd,mock_terr):
        
        mock_terr.return_value = self.territoryDefault
        mock_qtd.return_value = 3
        
        original_troops = self.territoryDefault.troops

        self.playerDefault.add_troops(9,self.territoryList)
        self.assertEqual(self.territoryDefault.troops, original_troops+9)

    def test_should_increase_number_of_troops_in_card_territory_by_two(self):
        card_list = []
        card_alasca = Card(ALASCA,TRIANGULO)
        card_list.append(card_alasca)
        tropas_originais = self.playerDefault.territories[0].troops
        self.playerDefault.cards_that_have_territories(card_list)
        self.assertEqual(self.playerDefault.territories[0].troops, tropas_originais+2)

    def test_should_return_correct_number_of_troops(self):
        self.assertEqual(self.playerDefault.get_troops_by_exchange(3),10)

    def test_shouldnt_give_minor_number_of_troops(self):
        self.assertNotEqual(self.playerDefault.get_troops_by_exchange(2),5)

    @patch('player.ask_territory')
    @patch('territory.Territory.get_hostile_neighbors')
    def test_should_return_valid_territory_when_asked_to_attack(self,mock_neighbors,mock_terr):
        mock_terr.return_value = self.territoryDefault
        mock_neighbors.return_value = [self.neighborDefault]
        self.playerDefault.territories[0].troops = self.playerDefault.territories[0].troops + 1
        self.assertEqual(self.playerDefault.get_attacking_territory(),self.territoryDefault)

    @patch('player.ask_territory')
    @patch('player.ask_yes_or_no')
    @patch('territory.Territory.get_hostile_neighbors')
    def test_should_return_none_when_asked_to_attack_with_no_valid_territory(self,mock_neighbors,mock_yes_no,mock_terr):
        mock_terr.return_value = self.territoryDefault
        mock_neighbors.return_value = [self.neighborDefault]
        mock_yes_no.return_value = False
        self.assertEqual(self.playerDefault.get_attacking_territory(),None)

    @patch('player.ask_territory')
    @patch('territory.Territory.get_hostile_neighbors')
    def test_should_return_valid_territory_when_asked_where_to_attack(self,mock_neighbors,mock_terr):
        mock_terr.return_value = self.territoryDefault
        mock_neighbors.return_value = [self.neighborDefault]
        self.assertEqual(self.playerDefault.get_defending_territory(self.territoryDefault),self.territoryDefault)

    def test_should_add_a_territory_to_player(self):
        number_of_territories =len(self.playerDefault.territories)
        self.playerDefault.add_territory(self.neighborDefault)
        self.assertEqual(len(self.playerDefault.territories),number_of_territories+1)

    def test_should_remove_a_territory_from_player(self):
        number_of_territories =len(self.playerDefault.territories)
        self.playerDefault.remove_territory(self.territoryDefault)
        self.assertEqual(len(self.playerDefault.territories),number_of_territories-1)

    def test_should_add_a_continent_to_player(self):
        territory_in_africa = Territory(ARGELIA, AFRICA, [BRASIL,  FRANCA, EGITO, SUDAO, CONGO], TROPAS_MINIMAS)
        continente_do_teste = Continent(AFRICA, BONUS_ASIA, [territory_in_africa])
        number_of_continents = len(self.playerDefault.continents)
        self.playerDefault.add_continent(continente_do_teste)
        self.assertEqual(len(self.playerDefault.continents),number_of_continents+1)

    def test_should_remove_a_continent_from_player(self):
        territory_in_africa = Territory(ARGELIA, AFRICA, [BRASIL,  FRANCA, EGITO, SUDAO, CONGO], TROPAS_MINIMAS)
        continente_do_teste = Continent(AFRICA, BONUS_ASIA, [territory_in_africa])
        self.playerDefault.continents.append(continente_do_teste)
        number_of_continents = len(self.playerDefault.continents)
        self.playerDefault.remove_continent(continente_do_teste)
        self.assertEqual(len(self.playerDefault.continents),number_of_continents-1)

    @patch('player.ask_territory')
    @patch('territory.Territory.get_friendly_neighbors')
    def test_should_give_valid_territory_when_asked(self,mock_neighbors,mock_asked_territory):
        self.territoryDefault.troops = self.territoryDefault.troops +1 
        mock_asked_territory.return_value = self.territoryDefault
        mock_neighbors.return_value = [self.neighborDefault]
        self.assertEqual(self.playerDefault.ask_from_territory(),self.territoryDefault)

    @patch('player.ask_territory')
    @patch('player.ask_yes_or_no')
    @patch('territory.Territory.get_friendly_neighbors')
    def test_should_return_none_when_no_valid_territory_avaiable(self,mock_neighbors,mock_ask_yer_no,mock_asked_territory):
        
        mock_asked_territory.return_value = self.territoryDefault
        mock_neighbors.return_value = [self.neighborDefault]
        mock_ask_yer_no.return_value = False
        self.assertEqual(self.playerDefault.ask_from_territory(),None)

    @patch('player.ask_territory')
    @patch('territory.Territory.get_friendly_neighbors')
    def test_should_return_valid_move(self,mock_neighbors,mock_asked_territory):
        mock_asked_territory.return_value = self.neighborDefault
        mock_neighbors.return_value = [self.neighborDefault]
        self.assertEqual(self.playerDefault.ask_to_territory(self.territoryDefault),self.neighborDefault)

    
