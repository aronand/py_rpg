from pathlib import Path

import pyray

from item import Item
from itemloader import ItemLoader
from itemrepository import ItemRepository


def main() -> None:
    items_json: Path = Path(__file__).parent.joinpath("data", "items.json")
    loader = ItemLoader()
    item_repo = ItemRepository()
    for item in loader.json_to_item_generator(items_json):
        item_repo.add_item(item)

    pyray.init_window(800, 600, "py_rpg")
    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(pyray.WHITE)
        pyray.draw_text(item_repo[0].name, 50, 50, 24, pyray.BLACK)
        pyray.draw_text(item_repo[1].name, 50, 75, 24, pyray.BLACK)
        pyray.end_drawing()
    pyray.close_window()


if __name__ == "__main__":
    main()
