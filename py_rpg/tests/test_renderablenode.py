from unittest import TestCase

from py_rpg.core import RenderableNode


class TestRenderableNode(TestCase):
    def setUp(self) -> None:
        self.node = RenderableNode(visible=True)

    def test_visibility(self) -> None:
        self.assertTrue(self.node.visible)
        self.node.visible = False
        self.assertFalse(self.node.visible)

    def test_render_method(self) -> None:
        with self.assertRaises(NotImplementedError):
            self.node.render()
