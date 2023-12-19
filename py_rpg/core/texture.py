from typing import Optional

from .node import Node
from .renderablenode import RenderableNode

import pyray


class Texture(RenderableNode):
    __slots__ = "__texture"

    def __init__(self, node_name: str = "Texture",
                 parent: Node | None = None,
                 texture: Optional[pyray.Texture2D] = None,
                 position: pyray.Vector2 = pyray.vector2_zero()) -> None:
        super().__init__(node_name=node_name, parent=parent, position=position)
        self.__texture = texture

    def render(self) -> None:
        if not self.visible or self.__texture == None:
            return
        if self.parent is not None and hasattr(self.parent, "position"):
            position = pyray.vector2_add(self.parent.position, self.position)
            pos_x = int(position.x)
            pos_y = int(position.y)
        else:
            pos_x = int(self.position.x)
            pos_y = int(self.position.y)
        pyray.draw_texture(self.__texture, pos_x, pos_y, pyray.Color(255, 255, 255, 255))
