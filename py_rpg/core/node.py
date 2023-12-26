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
        if parent:
            parent.add_child(self)
        self.child_nodes: dict[str, "Node"] = {}

    @property
    def parent(self) -> Optional["Node"]:
        return self.__parent

    def add_child(self, node: "Node") -> None:
        """Adds a child object to the Node.
        
        :raises TypeError: Argument is not a subclass of Node
        :raises RuntimeError: Node already has a parent
        :raises RuntimeError: Child Node with same name already exists
        """
        if not issubclass(type(node), Node):
            raise TypeError
        if node.parent is not None:
            raise RuntimeError
        if node.name in self.child_nodes:
            raise RuntimeError
        node_name: str = node.name
        self.child_nodes[node_name] = node
        node.__parent = self

    def remove_child(self, node_name: str) -> Optional["Node"]:
        """Removes and returns a child object with a given name, or None if not found.
        Sets child node's parent to None.
        
        :returns: Node | None
        """
        node = self.child_nodes.pop(node_name, None)
        if node:
            node.__parent = None
        return node

    def find_child(self, node_name: str) -> Optional["Node"]:
        """Finds and returns a child object with a given name.
        
        Only returns the first object with a matching name, or None if no matches found.

        :returns: Node | None
        """
        return self.child_nodes.get(node_name, None)

    def update(self) -> None:
        """A method that should be called during each game loop.
        
        Subclasses of Node should override the behaviour to meet their unique needs.
        """
        pass
