import time

from item import Item
from itemrepository import ItemRepository

import pyray


class Game:
    __slots__ = ["__name", "__time", "__delta_time"]

    def __init__(self, name: str):
        self.__name = name
        # TODO: Create a separate time module to avoid a monolithic Game class
        self.__time = time.time()
        self.__delta_time = self.__time
        pyray.init_window(800, 600, self.__name)

    @property
    def delta_time(self) -> float:
        return self.__delta_time
    
    def __update_time(self) -> None:
        self.__delta_time = time.time() - self.__time
        self.__time = time.time()

    def run(self) -> None:
        while not pyray.window_should_close():
            self.__update_time()
            pyray.begin_drawing()
            pyray.clear_background(pyray.WHITE)
            pyray.draw_text(self.__name, 100, 100, 24, pyray.BLACK)
            pyray.draw_text(f"delta_time: {self.__delta_time:.4f}", 100, 145, 24, pyray.BLACK)
            pyray.end_drawing()
        pyray.close_window()


def main() -> None:
    game = Game("py_rpg")
    game.run()


if __name__ == "__main__":
    main()
