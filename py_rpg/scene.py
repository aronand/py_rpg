from core import Node, RenderableNode


class Scene:
    __slots__ = "__root_node", "__renderables"

    def __init__(self) -> None:
        self.__root_node = Node(node_name="SceneRoot")
        self.__renderables: list[RenderableNode] = []

    @property
    def nodes(self) -> dict[str, Node]:
        return self.__root_node.child_nodes

    @property
    def renderable_nodes(self) -> list[RenderableNode]:
        return self.__renderables

    @property
    def root_node(self) -> Node:
        return self.__root_node

    def __update_node_recursive(self, node: Node, update_renderables: bool) -> None:
        for child in node.child_nodes.values():
            self.__update_node_recursive(child, update_renderables)
        if update_renderables and isinstance(node, RenderableNode):
            self.__renderables.append(node)
        node.update()

    def update(self) -> None:
        self.__update_node_recursive(self.__root_node, len(self.__renderables) == 0)
