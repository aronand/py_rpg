from .renderablenode import RenderableNode

import pyray


class Label(RenderableNode):
    __slots__ = "__font_size", "__text"

    def __init__(self, text: str = "", font_size: int = 18) -> None:
        super().__init__()
        self.__font_size = font_size
        self.__text = text

    def render(self) -> None:
        if self.parent is not None and hasattr(self.parent, "position"):
            position = pyray.vector2_add(self.parent.position, self.position)
            pos_x = int(position.x)
            pos_y = int(position.y) - self.__font_size
        else:
            pos_x = int(self.position.x)
            pos_y = int(self.position.y) - self.__font_size
        pyray.draw_text(self.__text, pos_x, pos_y, self.__font_size, pyray.BLACK)
