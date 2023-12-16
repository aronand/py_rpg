"""A base class for game objects. Heavily inspired by Godot."""
from typing import Self

from attrs import define, field


@define
class Node:
    name: str = field(default="Node")
    parent: Self | None = field(default=None)
    child_nodes: list[Self] = field(init=False, factory=list)

    def add_child(self, node: Self) -> None:
        if not issubclass(type(node), Node):
            raise TypeError
        self.child_nodes.append(node)

    def remove_child(self, idx: int) -> Self:
        return self.child_nodes.pop(idx)

    def find_child(self, name: str) -> Self | None:
        for child in self.child_nodes:
            if child.name != name:
                continue
            return child
        return None
