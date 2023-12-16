"""A base class for game objects. Heavily inspired by Godot."""
from typing import Self

from attrs import define, field


@define
class Node:
    parent: Self | None = field(init=False, default=None)
    child_nodes: list[Self] = field(init=False, factory=list)

    def add_child(self, node: Self) -> None:
        if not issubclass(type(node), Node):
            raise TypeError
        self.child_nodes.append(node)
