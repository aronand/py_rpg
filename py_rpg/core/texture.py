from .renderablenode import RenderableNode

import pyray


class Texture(RenderableNode):
    __slots__ = "__texture"

    def __init__(self, texture: pyray.Texture2D) -> None:
        self.__texture = texture
        super().__init__()

    def render(self) -> None:
        # TODO: Figure out how to handle this better, as right now we are very much assuming that a parent has pos_x and pos_y methods
        pos_x = int(self.parent.pos_x + self.position.x)
        pos_y = int(self.parent.pos_y + self.position.y)
        pyray.draw_texture(self.__texture, pos_x, pos_y, pyray.Color(255, 255, 255, 255))
