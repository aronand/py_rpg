from .node import Node
from .node2d import Node2D
from .time import Time

import pyray


class KinematicBody(Node2D):
    __slots__ = "__next_position"

    def __init__(self, node_name: str = "KinematicBody",
                 parent: Node | None = None,
                 position: pyray.Vector2 = pyray.Vector2(0, 0)) -> None:
        super().__init__(node_name=node_name, parent=parent, position=position)
        self.__next_position = position

    @property
    def pos_x(self) -> float:
        return float(self.position.x)

    @property
    def pos_y(self) -> float:
        return float(self.position.y)

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

    def update(self) -> None:
        """
        Moves the character towards its next position.
        """
        speed_per_second = 64
        self.position = pyray.vector2_move_towards(self.position, self.__next_position, speed_per_second * Time.delta_time)
