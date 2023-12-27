import pyray


class Window:
    __slots__ = ("__title")

    def __init__(self, width: int, height: int, title: str) -> None:
        self.__title = title
        pyray.init_window(width, height, self.__title)

    def __del__(self) -> None:
        pyray.close_window()

    @property
    def width(self) -> int:
        return int(pyray.get_screen_width())

    @property
    def height(self) -> int:
        return int(pyray.get_screen_height())

    @property
    def size(self) -> tuple[int, int]:
        return self.width, self.height

    @size.setter
    def size(self, size: tuple[int, int]) -> None:
        pyray.set_window_size(size[0], size[1])

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, new_title: str) -> None:
        self.__title = new_title
        pyray.set_window_title(new_title)
