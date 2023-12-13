import json

from unittest import TestCase
from unittest.mock import patch, mock_open

from item import Item
from itemloader import ItemLoader


class TestItemLoader(TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"name": "Test", "description": ""}]))
    def test_loading_json(self, filemock) -> None:
        loader = ItemLoader()
        itm: Item = next(loader.json_to_item_generator("some_path"))
        self.assertEqual("Test", itm.name)
