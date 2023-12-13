import pyray


class Character:
    __slots__ = ["__position"]
    def __init__(self):
        self.__position = pyray.Vector2(0, 0)

    @property
    def pos_x(self) -> float:
        return self.__position.x

    @property
    def pos_y(self) -> float:
        return self.__position.y
