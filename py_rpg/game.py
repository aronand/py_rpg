import logging

from pathlib import Path

import raywrap

from character import Character
from core import Node, Time
from itemloader import ItemLoader
from itemrepository import ItemRepository

import pyray


def generate_test_scene() -> Node:
    player_texture = pyray.load_texture(str(Path(__file__).parent.joinpath("assets", "test_player.png")))
    npc_texture = pyray.load_texture(str(Path(__file__).parent.joinpath("assets", "test_npc.png")))

    player = Character("Player")
    player.texture = player_texture
    mike = Character("Mike", pyray.Vector2(384, 160))
    mike.texture = npc_texture
    john = Character("John", pyray.Vector2(32, 64))
    john.texture = npc_texture

    scene = Node("test_scene")
    characters = Node("Characters", scene)
    characters.add_child(player)
    characters.add_child(mike)
    characters.add_child(john)
    return scene


class Game:
    __slots__ = ["__debug_mode", "__item_repository", "__scene", "__characters", "__name"]

    def __init__(self, name: str, debug_mode: bool):
        self.__name = name
        self.__debug_mode = debug_mode
        pyray.init_window(800, 600, self.__name)
        self.__scene: Node = generate_test_scene()
        self.__characters: Node = self.__get_characters()
        self.__item_repository = self.__load_items()

    def __get_characters(self) -> Node:
        characters: Node | None = self.__scene.find_child("Characters")
        if characters is None:
            raise RuntimeError
        return characters

    def __load_items(self) -> ItemRepository:
        item_repo = ItemRepository()
        loader = ItemLoader()
        items_json: Path = Path(__file__).parent.joinpath("assets", "items.json")
        for item in loader.json_to_item_generator(items_json):
            logging.info(f"[ITEMS] {item.name} loaded")
            item_repo.add_item(item)
        return item_repo

    @property
    def debug_mode(self) -> bool:
        return self.__debug_mode

    def __get_player_input(self) -> None:
        # TODO: For testing purposes this is fine, but long-term this is far from optimal
        player = self.__characters.child_nodes[0]
        if not isinstance(player, Character):
            return
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
        Time.update()
        self.__get_player_input()
        for chr in self.__characters.child_nodes:
            if not isinstance(chr, Character):
                continue
            if not chr.is_moving:
                continue
            chr.update_position()

    def __render_characters(self) -> None:
        for chr in self.__characters.child_nodes:
            if not isinstance(chr, Character):
                continue
            font_size = 18
            pos_x = int(chr.pos_x)
            pos_y = int(chr.pos_y)
            if chr.texture is None:
                pyray.draw_rectangle(pos_x, pos_y, 32, 32, pyray.MAGENTA)
            else:
                pyray.draw_texture(chr.texture, pos_x, pos_y, pyray.Color(255, 255, 255, 255))
            pyray.draw_text(chr.character_name, pos_x, pos_y - font_size, font_size, pyray.BLACK)
            # Debug information
            if not self.debug_mode:
                continue
            next_x = int(chr.next_x)
            next_y = int(chr.next_y)
            pyray.draw_text(f"X: {pos_x}/{next_x}", pos_x, pos_y + font_size * 2, font_size, pyray.BLACK)
            pyray.draw_text(f"Y: {pos_y}/{next_y}", pos_x, pos_y + font_size * 3, font_size, pyray.BLACK)

    def __render_debug_information(self) -> None:
        pyray.draw_text(self.__name, 100, 100, 24, pyray.BLACK)
        pyray.draw_text(f"delta_time: {Time.delta_time:.4f}", 100, 145, 24, pyray.BLACK)
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
        chr = self.__characters.child_nodes[1]
        if isinstance(chr, Character):
            new_position = pyray.Vector2(chr.pos_x + 128, chr.pos_y + 64)
            chr.move_to(new_position)

        while not pyray.window_should_close():
            self.__update()
            self.__render()
        pyray.close_window()
