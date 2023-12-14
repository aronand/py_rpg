import time

from pathlib import Path

from character import Character
from itemloader import ItemLoader
from itemrepository import ItemRepository

import pyray


class Game:
    __slots__ = ["__characters", "__item_repository", "__name", "__time", "__delta_time"]

    def __init__(self, name: str):
        self.__name = name
        self.__characters: list[Character] = [
            Character("Mike", pyray.Vector2(384, 160)),
            Character("John", pyray.Vector2(32, 64)),
            Character("Player"),
        ]
        self.__item_repository = ItemRepository()
        self.__load_items()
        # TODO: Create a separate time module to avoid a monolithic Game class
        self.__time = time.time()
        self.__delta_time = self.__time
        pyray.init_window(800, 600, self.__name)

    def __load_items(self) -> None:
        items_json: Path = Path(__file__).parent.joinpath("assets", "items.json")
        loader = ItemLoader()
        for item in loader.json_to_item_generator(items_json):
            self.__item_repository.add_item(item)

    @property
    def delta_time(self) -> float:
        return self.__delta_time

    def __update_time(self) -> None:
        self.__delta_time = time.time() - self.__time
        self.__time = time.time()

    def __get_player_input(self) -> None:
        # TODO: For testing purposes this is fine, but long-term this is far from optimal
        plr = self.__characters[2]
        if not plr.is_moving:
            if pyray.is_key_down(pyray.KEY_W):
                plr.move_to(pyray.Vector2(plr.pos_x, plr.pos_y - 32))
            if pyray.is_key_down(pyray.KEY_S):
                plr.move_to(pyray.Vector2(plr.pos_x, plr.pos_y + 32))
            if pyray.is_key_down(pyray.KEY_A):
                plr.move_to(pyray.Vector2(plr.pos_x - 32, plr.pos_y))
            if pyray.is_key_down(pyray.KEY_D):
                plr.move_to(pyray.Vector2(plr.pos_x + 32, plr.pos_y))

    def __update(self) -> None:
        self.__update_time()
        self.__get_player_input()
        for chr in self.__characters:
            if not chr.is_moving:
                continue
            chr.update_position(self.delta_time)

    def __render_characters(self) -> None:
        for chr in self.__characters:
            font_size = 18
            pos_x = int(chr.pos_x)
            pos_y = int(chr.pos_y)
            next_x = int(chr.next_x)
            next_y = int(chr.next_y)
            pyray.draw_rectangle(pos_x, pos_y, 32, 32, pyray.BEIGE)
            # Debug information
            pyray.draw_text(chr.name, pos_x, pos_y - font_size, font_size, pyray.BLACK)
            pyray.draw_text(f"X: {pos_x}/{next_x}", pos_x, pos_y + font_size * 2, font_size, pyray.BLACK)
            pyray.draw_text(f"Y: {pos_y}/{next_y}", pos_x, pos_y + font_size * 3, font_size, pyray.BLACK)

    def __render_debug_information(self) -> None:
        pyray.draw_text(self.__name, 100, 100, 24, pyray.BLACK)
        pyray.draw_text(f"delta_time: {self.__delta_time:.4f}", 100, 145, 24, pyray.BLACK)
        pyray.draw_text(self.__item_repository[0].name, 100, 190, 24, pyray.BLACK)
        pyray.draw_text(self.__item_repository[1].name, 100, 235, 24, pyray.BLACK)

    def __render(self) -> None:
        pyray.begin_drawing()
        pyray.clear_background(pyray.WHITE)
        self.__render_characters()
        self.__render_debug_information()
        pyray.end_drawing()

    def run(self) -> None:
        # TODO: Delete these after testing
        chr = self.__characters[0]
        new_position = pyray.Vector2(chr.pos_x + 128, chr.pos_y + 64)
        chr.move_to(new_position)

        while not pyray.window_should_close():
            self.__update()
            self.__render()
        pyray.close_window()


def main() -> None:
    game = Game("py_rpg")
    game.run()


if __name__ == "__main__":
    main()
