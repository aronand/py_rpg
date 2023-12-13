from item import Item
from itemrepository import ItemRepository

import pyray


class Game:
    __slots__ = ["__name"]

    def __init__(self, name: str):
        self.__name = name
        pyray.init_window(800, 600, self.__name)

    def run(self) -> None:
        while not pyray.window_should_close():
            pyray.begin_drawing()
            pyray.clear_background(pyray.WHITE)
            pyray.draw_text(self.__name, 100, 100, 24, pyray.BLACK)
            pyray.end_drawing()
        pyray.close_window()


def main() -> None:
    game = Game("py_rpg")
    game.run()


if __name__ == "__main__":
    main()
