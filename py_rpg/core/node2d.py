from .node import Node

import pyray


class Node2D(Node):
    __slots__ = "__position"

    def __init__(self, node_name: str = "Node2D",
                 parent: Node | None = None, 
                 position: pyray.Vector2 = pyray.vector2_zero()) -> None:
        super().__init__(node_name=node_name, parent=parent)
        self.__position = position

    @property
    def position(self) -> pyray.Vector2:
        return self.__position

    @position.setter
    def position(self, new_pos: pyray.Vector2) -> None:
        self.__position = new_pos
