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
