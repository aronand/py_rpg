from unittest import TestCase

from item import Item


class TestItemCreation(TestCase):
    name = "Test Item"
    description = "Item for testing purposes."
    item: Item

    def setUp(self) -> None:
        self.item = Item(self.name, self.description)
    
    def test_name_is_correct(self) -> None:
        self.assertEqual(self.name, self.item.name)
    
    def test_description_is_correct(self) -> None:
        self.assertEqual(self.description, self.item.description)
