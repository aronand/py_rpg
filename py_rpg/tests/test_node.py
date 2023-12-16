from unittest import TestCase

from py_rpg.core import Node


class TestNode(TestCase):
    def setUp(self) -> None:
        self.node = Node()

    def test_initial_parent_node(self) -> None:
        self.assertIsNone(self.node.parent)

    def test_initial_child_nodes(self) -> None:
        self.assertEqual(0, len(self.node.child_nodes))

    def test_adding_child_nodes(self) -> None:
        with self.assertRaises(TypeError):
            self.node.add_child(123)

        self.node.add_child(Node())
        self.assertEqual(1, len(self.node.child_nodes))

    def test_removing_child_nodes(self) -> None:
        self.node.add_child(Node())
        self.assertEqual(1, len(self.node.child_nodes))
        removed = self.node.remove_child(0)
        self.assertTrue(issubclass(type(removed), Node))
        self.assertEqual(0, len(self.node.child_nodes))
        with self.assertRaises(IndexError):
            self.node.remove_child(0)

    def test_finding_child_nodes(self) -> None:
        child_name = "TestChild"
        self.node.add_child(Node(child_name))
        self.assertEqual(child_name, self.node.find_child(child_name).name)
        self.assertIsNone(self.node.find_child("DoesNotExist"))
