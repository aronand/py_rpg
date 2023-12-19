from .node import Node
from .node2d import Node2D

import pyray


class RenderableNode(Node2D):
    __slots__ = "visible"

    def __init__(self, node_name: str = "RenderableNode",
                 parent: Node | None = None,
                 position: pyray.Vector2 = pyray.vector2_zero(),
                 visible: bool = True) -> None:
        super().__init__(node_name=node_name, parent=parent, position=position)
        self.visible = visible

    def render(self) -> None:
        pass
