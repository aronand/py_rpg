from unittest import TestCase

import pyray

from character import Character


class TestCharacter(TestCase):
    def setUp(self) -> None:
        self.character = Character()

    def test_position_attributes(self) -> None:
        self.assertEqual(0.0, self.character.pos_x)
        self.assertEqual(0.0, self.character.pos_y)
