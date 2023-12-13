from unittest import TestCase

from item import Item
from itemrepository import ItemRepository


class TestItemRepository(TestCase):
    item_repository: ItemRepository

    def setUp(self) -> None:
        self.item_repository = ItemRepository()

    def test_adding_item_object(self) -> None:
        item = Item("Added", "Added test item.")
        self.item_repository.add_item(item)
        self.assertEqual("Added", self.item_repository[0].name)

    def test_creating_item(self) -> None:
        self.item_repository.create_item("Created", "Created test item.")
        self.assertEqual("Created", self.item_repository[0].name)
    
    def test_len(self) -> None:
        self.assertEqual(0, len(self.item_repository))
        self.item_repository.create_item("Test", "Test")
        self.assertEqual(1, len(self.item_repository))
    
    def test_removing_item_that_exists(self) -> None:
        with self.subTest("Test index based removal."):
            self.item_repository.create_item("Created", "Created test item.")
            item = self.item_repository.remove_item(0)
            self.assertEqual("Created", item.name)
            self.assertEqual(0, len(self.item_repository))
        
        with self.subTest("Test name based removal."):
            self.item_repository.create_item("Created", "Created test item.")
            item = self.item_repository.remove_item("Created")
            self.assertEqual("Created", item.name)
            self.assertEqual(0, len(self.item_repository))
    
    def test_removing_item_that_doesnt_exist(self) -> None:
        with self.subTest("Test index based removal."):
            self.assertRaises(IndexError, self.item_repository.remove_item, 0)
        
        with self.subTest("Test name based removal."):
            self.assertRaises(ItemRepository.ItemNotFoundException,
                              self.item_repository.remove_item, "Item")

    def test_iterator(self) -> None:
        items = 5
        for i in range(items):
            item = Item(f"Item_{i}", "")
            self.item_repository.add_item(item)

        item_count = 0
        for item in self.item_repository:
            item_count += 1
        
        self.assertEqual(items, item_count)
