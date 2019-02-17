import unittest
from game.player import Player
from game.rooms import Room
from game.game import GameFlags


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.start_location = Room()
        self.player = Player('chandler', self.start_location, GameFlags())

    def test_go_valid_destination(self):
        destination = Room()
        self.player.location.neighbors = {'dest': destination}
        self.player.go('dest')
        self.assertEqual(self.player.location, destination)

    def test_go_invalid_destination(self):
        self.player.go('invalid')
        self.assertEqual(self.player.location, self.start_location)
