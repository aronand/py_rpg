import logging
import time

from pathlib import Path

import raywrap

from character import Character
from core import Node
from itemloader import ItemLoader
from itemrepository import ItemRepository

import pyray


def generate_test_scene() -> Node:
    scene = Node("test_scene")
    characters = Node("Characters")
    characters.add_child(Character("Player"))
    characters.add_child(Character("Mike", pyray.Vector2(384, 160)))
    characters.add_child(Character("John", pyray.Vector2(32, 64)))
    scene.add_child(characters)
    return scene


class Game:
    __slots__ = ["__characters", "__debug_mode", "__item_repository", "__scene", "__name", "__time", "__delta_time"]

    def __init__(self, name: str, debug_mode: bool):
        self.__name = name
        self.__debug_mode = debug_mode
        pyray.init_window(800, 600, self.__name)
        self.__scene: Node = generate_test_scene()
        self.__characters: list[Character] = [
            Character("Player"),
            Character("Mike", pyray.Vector2(384, 160)),
            Character("John", pyray.Vector2(32, 64)),
        ]
        self.__item_repository = self.__load_items()
        # TODO: Create a separate time module to avoid a monolithic Game class
        self.__time: float = time.time()
        self.__delta_time: float = self.__time

    def __load_items(self) -> ItemRepository:
        item_repo = ItemRepository()
        loader = ItemLoader()
        items_json: Path = Path(__file__).parent.joinpath("assets", "items.json")
        for item in loader.json_to_item_generator(items_json):
            logging.info(f"[ITEMS] {item.name} loaded")
            item_repo.add_item(item)
        return item_repo

    @property
    def delta_time(self) -> float:
        return self.__delta_time

    @property
    def debug_mode(self) -> bool:
        return self.__debug_mode

    def __update_time(self) -> None:
        self.__delta_time = time.time() - self.__time
        self.__time = time.time()

    def __get_player_input(self) -> None:
        # TODO: For testing purposes this is fine, but long-term this is far from optimal
        player = self.__characters[0]
        if not player.is_moving:
            if pyray.is_key_down(pyray.KEY_W):
                player.move_to(pyray.Vector2(player.pos_x, player.pos_y - 32))
            if pyray.is_key_down(pyray.KEY_S):
                player.move_to(pyray.Vector2(player.pos_x, player.pos_y + 32))
            if pyray.is_key_down(pyray.KEY_A):
                player.move_to(pyray.Vector2(player.pos_x - 32, player.pos_y))
            if pyray.is_key_down(pyray.KEY_D):
                player.move_to(pyray.Vector2(player.pos_x + 32, player.pos_y))

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
            pyray.draw_text(chr.character_name, pos_x, pos_y - font_size, font_size, pyray.BLACK)
            # Debug information
            if not self.debug_mode:
                continue
            pyray.draw_text(f"X: {pos_x}/{next_x}", pos_x, pos_y + font_size * 2, font_size, pyray.BLACK)
            pyray.draw_text(f"Y: {pos_y}/{next_y}", pos_x, pos_y + font_size * 3, font_size, pyray.BLACK)

    def __render_debug_information(self) -> None:
        pyray.draw_text(self.__name, 100, 100, 24, pyray.BLACK)
        pyray.draw_text(f"delta_time: {self.__delta_time:.4f}", 100, 145, 24, pyray.BLACK)
        pyray.draw_text(self.__item_repository[0].name, 100, 190, 24, pyray.BLACK)
        pyray.draw_text(self.__item_repository[1].name, 100, 235, 24, pyray.BLACK)

    def __render(self) -> None:
        with raywrap.drawing():
            pyray.clear_background(pyray.WHITE)
            self.__render_characters()
            if self.debug_mode:
                self.__render_debug_information()

    def run(self) -> None:
        # TODO: Delete these after testing
        chr = self.__characters[1]
        new_position = pyray.Vector2(chr.pos_x + 128, chr.pos_y + 64)
        chr.move_to(new_position)

        while not pyray.window_should_close():
            self.__update()
            self.__render()
        pyray.close_window()
