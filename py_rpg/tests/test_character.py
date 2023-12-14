from unittest import TestCase

import pyray

from character import Character


class TestCharacter(TestCase):
    def setUp(self) -> None:
        self.character1 = Character("Test")
        self.character2 = Character("Bob", pyray.Vector2(320, 160))

    def test_name(self) -> None:
        self.assertEqual("Test", self.character1.name)

    def test_position(self) -> None:
        with self.subTest("Test default position"):
            self.assertEqual(0.0, self.character1.pos_x)
            self.assertEqual(0.0, self.character1.pos_y)
        
        with self.subTest("Test custom position"):
            self.assertEqual(320.0, self.character2.pos_x)
            self.assertEqual(160.0, self.character2.pos_y)

    def test_not_moving(self) -> None:
        self.assertFalse(self.character1.is_moving)

    def test_next_position(self) -> None:
        self.character1.move_to(pyray.Vector2(32, 64))

        with self.subTest("Test Character.is_moving"):
            self.assertTrue(self.character1.is_moving)
        
        with self.subTest("Test Character.next_x and Character.next_y"):
            self.assertEqual(32.0, self.character1.next_x)
            self.assertEqual(64.0, self.character1.next_y)
