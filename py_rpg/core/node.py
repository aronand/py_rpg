"""A base class for game objects. Heavily inspired by Godot."""
from typing import Self


class Node:
    """A base class for game objects."""
    __slots__ = ["name", "parent", "child_nodes"]

    def __init__(self, name: str = "Node", parent: Self | None = None) -> None:
        self.name = name
        self.parent = parent
        if parent is not None:
            parent.add_child(self)
        self.child_nodes: list[Self] = []  # TODO: Figure out how make Mypy work with this (i.e. how to easily make Mypy know the type of Node contained here)

    def add_child(self, node: Self) -> None:
        """Adds a child object to the Node.
        
        :raises TypeError: Argument is not a subclass of Node
        """
        if not issubclass(type(node), Node):
            raise TypeError
        self.child_nodes.append(node)
        node.parent = self

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
