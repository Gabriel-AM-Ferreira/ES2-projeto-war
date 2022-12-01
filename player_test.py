import unittest
from player import *
from unittest.mock import patch
from unittest.mock import MagicMock
from territory import *
from inputPlayer import ask_territory
from inputPlayer import ask_quantity

class PlayerTester(unittest.TestCase):



    def setUp(self):
        self.playerDefault = Player("Tester")
        self.territoryDefault = Territory(ALASCA, AMERICA_DO_NORTE, [MACKENZIE, VANCOUVER, VLADIVOSTOK], 1)
        self.territoryList = []
        self.territoryList.append(self.territoryDefault)
        self.playerDefault.add_territory(self.territoryDefault)
        #ask_territory(10,"Qual territorio deseja adicionar tropas?") 
        


    @unittest.skip("demonstrating skipping")
    def test_constructor(self):

        self.assertEqual(self.playerDefault,Player("Tester"))


    def test_tautologia(self):
        self.assertEqual("a","a")
    
    @patch('inputPlayer.ask_territory')
    @patch('inputPlayer.ask_quantity')
    def test_should_add_troops(self,mock_ask_territory,mock_ask_quantity):
        
        ask_territory = MagicMock(return_value=self.territoryDefault.name)
        ask_quantity = MagicMock(return_value=3)
        mock_ask_territory.return_value = self.territoryDefault.name
        mock_ask_quantity.return_value = 3
        original_troops = self.territoryDefault.troops

        #iP.ask_territory = MagicMock(return_value=self.territoryDefault.name)
        #iP.ask_quantity = MagicMock(return_value=3)
        
        print(ask_territory(self.territoryList,"Qual territorio deseja adicionar tropas?"))
        print(ask_quantity(3,"Quantas tropas deseja adicionar?"))
        self.playerDefault.add_troops(9,self.territoryList)
        self.assertEqual(self.territoryDefault.troops, original_troops+9)

