import unittest
from player import *
from unittest.mock import patch, MagicMock
from territory import *
import inputPlayer

class PlayerTester(unittest.TestCase):



    def setUp(self):
        self.playerDefault = Player("Tester")
        self.territoryDefault = Territory(ALASCA, AMERICA_DO_NORTE, [MACKENZIE, VANCOUVER, VLADIVOSTOK], 1)
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

    def test_should_increase_number_of_troops_in_card_territory(self):
        

    
