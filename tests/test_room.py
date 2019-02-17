import unittest
from game.rooms import Room
from game.items import InventoryItem


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room()

    def test_get_item_pop(self):
        item = InventoryItem('thing', 'This is a test InventoryItem')
        self.room.contents.append(item)
        self.room.get_item(item.name.lower())
        self.assertNotIn(item, self.room.contents)
