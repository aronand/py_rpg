"""Wrappers for Raylib functions."""
from typing import Optional, Type, Literal
from types import TracebackType

import pyray

class drawing:
    """Context manager for Raylib drawing."""
    def __enter__(self) -> None:
        pyray.begin_drawing()
        pyray.clear_background(pyray.WHITE)

    def __exit__(self, 
                 type: Optional[Type[BaseException]],
                 value: Optional[BaseException],
                 traceback: Optional[TracebackType]
    ) -> Literal[False]:
        pyray.end_drawing()
        return False  # return True to suppress raised exceptions

class mode_2d:
    """Context manager for Raylib mode_2d.
    
    Objects rendered within here will be drawn in the world space.
    """
    def __init__(self, camera: pyray.Camera2D) -> None:
        self.__camera = camera

    def __enter__(self) -> None:
        pyray.begin_mode_2d(self.__camera)

    def __exit__(self, 
                 type: Optional[Type[BaseException]],
                 value: Optional[BaseException],
                 traceback: Optional[TracebackType]
    ) -> Literal[False]:
        pyray.end_mode_2d()
        return False  # return True to suppress raised exceptions
