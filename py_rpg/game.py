import logging

from pathlib import Path

import raywrap

from character import Character
from core import Label, Node, RenderableNode, Texture, Time
from itemloader import ItemLoader
from itemrepository import ItemRepository

import pyray


def generate_test_scene() -> Node:
    player_texture = pyray.load_texture(str(Path(__file__).parent.joinpath("assets", "test_player.png")))
    npc_texture = pyray.load_texture(str(Path(__file__).parent.joinpath("assets", "test_npc.png")))

    player = Character("Player")
    player.add_child(Texture(player_texture))
    player.add_child(Label("Player"))
    mike = Character("Mike", pyray.Vector2(384, 160))
    mike.add_child(Texture(npc_texture))
    mike.add_child(Label("Mike"))
    john = Character("John", pyray.Vector2(32, 64))
    john.add_child(Texture(npc_texture))
    john.add_child(Label("John"))

    scene = Node("test_scene")
    characters = Node("Characters", scene)
    characters.add_child(player)
    characters.add_child(mike)
    characters.add_child(john)

    # As this Texture is parented to a Node, which has no position, its position should be only affected by itself
    texture_test_parent = Node(parent=scene)
    texture_test = Texture(npc_texture)
    texture_test.position = pyray.Vector2(700, 500)
    texture_test_parent.add_child(texture_test)

    return scene


class Game:
    __slots__ = "__debug_mode", "__item_repository", "__scene", "__characters", "__name", "__renderables"

    def __init__(self, name: str, debug_mode: bool):
        self.__name = name
        self.__debug_mode = debug_mode
        pyray.init_window(800, 600, self.__name)
        self.__scene: Node = generate_test_scene()
        self.__characters: Node = self.__get_characters()
        self.__renderables: list[RenderableNode] = []
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

    def __update_node_recursive(self, node: Node) -> None:
        for child in node.child_nodes:
            self.__update_node_recursive(child)
        if isinstance(node, RenderableNode):
            self.__renderables.append(node)
        node.update()

    def __update(self) -> None:
        Time.update()
        self.__get_player_input()
        self.__update_node_recursive(self.__scene)

    def __render_debug_information(self) -> None:
        pyray.draw_text(self.__name, 100, 100, 24, pyray.BLACK)
        pyray.draw_text(f"delta_time: {Time.delta_time:.4f}", 100, 145, 24, pyray.BLACK)
        pyray.draw_text(self.__item_repository[0].name, 100, 190, 24, pyray.BLACK)
        pyray.draw_text(self.__item_repository[1].name, 100, 235, 24, pyray.BLACK)

    def __render(self) -> None:
        with raywrap.drawing():
            pyray.clear_background(pyray.WHITE)
            for renderable in self.__renderables:
                renderable.render()
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
