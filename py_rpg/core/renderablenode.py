from .node import Node

import pyray


class RenderableNode(Node):
    __slots__ = ("position")

    def __init__(self) -> None:
        self.position = pyray.Vector2(0, 0)
        super().__init__()

    def render(self) -> None:
        pass
