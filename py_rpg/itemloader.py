import json
from pathlib import Path
from typing import Generator

from item import Item


class ItemLoader:
    def __init__(self) -> None:
        pass

    def json_to_item_generator(self, path: Path) -> Generator[Item, None, None]:
        """
        Generate Item objects from the specified JSON file.

        :yields: Item
        """
        with open(path, "r") as item_json:
            parsed_json = json.load(item_json)

        for item in parsed_json:
            name: str = item["name"]
            description: str = item["description"]
            yield Item(name, description)
