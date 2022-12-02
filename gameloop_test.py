import unittest
from player import *
from territory import *
from gameloop import *


class GameloopTest(unittest.TestCase):

    def setUp(self):
        self.gameLoop = GameLoop(0,4)

    def test_should_have_all_territories(self):
        self.assertEqual(len(self.gameLoop.territories),42)

    def test_should_have_all_continents(self):
        self.assertEqual(len(self.gameLoop.continents),6)

    def test_all_territories_should_have_diferent_owners(self):
        owners = []
        for territory in self.gameLoop.territories:
            if territory.owner not in owners:
                owners.append(territory.owner)
        self.assertEqual(len(owners),4)