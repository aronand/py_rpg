import logging

from pathlib import Path

import raywrap

from character import Character
from core import Label, Node, RenderableNode, Texture, Time
from itemloader import ItemLoader
from itemrepository import ItemRepository
from window import Window

import pyray


TILE_SIZE: int = 32


def create_character(name: str, texture: pyray.Texture2D, position: pyray.Vector2 = pyray.Vector2(0, 0)) -> Character:
    character = Character(node_name=name, character_name=name, position=position)
    Texture(parent=character, texture=texture)
    Label(parent=character, text=name)
    return character


def generate_test_scene() -> Node:
    player_texture = pyray.load_texture(str(Path(__file__).parent.joinpath("assets", "test_player.png")))
    npc_texture = pyray.load_texture(str(Path(__file__).parent.joinpath("assets", "test_npc.png")))

    character_list = [
        create_character("Player", player_texture),
        create_character("Mike", npc_texture, pyray.Vector2(384, 160)),
        create_character("John", npc_texture, pyray.Vector2(32, 64)),
        create_character("Peter", npc_texture, pyray.Vector2(32, 320))
    ]

    scene = Node("test_scene")
    characters = Node("Characters", scene)
    for character in character_list:
        characters.add_child(character)

    # As this Texture is parented to a Node, which has no position, its position should be only affected by itself
    texture_test = Node(parent=scene)
    Texture(parent=texture_test, texture=npc_texture, position=pyray.Vector2(700, 500))

    return scene


class Game:
    __slots__ = ("__debug_mode", "__item_repository", "__scene", "__characters", "__name", "__renderables",
                 "__camera", "__window")

    def __init__(self, name: str, debug_mode: bool):
        self.__name = name
        self.__debug_mode = debug_mode
        self.__window = Window(800, 600, self.__name)
        self.__camera = pyray.Camera2D()
        self.__camera.offset = pyray.Vector2(self.__window.width / 2, self.__window.height / 2)
        self.__camera.rotation = 0
        self.__camera.zoom = 1
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
        player = self.__characters.child_nodes[0]
        if not isinstance(player, Character):
            return
        mouse_position = pyray.get_mouse_position()
        mouse_world_position = pyray.get_screen_to_world_2d(mouse_position, self.__camera)
        # FIXME: This is the wrong place for this
        self.__camera.target = pyray.Vector2(player.position.x + TILE_SIZE, player.position.y + TILE_SIZE)
        if not player.is_moving:
            direction = pyray.vector2_zero()
            direction.x += pyray.is_key_down(pyray.KEY_D) - pyray.is_key_down(pyray.KEY_A)
            direction.y += pyray.is_key_down(pyray.KEY_S) - pyray.is_key_down(pyray.KEY_W)
            # Multiply axes by TILE_SIZE for tile based movement
            next_pos = pyray.Vector2(player.pos_x + direction.x, player.pos_y + direction.y)
            player.move_to(next_pos)
        if pyray.is_mouse_button_pressed(0):
            player.move_to(mouse_world_position)
        # Check who's under the cursor when pressing the right mouse button
        if pyray.is_mouse_button_pressed(1):
            for character in self.__characters.child_nodes:
                if not type(character) is Character:
                    continue
                rec = pyray.Rectangle(character.pos_x, character.pos_y, TILE_SIZE, TILE_SIZE)
                collision = pyray.check_collision_point_rec(mouse_world_position, rec)
                if collision:
                    logging.info(f"Clicked on {character.character_name}")
                    break

    def __update_node_recursive(self, node: Node, update_renderables: bool) -> None:
        for child in node.child_nodes:
            self.__update_node_recursive(child, update_renderables)
        if update_renderables and isinstance(node, RenderableNode):
            self.__renderables.append(node)
        node.update()

    def __update(self) -> None:
        Time.update()
        self.__get_player_input()
        update_renderables: bool = len(self.__renderables) == 0
        self.__update_node_recursive(self.__scene, update_renderables)

    def __render_debug_information(self) -> None:
        text_items: list[str] = [
            self.__name,
            f"FPS: {pyray.get_fps()}",
            f"delta_time: {Time.delta_time:.4f}",
            f"pyray.get_frame_time(): {pyray.get_frame_time():.4f}"
        ]

        for idx, item in enumerate(text_items):
            pos_y = 10 + (30 * idx )
            pyray.draw_text(item, 10, pos_y, 24, pyray.BLACK)

    def __render(self) -> None:
        with raywrap.drawing():
            with raywrap.mode_2d(self.__camera):
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
