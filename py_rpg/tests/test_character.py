from unittest import TestCase

import pyray

from character import Character


class TestCharacter(TestCase):
    def setUp(self) -> None:
        self.character1 = Character(character_name="Test")
        self.character2 = Character(character_name="Bob", position=pyray.Vector2(320, 160))

    def test_name(self) -> None:
        self.assertEqual("Test", self.character1.character_name)

    def test_stamina_properties(self) -> None:
        max_stamina = self.character1.max_stamina
        self.assertEqual(max_stamina, self.character1.cur_stamina)
        # Test that cur_stamina can't be made higher than max_stamina
        self.character1.cur_stamina = max_stamina + 1
        self.assertEqual(max_stamina, self.character1.cur_stamina)
        # Test that other value types, such as float, are not supported
        self.character1.cur_stamina = 80.0
        self.assertEqual(max_stamina, self.character1.cur_stamina)
        # Test that negative values become zero
        self.character1.cur_stamina = -1000
        self.assertEqual(0, self.character1.cur_stamina)

    def test_is_dead(self) -> None:
        self.assertFalse(self.character1.is_dead)
        self.character1.cur_stamina = 0
        self.assertTrue(self.character1.is_dead)

    def test_level_up(self) -> None:
        max_stamina = self.character1.max_stamina
        self.assertEqual(1, self.character1.level)
        self.character1.level_up()
        self.assertEqual(2, self.character1.level)
        self.assertGreater(self.character1.max_stamina, max_stamina)
