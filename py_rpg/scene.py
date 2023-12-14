from pathlib import Path

import pyray


class Scene:
    def __init__(self, name: str, tileset: Path):
        self.__name: str = ""
        self.__characters: list[int] = []  # indices to characters that are in the scene
                                           # note that Character class probably needs a rework when it comes to position data!
        self.__tileset: pyray.Texture2D = pyray.load_texture(str(tileset))
        self.__map = None  # TODO: Figure out how we'll represent the map

    def load_scene(self, path: Path) -> None:
        pass
