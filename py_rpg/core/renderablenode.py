from .node import Node

import pyray


class RenderableNode(Node):
    __slots__ = ("__position")

    def __init__(self) -> None:
        self.__position = pyray.Vector2(0, 0)

    def render(self) -> None:
        pass
