from unittest import TestCase

from py_rpg.core import Node2D

import pyray


class TestNode2D(TestCase):
    def test_default_node(self) -> None:
        default_node = Node2D()
        self.assertEqual(default_node.name, "Node2D")
        self.assertIsNone(default_node.parent)
        self.assertEqual(default_node.position.x, 0)
        self.assertEqual(default_node.position.y, 0)

    def test_setting_node_position(self) -> None:
        node: Node2D

        with self.subTest("Set position in constructor"):
            position = pyray.Vector2(100, 200)
            node = Node2D(position=position)
            self.assertEqual(node.position.x, position.x)
            self.assertEqual(node.position.y, position.y)

        with self.subTest("Set position with setter"):
            new_position = pyray.Vector2(600, 600)
            node.position = new_position
            self.assertEqual(node.position.x, new_position.x)
            self.assertEqual(node.position.y, new_position.y)
