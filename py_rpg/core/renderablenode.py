from .node import Node
from .node2d import Node2D

import pyray


class RenderableNode(Node2D):
    """A base class for renderable game objects.
    
    Should not be instantiated, as its render() method is not implemented!
    """
    __slots__ = "visible"

    def __init__(self, node_name: str = "RenderableNode",
                 parent: Node | None = None,
                 position: pyray.Vector2 = pyray.vector2_zero(),
                 visible: bool = True) -> None:
        super().__init__(node_name=node_name, parent=parent, position=position)
        self.visible = visible

    def render(self) -> None:
        """A method that should be called during each game loop.
        
        Subclasses must implement this method!
        """
        raise NotImplementedError
