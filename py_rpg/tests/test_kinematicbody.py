from unittest import TestCase

from py_rpg.core import KinematicBody

import pyray


class TestKinematicBody(TestCase):
    def setUp(self) -> None:
        self.node = KinematicBody()    

    def test_position_getters(self) -> None:
        position = pyray.Vector2(25, 36)
        self.node.position = position
        self.assertEqual(self.node.pos_x, position.x)
        self.assertEqual(self.node.pos_y, position.y)

    def test_not_moving(self) -> None:
        self.assertFalse(self.node.is_moving)

    def test_next_position(self) -> None:
        next_position = pyray.Vector2(32, 64)
        self.node.move_to(next_position)

        with self.subTest("Test KinematicBody.is_moving"):
            self.assertTrue(self.node.is_moving)
        
        with self.subTest("Test KinematicBody.next_x and KinematicBody.next_y"):
            self.assertEqual(self.node.next_x, next_position.x)
            self.assertEqual(self.node.next_y, next_position.y)
