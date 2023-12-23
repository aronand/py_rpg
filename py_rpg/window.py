import pyray


class Window:
    __slots__ = ()

    def __init__(self, width: int, height: int, title: str) -> None:
        pyray.init_window(width, height, title)

    def __del__(self) -> None:
        pyray.close_window()

    @property
    def width(self) -> int:
        return int(pyray.get_screen_width())

    @property
    def height(self) -> int:
        return int(pyray.get_screen_height())
