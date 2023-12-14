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
        return float(self.__position.x)

    @property
    def pos_y(self) -> float:
        return float(self.__position.y)

    @property
    def next_x(self) -> float:
        return float(self.__next_position.x)

    @property
    def next_y(self) -> float:
        return float(self.__next_position.y)

    @property
    def is_moving(self) -> bool:
        """
        Determines if a character is moving.
        
        Based on whether the character's position is roughly equal to the next position.
        """
        # For whatever reason comparing the vectors doesn't work, will have to investigate further
        return int(self.pos_x) != int(self.next_x) or int(self.pos_y) != int(self.next_y)

    def move_to(self, position: pyray.Vector2) -> None:
        """
        Sets the position where the character should move towards.
        """
        self.__next_position = position

    def update_position(self, delta_time: float) -> None:
        """
        Moves the character towards its next position.
        """
        speed = 64
        self.__position = pyray.vector2_move_towards(self.__position, self.__next_position, speed * delta_time)
