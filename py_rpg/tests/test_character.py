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

