"""A base class for game objects. Heavily inspired by Godot."""
# Need to use Optional instead of "Node" | None due to:
# TypeError: unsupported operand type(s) for |: 'str' and 'NoneType'
from typing import Optional

class Node:
    __slots__ = "name", "__parent", "child_nodes"

    def __init__(self, node_name: str = "Node", 
                 parent: Optional["Node"] = None) -> None:
        self.name = node_name
        self.__parent: "Node" | None = None
        self.parent = parent
        self.child_nodes: list["Node"] = []

    @property
    def parent(self) -> Optional["Node"]:
        return self.__parent

    @parent.setter
    def parent(self, value: Optional["Node"]) -> None:
        if self.__parent is not None:
            self.__parent.child_nodes.remove(self)
        self.__parent = value
        if value is None:
            return
        value.add_child(self)

    def add_child(self, node: "Node") -> None:
        """Adds a child object to the Node.
        
        :raises TypeError: Argument is not a subclass of Node
        """
        if not issubclass(type(node), Node):
            raise TypeError
        self.child_nodes.append(node)
        node.__parent = self

    def remove_child(self, idx: int) -> "Node":
        """Removes and returns a child object at given index.
        
        :returns: Node
        :raises IndexError: Given index is invalid
        """
        return self.child_nodes.pop(idx)

    def find_child(self, name: str) -> Optional["Node"]:
        """Finds and returns a child object with a given name.
        
        Only returns the first object with a matching name, or None if no matches found.

        :returns: Node or None
        """
        for child in self.child_nodes:
            if child.name != name:
                continue
            return child
        return None

    def update(self) -> None:
        """A method that should be called during each game loop.
        
        Subclasses of Node should override the behaviour to meet their unique needs.
        """
        pass
