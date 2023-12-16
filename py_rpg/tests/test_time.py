from unittest import TestCase

from py_rpg.core import Time


class TestTime(TestCase):
    def test_initial_value(self) -> None:
        self.assertEqual(0.0, Time.delta_time)

    def test_update(self) -> None:
        initial_time: float = Time.time
        Time.update()
        self.assertGreater(Time.time, initial_time)
        self.assertGreater(Time.delta_time, 0.0)
