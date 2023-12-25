from unittest import TestCase

from py_rpg.core import Node


class TestNode(TestCase):
    def setUp(self) -> None:
        self.node = Node()

    def test_initial_parent_node(self) -> None:
        self.assertIsNone(self.node.parent)

    def test_initial_child_nodes(self) -> None:
        self.assertEqual(0, len(self.node.child_nodes))

    def test_constructor(self) -> None:
        node = Node(node_name="Test", parent=self.node)
        self.assertEqual("Test", node.name)
        self.assertIs(node.parent, self.node)

    def test_adding_child_nodes(self) -> None:
        test_parent = Node()
        test_node = Node()

        with self.subTest("Verify type"):
            with self.assertRaises(TypeError):
                self.node.add_child(123)
        
        with self.subTest("Child must have no parent"):
            test_parent.add_child(test_node)
            with self.assertRaises(RuntimeError):
                self.node.add_child(test_node)

        with self.subTest("Parent is modified and child is added"):
            test_node2 = Node("TestNode2")
            self.node.add_child(test_node2)
            self.assertIs(test_node2.parent, self.node)
            self.assertEqual("TestNode2", self.node.find_child("TestNode2").name)

    def test_removing_child_nodes(self) -> None:
        test_node = Node("TestNode")
        with self.subTest("Child is removed from parent."):
            self.node.add_child(test_node)
            self.assertEqual(1, len(self.node.child_nodes))
            self.node.remove_child("TestNode")
            self.assertEqual(0, len(self.node.child_nodes))
        
        with self.subTest("Child's parent is set to None"):
            self.assertIsNone(test_node.parent)

    def test_finding_child_nodes(self) -> None:
        child_name = "TestChild"
        self.node.add_child(Node(child_name))
        self.assertEqual(child_name, self.node.find_child(child_name).name)
        self.assertIsNone(self.node.find_child("DoesNotExist"))
