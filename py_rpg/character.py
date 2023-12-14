import pyray


class Character:
    __slots__ = ["__name", "__position", "__next_position"]
    def __init__(self, name: str, position: pyray.Vector2 = pyray.Vector2(0, 0)):
        self.__name = name
        self.__position = position
        self.__next_position = position

    @property
    def name(self) -> str:
        return self.__name

    @property
    def pos_x(self) -> float:
        return self.__position.x

    @property
    def pos_y(self) -> float:
        return self.__position.y

    @property
    def is_moving(self) -> bool:
        return self.__position != self.__next_position

    def move_to(self, position: pyray.Vector2) -> None:
        self.__next_position = position
