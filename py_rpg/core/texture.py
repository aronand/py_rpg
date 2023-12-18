from .renderablenode import RenderableNode

import pyray


class Texture(RenderableNode):
    __slots__ = "__texture"

    def __init__(self, texture: pyray.Texture2D) -> None:
        self.__texture = texture
        super().__init__()

    def render(self) -> None:
        if self.parent is not None and hasattr(self.parent, "position"):
            position = pyray.vector2_add(self.parent.position, self.position)
            pos_x = int(position.x)
            pos_y = int(position.y)
        else:
            pos_x = int(self.position.x)
            pos_y = int(self.position.y)
        pyray.draw_texture(self.__texture, pos_x, pos_y, pyray.Color(255, 255, 255, 255))
