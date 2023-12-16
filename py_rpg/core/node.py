"""A base class for game objects. Heavily inspired by Godot."""
from typing import Self

from attrs import define, field


@define
class Node:
    """A base class for game objects. Heavily inspired by Godot."""
    name: str = field(default="Node")
    parent: Self | None = field(default=None)
    child_nodes: list[Self] = field(init=False, factory=list)

    def add_child(self, node: Self) -> None:
        """Adds a child object to the Node.
        
        :raises TypeError: Argument is not a subclass of Node
        """
        if not issubclass(type(node), Node):
            raise TypeError
        self.child_nodes.append(node)

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
