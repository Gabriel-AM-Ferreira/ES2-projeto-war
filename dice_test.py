import unittest
from random import randint
from dice import *

class DiceTest(unittest.TestCase):

    def setUp(self):
        self.defaultDice = Dice(6)
    
    def test_should_roll_a_number_bettwen_one_and_six(self):
        numberRolled = self.defaultDice.roll()
        self.assertTrue(numberRolled>0 and numberRolled <7)
    
    
