"""A base class for game objects. Heavily inspired by Godot."""
from typing import Self


class Node:
    """A base class for game objects."""
    __slots__ = ["name", "__parent", "child_nodes"]

    def __init__(self, name: str = "Node", parent: Self | None = None) -> None:
        self.name = name
        self.parent = parent
        self.child_nodes: list[Self] = []

    @property
    def parent(self) -> Self | None:
        return self.__parent

    @parent.setter
    def parent(self, value: Self | None) -> None:
        # TODO: If node already has a parent, remove it from parent's child_nodes
        self.__parent = value
        if value is None:
            return
        value.add_child(self)

    def add_child(self, node: Self) -> None:
        """Adds a child object to the Node.
        
        :raises TypeError: Argument is not a subclass of Node
        """
        if not issubclass(type(node), Node):
            raise TypeError
        self.child_nodes.append(node)
        node.__parent = self

    def remove_child(self, idx: int) -> Self:
        """Removes and returns a child object at given index.
        
        :returns: Node
        :raises IndexError: Given index is invalid
        """
        return self.child_nodes.pop(idx)

    def find_child(self, name: str) -> Self | None:
        """Finds and returns a child object with a given name.
        
        Only returns the first object with a matching name, or None if no matches found.

        :returns: Node or None
        """
        for child in self.child_nodes:
            if child.name != name:
                continue
            return child
        return None
