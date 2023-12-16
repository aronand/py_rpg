from core import KinematicBody

import pyray


class Character(KinematicBody):
    __slots__ = ["__name", "texture"]

    def __init__(self, name: str, position: pyray.Vector2 = pyray.Vector2(0, 0)):
        self.__name = name
        self.texture: pyray.Texture2D | None = None
        super().__init__(position)

    @property
    def character_name(self) -> str:  # can't use name, as this clashes with Node.name
        return self.__name
