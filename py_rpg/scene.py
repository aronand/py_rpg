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

    def __update_node_recursive(self, node: Node) -> None:
        """Recursively calls the update the method of each node in the scene"""
        for child in node.child_nodes.values():
            self.__update_node_recursive(child)
        node.update()
    
    def __get_renderables_recursive(self, node: Node) -> None:
        for child in node.child_nodes.values():
            self.__get_renderables_recursive(child)
        if isinstance(node, RenderableNode):
            self.__renderables.append(node)

    def generate_renderables(self) -> None:
        """Recursively travels through scene nodes, populating the list of renderable nodes.
        
        Calling this method again will regenerate the list. Note that the original list is cleared,
        not replaced with a new list. If you need a copy of the original state, do so before the calling
        this method.
        """
        self.__renderables.clear()
        self.__get_renderables_recursive(self.__root_node)

    def update(self) -> None:
        self.__update_node_recursive(self.__root_node)
