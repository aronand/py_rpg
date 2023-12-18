from .node import Node

import pyray


class RenderableNode(Node):
    __slots__ = "position", "visible"

    def __init__(self) -> None:
        self.position = pyray.Vector2(0, 0)
        self.visible: bool = True
        super().__init__()

    def render(self) -> None:
        pass
