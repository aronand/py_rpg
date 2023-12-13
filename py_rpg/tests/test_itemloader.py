from unittest import TestCase
from unittest.mock import patch, mock_open

from item import Item
from itemloader import ItemLoader


class TestItemLoader(TestCase):
    @patch("builtins.open", mock_open(read_data='[{"name": "Test", "description": ""}]'))
    def test_loading_json(self, filemock) -> None:
        loader = ItemLoader()
        itm: Item = next(loader.json_to_item_generator(filemock))
        self.assertEqual("Test", itm.name)
